from django.db import models

import datetime
from django.utils import timezone

class Department(models.Model):
    dept_type = models.CharField(max_length=64)
    function = models.CharField(max_length=750)

    def __str__(self):
        return f"{self.dept_type}"
    

class Specialization(models.Model):
    type = models.CharField(max_length=64)
    role = models.CharField(max_length=750)

    def __str__(self):
        return f"{self.type}"
    

class Doctor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    specialty = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name="experts")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="departments")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Nurse(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="wards")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Patient(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    contact = models.CharField(max_length=30)
    residential_address = models.CharField(max_length=550)
    gender = models.CharField(max_length=2)
    date_of_birth = models.DateField()

    # validate date of birth
    def valid_date_of_birth(self):
        now = timezone.now().date()
        return self.date_of_birth <= now

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Patient_Record(models.Model):
    PERIOD_ADMITTED = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night')
    ]
    check_in_date = models.DateField()
    check_in_period = models.CharField(max_length=64, choices=PERIOD_ADMITTED)
    check_out_date = models.DateField(blank=True, null=True)
    check_out_period = models.CharField(max_length=64, blank=True, choices=PERIOD_ADMITTED)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patients")
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctors")

    def valid_checkin_date(self):
        now = timezone.now().date()
        return self.check_in_date <= now

    def __str__(self):
        return f"{self.patient}"
    