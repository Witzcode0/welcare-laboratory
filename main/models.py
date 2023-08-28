from django.db import models
from django.utils import timezone
from .helpers import generate_employee_id
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class EmployeeRole(BaseModel):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role

    def save(self, *args, **kwargs):
        # Convert role to lowercase before saving
        self.role = self.role.lower()
        super(EmployeeRole, self).save(*args, **kwargs)

class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, default=generate_employee_id(
        digit=6), unique=True, max_length=10)
    role = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=100)
    password = models.CharField(
        max_length=200, default=generate_employee_id(digit=8))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_id} - {self.last_name.capitalize()} {self.first_name.capitalize()}"

    def save(self, *args, **kwargs):
        # Convert first_name, last_name and email to lowercase before saving
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        self.email = self.email.lower()
        super(Employee, self).save(*args, **kwargs)