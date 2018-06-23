from django.db import models


class Company(models.Model):
    # This model is the responsible to receive all companies data
    name = models.CharField(max_length=100)

    # Created at and Updated ad automatic values
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.name


class Location(models.Model):
    # This model is the responsible to receive all branches or companies locations
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=3)
    state = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    timezone = models.CharField(max_length=50)
    auto_break = models.BooleanField(default=0)

    dailyOvertimeMultiplier = models.DecimalField(max_digits=5, decimal_places=2)
    dailyOvertimeThreshold = models.SmallIntegerField()
    overtime = models.BooleanField()
    weeklyOvertimeMultiplier = models.SmallIntegerField()
    weeklyOvertimeThreshold = models.IntegerField()

    # Created at and Updated ad automatic values
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class LocationLabourSettings(models.Model):
    # Since each location have his own labour settings, this model retain them
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    break_length = models.SmallIntegerField()
    threshold = models.SmallIntegerField()

    # Created at and Updated ad automatic values
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location
