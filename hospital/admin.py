from django.contrib import admin
from .models import Department, Specialization, Doctor, Nurse, Patient, Patient_Record

admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Patient_Record)
