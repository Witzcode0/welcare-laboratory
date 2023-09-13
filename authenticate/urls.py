from django.urls import path
from .views import * 

urlpatterns = [
    path('', login_view, name='login_view'),
    path('forgot_password_view/', forgot_password_view, name='forgot_password_view'),
    path('otp_verification/', otp_verification, name='otp_verification'),
    
]