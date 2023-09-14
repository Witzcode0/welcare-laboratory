from django.shortcuts import render
from django.conf import settings

from main.models import Employee

import jwt


# Create your views here.
def dashboard_view(request):
    try:
        token = request.session.get('employee_token')
        secret_key = settings.SECRET_KEY
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        employee = Employee.objects.get(employee_id=decoded_token['user_id'])
        print(employee.first_name, employee.last_name, employee.email)
    except jwt.ExpiredSignatureError:
        print("Your session has expired please login again !!!")
    except jwt.DecodeError:
        print("Token decoding failed.")
    except Employee.DoesNotExist:
        # Handle the case where the employee with the specified ID does not exist
        print("Employee not found")
    context = {
        'employee':employee
    }
    return render(request, 'dashboard.html', context)


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