from django.urls import path
from . import views

app_name='hospital'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("patient-registration/", views.patient_registration, name="add_patient"),
    path("patient-information/", views.patient_information, name="patient_info"),
    path("patient-log/", views.patient_log, name="patient_log")
]