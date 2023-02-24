from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
 
def home_page(request : HttpRequest):

    return render(request,'main/home.html')

def profile_page(request : HttpRequest):

    return render(request,'main/profile.html')

def vaccination_schedule_page(request : HttpRequest):

    return render(request,'main/vaccination_Schedule.html')

def vaccination_reminders_page(request : HttpRequest):

    return render(request,'main/vaccination_reminders.html')

def vaccination_service_page(request : HttpRequest):

    return render(request,'main/vaccination_service.html')

def communication_service_page(request : HttpRequest):

    return render(request,'main/communication_service.html')




