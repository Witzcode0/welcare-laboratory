from django.contrib import admin
from .models import Employee, EmployeeRole, Permission, EmployeePermissionRelation

# Change the site header
admin.site.site_header = "Welcare Laboratory Management System"

# Change the site title
admin.site.site_title = "Welcare"

@admin.register(EmployeeRole)
class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
    # Add any other customization you need for the EmployeeRole model admin.

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_name',)
    # Add any other customization you need for the Permission model admin.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('employee_id', 'first_name', 'last_name', 'email', 'mobile')
    # Add any other customization you need for the Employee model admin.

@admin.register(EmployeePermissionRelation)
class EmployeePermissionRelationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'permission', 'permission_status')
    list_filter = ('permission_status',)
    search_fields = ('employee__employee_id', 'permission__permission_name')
    # Add any other customization you need for the EmployeePermissionRelation model admin.
