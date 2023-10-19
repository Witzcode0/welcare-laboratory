from django.urls import path
from .views import *

urlpatterns = [
    path('add_patient/', add_patient, name="add_patient"),
] 