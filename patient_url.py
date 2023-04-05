#!/usr/bin/python3

from django.urls import path
from patient_registration.views import patient_registration

urlpatterns = [
        path('register/', patient_registration, name='patient_registration'),
        # other URLs for the healthcare web application
        ]

