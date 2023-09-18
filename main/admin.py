from django.contrib import admin
from django.contrib import messages
from .models import Employee, EmployeeRole
# Register your models here.

admin.site.register(EmployeeRole)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'role', 'first_name', 'last_name', 'email', 'mobile')

    # def response_add(self, request, obj, post_url_continue=None):
    #     print(request.body)
    #     print(obj.first_name, "=-=-=")
    #     messages.success(request, "Employee has been added successfully.")  # Add a success message
    #     return super().response_add(request, obj, post_url_continue)