# main/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Employee  # Replace with your actual model

# Signal handler to send an email when Employee is saved
@receiver(post_save, sender=Employee)
def send_data_saved_email(sender, instance, created, **kwargs):
    if created:
        # New instance of Employee is created (data is saved)
        subject = 'Data Saved Notification'
        message = 'Your data has been saved successfully.'
        from_email = 'brijeshgondaliya.tops@gmail.com'  # Replace with your sender email
        recipient_list = ['brijesh.gondaliya07@gmail.com']  # Replace with the recipient's email

        # Render the email template
        email_content = render_to_string('data_saved_email.html', {})

        # Send the email
        send_mail(subject, message, from_email, recipient_list, html_message=email_content)
