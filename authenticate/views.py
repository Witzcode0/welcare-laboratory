from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def branch_view(request):
    return render(request, 'branch.html')

def patients_view(request):
    return render(request, 'patients.html')

def payments_view(request):
    return render(request, 'payments.html')

def staff_view(request):
    return render(request, 'staff.html')

def maintainance_view(request):
    return render(request, 'maintainance.html')


