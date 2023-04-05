#!/usr/bin/python3

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required

# Define user roles and permissions
doctor_group = Group.objects.create(name='Doctor')
nurse_group = Group.objects.create(name='Nurse')
patient_group = Group.objects.create(name='Patient')

# Create user accounts and assign them to groups
doctor = User.objects.create_user('doctor', 'doctor@example.com', 'password')
doctor.groups.add(doctor_group)

patient = User.objects.create_user('patient', 'patient@example.com', 'password')
patient.groups.add(patient_group)

# Use decorators to enforce authentication and authorization
@login_required

def view_medical_history(request):
    # code to display medical history

@permission_required('healthcare_app.view_medical_history', raise_exception=True)
def view_medical_history(request):
    # code to display medical history for users with the view_medical_history permission


