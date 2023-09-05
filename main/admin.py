from django.contrib import admin
from .models import Employee, EmployeeRole
# Register your models here.

admin.site.register(EmployeeRole)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'role', 'first_name', 'last_name', 'email', 'mobile')