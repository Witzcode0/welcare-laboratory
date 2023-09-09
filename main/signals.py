# main/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Employee  # Replace with your actual model

@receiver(post_save, sender=Employee)
def send_data_saved_email(sender, instance, created, **kwargs):
    """
    This signal handler to send an email when Employee is saved
    """
    if created:
        # New instance of Employee is created (data is saved)

        subject = f"Employee Login Credentials for {instance.first_name} {instance.last_name} at Welcare Laboratory"
        message = 'Your data has been saved successfully.'
        from_email = settings.EMAIL_HOST_USER  # Replace with your sender email
        recipient_list = [f'{instance.email}']  # Replace with the recipient's email

        context = {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'employee_id': instance.employee_id,
            'employee_password': instance.password
        }
        # Render the email template
        email_content = render_to_string('mail-templates\employee-login-credentials.html', context)
        # Send the email
        send_mail(subject, message, from_email, recipient_list, html_message=email_content)
