from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from main.models import Employee
from .helpers import create_jwt_token, generate_otp


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        try:
            employee = Employee.objects.get(
                employee_id=employee_id, password=password)
            payload = {
                'user_id': employee.employee_id
            }
            token = create_jwt_token(payload=payload)
            request.session['employee_token'] = token
            messages.success(request, 'Login successful!')
            return redirect('dashboard_view')
        except Employee.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            employee = Employee.objects.get(email=email)
            # Generate a random OTP
            otp = generate_otp()

            # Send the OTP via email
            subject = 'Password Reset OTP'
            message = f'Your OTP for password reset is: {otp}'
            from_email = settings.EMAIL_HOST_USER  # Replace with your email address
            recipient_list = [email]

            context = {
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'otp': otp
            }

            # Render the email template
            email_content = render_to_string('mail-templates\sent-otp.html', context)
            # Send the email
            send_mail(subject, message, from_email, recipient_list, html_message=email_content)

            # Store the OTP in session for later verification
            request.session['reset_otp'] = otp
            request.session['email'] = email
            messages.success(
                request, 'OTP sent to your email. Please check your inbox.')
            return render(request, 'otp-verification.html')

        except Employee.DoesNotExist:
            messages.error(
                request, 'Email not found. Please check the email address and try again.')
            return render(request, 'forgot-password.html')
    return render(request, 'forgot-password.html')


def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        reset_otp = request.session.get('reset_otp')
        email = request.session.get('email')
        print(otp, new_password, confirm_password, reset_otp, email)
        if otp == reset_otp:
            try:
                employee = Employee.objects.get(email=email)
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid email. Please try again.')
                return render(request, 'otp-verification.html')
            if new_password == confirm_password:
                employee.password = new_password
                employee.save()

                del request.session['reset_otp']
                del request.session['email']

                messages.success(request, 'Password updated successfully.')
                return redirect('login_view')  # Redirect to a success page
            else:
                messages.error(request, 'Password and Confirm Password do not match. Please try again.')
                return render(request, 'otp-verification.html')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'otp-verification.html')
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
