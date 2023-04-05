#!/usr/bin/python3

#Create a Python class to represent the User, and add attributes such as username, password, and role. The role attribute can be used to specify whether the user is a patient, doctor, or admin.

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

