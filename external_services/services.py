#!/usr/bin/python3

import requests
import json

def retrieve_patient_data(patient_id):
    fhir_url = 'https://example.com/fhir/patient/' + patient_id
    headers = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get(fhir_url, headers=headers)

    if response.status_code == 200:
        # Parse the response JSON data
        patient_data = json.loads(response.text)

        # Store the patient data in the local database
        patient = Patient(
                id=patient_data['id'],name=patient_data['name'],birthdate=patient_data['birthdate'])
        patient.save()

        return True

    else:
        #Handle any errors or exceptions

        return False



def retrieve_medication_data(medication_name):
    med_url = 'https://example.com/api/medication/' + medication_name
    headers = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get(med_url, headers=headers)

    if response.status_code == 200:
        # Parse the response JSON data
        med_data = json.loads(response.text)

        # Store the medication data in the local database
        medication = Medication(
                name=med_data['name'],
                dose=med_data['dose'],
                frequency=med_data['frequency'],
                # Add more fields as needed
                )
        medication.save()
        return True

    else:
        #Handle any errors or exceptions
        return False


