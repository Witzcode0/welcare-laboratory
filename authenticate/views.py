from django.shortcuts import render

# Create your views here.
def login_view(request):
    
    return render(request, 'login.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def otp_verification(request):
    return render(request, 'otp-verification.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def branch_view(request):
    return render(request, 'branch.html')

def patients_view(request):
    return render(request, 'patients.html')

def patient_details_view(request):
    return render(request, 'patient-details.html')

def payments_view(request):
    return render(request, 'payments.html')

def staff_view(request):
    return render(request, 'staff.html')

def doctors_view(request):
    return render(request, 'doctors.html')

def wallet_view(request):
    return render(request, 'wallet.html')

def profile_view(request):
    return render(request, 'profile.html')

def notification_view(request):
    return render(request, 'notification.html')

def maintainance_view(request):
    return render(request, 'maintainance.html')


