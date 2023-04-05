#!/usr/bin/python3

from django.shortcuts import render, redirect
from .models import Patient, MedicalHistory, Appointment, Prescription

# View for retrieving a patient's medical history
def view_medical_history(request, patient_id):
     # Query the database to retrieve the patient's medical history
     patient = Patient.objects.get(id=patient_id)
     medical_history = MedicalHistory.objects.filter(patient=patient)

      # Render the template with the retrieved medical history data
       return render(request, 'medical_history.html', {'patient': patient, 'medical_history': medical_history})

# View for creating a new appointment
def create_appointment(request):
    if request.method == 'POST':
         # Retrieve form data from the POST request
         patient_id = request.POST.get('patient_id')
         date = request.POST.get('date')
         time = request.POST.get('time')

         # Create a new Appointment object and save it to the database
         patient = Patient.objects.get(id=patient_id)
         appointment = Appointment(patient=patient, date=date, time=time)
         appointment.save()

          # Redirect the user to the patient's appointments page
          return redirect('view_appointments', patient_id=patient_id)

      # Render the appointment creation form template
      return render(request, 'create_appointment.html')


#we are using Django's Object-Relational Mapping (ORM) to query and save data to the database. We define two views: one for retrieving a patient's medical history from the database and another for creating a new appointment and saving it to the database. The views use Django's built-in render() and redirect() functions to render templates and redirect the user to other pages in the application.


