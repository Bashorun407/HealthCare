#!/usr/bin/python3 

#Create a Python class to represent the User, and add attributes such as username, password, and role. The role attribute can be used to specify whether the user is a patient, doctor, or admin.

class Patient:
    def __init__(self, name, age, gender, contact_info, medical_history, prescription_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self.medical_history = medical_history
        self.prescription_info = prescription_info

