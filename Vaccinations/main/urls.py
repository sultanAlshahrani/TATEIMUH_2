from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
     path("", views.home_page, name="home_page"),
     path("profile/", views.profile_page, name="profile_page"),
     path("vaccination_Schedule/", views.vaccination_schedule_page, name="vaccination_schedule_page"),
     path("vaccination_reminders/", views.vaccination_reminders_page, name="vaccination_reminders_page"),
     path("vaccination_service/", views.vaccination_service_page, name="vaccination_service_page"),
     path("communication_service/", views.communication_service_page, name="communication_service_page"),


]
