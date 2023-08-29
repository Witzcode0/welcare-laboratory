from django.urls import path
from .views import * 

urlpatterns = [
    path('', login_view, name='login_view'),
    path('forgot_password_view/', forgot_password_view, name='forgot_password_view'),
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('branch_view/', branch_view, name='branch_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('payments_view/', payments_view, name='payments_view'),
    path('staff_view/', staff_view, name='staff_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('maintainance_view/', maintainance_view, name='maintainance_view')
]