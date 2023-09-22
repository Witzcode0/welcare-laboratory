from django.db import models
from main.models import BaseModel

class Doctor(BaseModel):
    profile = models.ImageField(upload_to='doctor_profiles/')  # Assuming you want to upload doctor profile pictures
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.name
