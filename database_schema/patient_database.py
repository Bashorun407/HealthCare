#!/usr/bin/python3

from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=100)
    description = models.TextField()

#we have defined two models: Patient and Appointment. The Patient model has fields for the patient's first name, last name, email, password, date of birth, gender, and phone number. The Appointment model has a foreign key to the Patient model, a date field, a doctor field, and a description field

