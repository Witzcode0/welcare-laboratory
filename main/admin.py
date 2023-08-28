from django.contrib import admin
from .models import Employee, EmployeeRole
# Register your models here.

admin.site.register(EmployeeRole)
admin.site.register(Employee)
