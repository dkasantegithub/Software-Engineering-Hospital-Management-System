from django.test import Client, TestCase

from .models import Department, Specialization, Doctor, Nurse, Patient, Patient_Record

import datetime
from django.utils import timezone

from django.db.models import Q
# mail = Doctor.objects.filter( Q(email__contains="@") & Q(email__contains="."))


class ModelsTestCase(TestCase):

    # setup models for testing
    def setUp(self):

        # create department
        d1 = Department.objects.create(dept_type="OPD", function="OPD services")
        d2 = Department.objects.create(dept_type="IPD", function="IPD services")

        # create specialization
        s1 = Specialization.objects.create(type="Optometrist", role="checks eye")
        s2 = Specialization.objects.create(type="Dentist", role="checks teeth")

        # create doctors
        dc1 = Doctor.objects.create(first_name="Robin", last_name="Jackson", email="robin@gmail.com",
        specialty=s2, department=d2)
        dc2 = Doctor.objects.create(first_name="Akuffo", last_name="Ronaldo", email="akuro@gmail.com",
        specialty=s1, department=d1)
        dc3 = Doctor.objects.create(first_name="Gideon", last_name="Ashely", email="gash@gmail.com",
        specialty=s1, department=d2)

        # create nurses
        n1 = Nurse.objects.create(first_name="Emmanuel", last_name="Dickson", email="emmadic@gmail.com",
        department=d2)
        n2 = Nurse.objects.create(first_name="Afia", last_name="Kuma", email="afiak@gmail.com",
        department=d1)

        # create patients
        p1 = Patient.objects.create(first_name="Bob", last_name="Harry", contact=233434,
        residential_address="kumasi", gender="M", date_of_birth="2020-05-01")
        p2 = Patient.objects.create(first_name="Harry", last_name="Potter", contact=84534524,
        residential_address="obuasi", gender="M", date_of_birth="1994-03-05")

        # create patient records
        pr1 = Patient_Record.objects.create(check_in_date="2020-03-01", check_in_period="morning",
        check_out_date="2020-03-02", check_out_period="evening", patient=p1, assigned_doctor=dc1)

        pr2 = Patient_Record.objects.create(check_in_date="2020-04-11", check_in_period="afternoon",
        check_out_date="2020-04-21", check_out_period="morning", patient=p2, assigned_doctor=dc1)




    # main test functions

    # TEST DOCTOR MODEL
    def test_experts_count(self):
        """
        test the relationship of Specialization with 'experts' of doctor model  
        """
        expert = Specialization.objects.get(type="Optometrist")
        self.assertEqual(expert.experts.count(), 2)


    def test_departments_count(self):
        """
        test that 'departments' relats to the departments in the hospital
        """
        department = Department.objects.get(dept_type="OPD")
        self.assertEqual(department.departments.count(), 1)


    def test_email_at_sign_for_doctor(self):
        """
        test that email is not valid (does not contain @)
        """
        at_sign = Doctor(email="davidgmail.com")
        self.assertNotIn("@", at_sign.email)

    
    def test_email_dot_sign_for_doctor(self):
        """
        test that email is not valid (does not contain .)
        """
        dot_sign = Doctor(email="asantedavid@gmailcom")
        self.assertNotIn(".", dot_sign.email)

    
    def test_email_is_valid_for_doctor(self):
        """
        test that email is valid (contains @ and .)
        """
        valid_mail = Doctor(email="david@gmail.com")
        self.assertTrue("." in valid_mail.email and "@" in valid_mail.email)




    
    # TEST NURSE MODEL
    def test_email_dot_sign_for_nurse(self):
        """
        test that email is not valid (does not contain .)
        """
        dot_sign = Nurse(email="nurse@gmailcom")
        self.assertNotIn(".", dot_sign.email)


    def test_email_at_sign_for_nurse(self):
        """
        test that email is not valid(does not contain @)
        """
        at_sign = Nurse(email="nursegmail.com")
        self.assertNotIn("@", at_sign.email)


    def test_email_is_valid_for_nurse(self):
        """
        test that email is valid(contains @ and .)
        """
        mail = Nurse(email="nurse@gmail.com")
        self.assertTrue("@" in mail.email and "." in mail.email)


    # def test_email_is_unique(self):
    #     """
    #     test that email is unique for each nurse
    #     """
    #     n1 = Nurse(email = "nurse@gmail.com")
    #     n2 = Nurse(email = "nurse@gmail.com")
    #     self.assertEqual(n1.email, n2.email)

    def test_wards_count(self):
        """
        test the relationship of departments with Nurse 'wards' of the Nurse model
        """
        ward = Department.objects.get(dept_type="OPD")
        self.assertEqual(ward.wards.count(), 1)





    # TEST PATIENT MODEL
    def test_valid_date_of_birth_with_past_date(self):
        """
        valid_date_of_birth returns True for date of birth with past date
        """
        date = timezone.now().date() - datetime.timedelta(days=1)
        past_date = Patient(date_of_birth=date)
        self.assertIs(past_date.valid_date_of_birth(), True)


    def test_valid_date_of_birth_with_present_date(self):
        """
        valid_date_of_birth returns True for date of birth with present date
        """
        date = timezone.now().date()
        present_date = Patient(date_of_birth=date)
        self.assertTrue(present_date.valid_date_of_birth())

    
    def test_valid_date_of_birth_with_future_date(self):
        """
        valid_date_of_birth returns False for date of birth with future date
        """
        date = timezone.now().date() + datetime.timedelta(days=1)
        future_date = Patient(date_of_birth=date)
        self.assertFalse(future_date.valid_date_of_birth())




    # TEST PATIENT RECORD MODEL
    def test_patients_relationship(self):
        """
        test that patients relates with patient records model
        """
        p1 = Patient.objects.get(Q(first_name="Bob") & Q(last_name="Harry"))
        self.assertEqual(p1.patients.count(), 1)


    def test_assigned_doctor_relationship(self):
        """
        test that assigned doctor relates to doctor model
        """
        d1 = Doctor.objects.get(Q(first_name="Robin") & Q(last_name="Jackson"))
        self.assertEqual(d1.doctors.count(), 2)


    def test_valid_checkin_date_for_past_date(self):
        """
        test that checkin date returns True for past dates
        """
        date = timezone.now().date() -  datetime.timedelta(days=1)
        past_date = Patient_Record(check_in_date = date)
        self.assertTrue(past_date.valid_checkin_date())


    def test_valid_checkin_date_for_present_date(self):
        """
        test that checkin date returns True for present date
        """
        date = timezone.now().date()
        present_date = Patient_Record(check_in_date=date)
        self.assertTrue(present_date.valid_checkin_date())


    def test_valid_checkin_date_for_future_date(self):
        """
        test that checkin date returns False for future date
        """
        date = timezone.now().date() + datetime.timedelta(days=1)
        future_date = Patient_Record(check_in_date=date)
        self.assertFalse(future_date.valid_checkin_date())








    # TEST VIEWS
    # test index view
    def test_index_view(self):
        """
        test that index response status code is 200
        """
        c1 = Client()
        response = c1.get("/")
        self.assertEqual(response.status_code, 200)


    def test_patient_information_view(self):
        """
        test that patient information view is valid
        """
        c2 =Client()
        response = c2.get("/patient-information/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["patients"].count(), 2)