from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def api_get_set_users(request):
    status = 202
    message = "Hello :)"
    return HttpResponse(message, status=status)
