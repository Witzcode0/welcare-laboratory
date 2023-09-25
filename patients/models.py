from django.db import models
from django.db.models import F
from datetime import datetime
from main.models import BaseModel

class Patient(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=15)
    conditions = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Payment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    paid_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True) 
    rest_payment = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    STATUS_CHOICES = (
        ('paid', 'paid'),
        ('partially', 'partially'),
        ('pending', 'pending'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        # Calculate rest payment
        self.rest_payment = self.total_payment - self.paid_payment

        # Determine the payment status
        if self.paid_payment == self.total_payment:
            self.status = 'paid'
        elif self.paid_payment > 0:
            self.status = 'partial'  # Corrected status value
        else:
            self.status = 'pending'

        super(Payment, self).save(*args, **kwargs)
