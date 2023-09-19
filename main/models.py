from django.db import models
from django.utils import timezone
import string
import random



class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class EmployeeRole(BaseModel):
    role = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role

    def save(self, *args, **kwargs):
        # Convert role to lowercase before saving
        self.role = self.role.lower()
        super(EmployeeRole, self).save(*args, **kwargs)

   

class Permission(BaseModel):
    permission_name = models.CharField(max_length=255)

    def __str__(self):
        return self.permission_name

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, editable=False)
    role = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    mobile = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200, blank=True)  # Allow password to be blank initially
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_id

    def save(self, *args, **kwargs):
        if not self.employee_id:
            # Generate the custom ID if it doesn't exist
            last_id = Employee.objects.all().order_by('-id').first()
            if last_id:
                last_id = last_id.employee_id
                last_id = last_id.replace('WL', '')
                last_id = int(last_id)
                new_id = f'WL{str(last_id + 1).zfill(4)}'
            else:
                new_id = 'WL0001'
            self.employee_id = new_id

        if not self.password:
            # Generate a random password
            password_characters = string.ascii_letters + string.digits
            random_password = ''.join(random.choice(password_characters) for i in range(6))
            self.password = random_password.upper() + "_CODE"

        super(Employee, self).save(*args, **kwargs)

class EmployeePermissionRelation(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    permission_status = models.BooleanField(default=False)

    def __str__(self):
        status = "Allowed" if self.permission_status else "Denied"
        return f"{self.employee} - {self.permission} ({status})"

    class Meta:
        # Add a unique constraint to ensure that each combination of employee and permission is unique
        unique_together = ('employee', 'permission')