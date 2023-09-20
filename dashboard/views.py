from django.shortcuts import render, redirect
from django.conf import settings

from main.models import Employee,Permission
from .decorators import authentication_required

# Create your views here.
@authentication_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@authentication_required
def branch_view(request):
    return render(request, 'branch.html')

@authentication_required
def patients_view(request):
    return render(request, 'patients.html')

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