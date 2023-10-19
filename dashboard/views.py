from django.shortcuts import render, redirect
from django.conf import settings

from main.models import Employee,Permission
from patients.models import Patient, Payment
from .decorators import authentication_required

from datetime import datetime

import json


# Create your views here.
@authentication_required
def dashboard_view(request):
    # Get the current date
    current_date = datetime.now().date()
    current_day = datetime.now().strftime("%A")
    
    # Retrieve payments for the current date
    payments_today = Payment.objects.filter(date_and_time__date=current_date)
    data = []
    for payment in payments_today:
        payment_data = {
            
            'patient_name': f"{payment.patient.first_name} {payment.patient.last_name}",
            'mobile_number': f"{payment.patient.mobile_number}",
            'payment_status': payment.status,
            'conditions' :payment.patient.conditions
        }
        data.append(payment_data)
    print(data)
    return render(request, 'dashboard.html', {'data': data, 'current_date':current_date, 'current_day':current_day})

@authentication_required
def branch_view(request):
    return render(request, 'branch.html')

@authentication_required
def patients_view(request):
    patients = Patient.objects.all()
    patient_data = [{'id': patient.id, 'name': f'{patient.first_name} {patient.last_name}', 'mobile': patient.mobile_number, 'age': patient.age, 'condition': patient.conditions} for patient in patients]
    patient_data_json = json.dumps(patient_data)
    print(patient_data_json)
    return render(request, 'patients.html', {'patients': patients, 'patient_data_json': patient_data_json})

@authentication_required
def patient_details_view(request):
    return render(request, 'patient-details.html')

@authentication_required
def payments_view(request):
    return render(request, 'payments.html')

@authentication_required
def staff_view(request):
    return render(request, 'staff.html')

@authentication_required
def doctors_view(request):
    return render(request, 'doctors.html')

@authentication_required
def wallet_view(request):
    return render(request, 'wallet.html')

@authentication_required
def profile_view(request):
    context = {
        'employee': request.employee,
    }
    return render(request, 'profile.html')
    

@authentication_required
def notification_view(request):
    return render(request, 'notification.html')

def maintainance_view(request):
    return render(request, 'maintainance.html')