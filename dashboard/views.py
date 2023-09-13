from django.shortcuts import render
from django.conf import settings
import jwt
# Create your views here.
def dashboard_view(request):
    print(request.session.get('employee_token'))
    token = request.session.get('employee_token')
    try:
        secret_key = settings.SECRET_KEY
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        print(decoded_token)
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.DecodeError:
        print("Token decoding failed.")
    context = {
        'user':decoded_token
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