from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('branch_view/', branch_view, name='branch_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('patient_details_view/', patient_details_view, name='patient_details_view'),
    path('payments_view/', payments_view, name='payments_view'),
    path('staff_view/', staff_view, name='staff_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('wallet_view/', wallet_view, name='wallet_view'),
    path('profile_view/', profile_view, name='profile_view'),
    path('notification_view/', notification_view, name='notification_view'),
    path('maintainance_view/', maintainance_view, name='maintainance_view')
]
