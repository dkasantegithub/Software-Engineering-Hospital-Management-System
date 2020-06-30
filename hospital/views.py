from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterForm, PatientLogForm
from .models import Patient, Patient_Record


def index(request):
    if not request.user.is_authenticated:
        return render(request, "hospital/login.htm", {"message": None})
    context = {}
    return render(request, "hospital/index.htm", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('hospital:index'))
        else:
            return render(request, "hospital/login.htm", {"message": "Invalid credentials"})
    else:
        return render(request, "hospital/login.htm",)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('hospital:login'))


def patient_registration(request):
    # check whether request is POST
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            contact = form.cleaned_data['contact']
            residential_address = form.cleaned_data['residential_address']
            date_of_birth = form.cleaned_data['date_of_birth']
            
            # if form is valid, create patient
            patient = Patient.objects.create(
                first_name=first_name, last_name=last_name, gender=gender, contact=contact,
                residential_address=residential_address, date_of_birth=date_of_birth
            )
            return HttpResponseRedirect(reverse('hospital:patient_log'))
    else:
        form = RegisterForm()
    return render(request, "hospital/add_patient.htm", {'form':form})


def patient_log(request):
    if request.method == 'POST':
        form = PatientLogForm(request.POST)
        if form.is_valid():
            check_in_date=form.cleaned_data['check_in_date']
            check_in_period = form.cleaned_data['check_in_period']
            check_out_date=form.cleaned_data['check_out_date']
            check_out_period = form.cleaned_data['check_out_period']
            patient=form.cleaned_data['patient']
            assigned_doctor = form.cleaned_data['assigned_doctor']

            log = Patient_Record.objects.create(
                check_in_date=check_in_date, check_in_period=check_in_period, 
                check_out_date=check_out_date, check_out_period=check_out_period,
                patient=patient, assigned_doctor=assigned_doctor
            )
            return HttpResponseRedirect(reverse('hospital:index'))
    else:
        form = PatientLogForm()
    return render(request, "hospital/patient_log.htm", {'form': form})



def patient_information(request):
    context = {
        "patients": Patient.objects.all(),
    }
    return render(request, "hospital/patient_info.htm", context)
    