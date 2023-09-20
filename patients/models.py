from django.db import models
from django.utils import timezone
from main.models import BaseModel

class Patient(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=15)
    conditions = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Payment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment of ${self.amount} by {self.patient.first_name} {self.patient.last_name}"