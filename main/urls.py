from django.urls import path
from . import views
urlpatterns = [
    path('custom_404/', views.custom_404_view, name='custom_404'),
]