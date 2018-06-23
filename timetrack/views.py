import json

from django.http import HttpResponse

import requests

from timetrack.models import Company, Location, AutoBreakRules


def api_get_set_companies_and_settings(request):
    # This function just get companies from API
    can_go = True
    status = 200
    url = "https://shiftstestapi.firebaseio.com/locations.json"
    json_data = requests.get(url).json()
    data = json.dumps(json_data["25753"])
    data = json.loads(data)

    # As we doesn't have a company, I will just create a fake company
    # Check if it was already created
    try:
        company_obj = Company.objects.get(id=25753)
    except Company.DoesNotExist:
        company_obj = Company.objects.create(
            id=25753,
            name="7Shifts",
        )
        try:
            company_obj.save()
        except Exception as e:
            print("Something bad happens... Take a look: ", e)
            can_go = False

    if can_go:
        # Save company location
        location = Location.objects.create(
            address=data["address"],
            country=data["country"],
            state=data["state"],
            city=data["city"],
            lat=data["lat"],
            lng=data["lng"],
            timezone=data["timezone"],
            auto_break=bool(data["labourSettings"]["autoBreak"]),
            dailyOvertimeMultiplier=data["labourSettings"]["dailyOvertimeMultiplier"],
            dailyOvertimeThreshold=data["labourSettings"]["dailyOvertimeThreshold"],
            overtime=data["labourSettings"]["overtime"],
            weeklyOvertimeMultiplier=data["labourSettings"]["weeklyOvertimeMultiplier"],
            weeklyOvertimeThreshold=data["labourSettings"]["weeklyOvertimeThreshold"],
            company=company_obj
        )

        try:
            location.save()
            message = "ok"
        except Exception as e:
            message = "Houston we've got a problem. Something goes wrong when we tried to save the database. Take a look: " + str(e)
            status = 404
            can_go = False
    else:
        message = "Houston we've got a problem. Something goes wrong when we tried to save to the database"
        status = 404

    if can_go:  # So, get settings
        autobreak_rules = json.dumps(data["labourSettings"]["autoBreakRules"])
        autobreak_rules = json.loads(autobreak_rules)
        for rule in autobreak_rules:
            new_rule = AutoBreakRules.objects.create(
                break_length=rule["breakLength"],
                threshold=rule["threshold"],
                location=location
            )
            try:
                new_rule.save()
            except Exception as e:
                message = "Houston we've got a problem. Something goes wrong when we tried to save the database. Take a look: " + str(
                    e)
                status = 404
                break

    return HttpResponse(message, status=status)
