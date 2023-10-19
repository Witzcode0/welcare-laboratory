from django.shortcuts import render, redirect
from .models import Patient, Payment
from django.contrib import messages
from dashboard.decorators import authentication_required

import json
# Create your views here.

@authentication_required
def add_patient(request):
    if request.method == 'POST':
        # Get data from the form using request.POST['field_name']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        age = request.POST['age']
        mobile_number = request.POST['mobile']
        conditions = request.POST['condition']
        total_payment = request.POST['total-payment']
        paid_payment = request.POST['paid-payment']

        new_patient = Patient(
            first_name=first_name,
            last_name=last_name,
            age=age,
            mobile_number=mobile_number,
            conditions=conditions
        )
        new_patient.save()
         # Create a new Payment object
        new_payment = Payment(
            patient=new_patient,  # Link the Payment to the Patient
            total_payment=float(total_payment),
            paid_payment=float(paid_payment),
            # You may need to calculate 'rest_payment' here based on your logic
        )
        
        # Save the payment object to the database
        new_payment.save()
        success_message = f'Patient {first_name} {last_name} has been added successfully.'
        messages.success(request, success_message)
        return redirect('dashboard_view')
    
