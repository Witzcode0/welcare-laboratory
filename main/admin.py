from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Employee, EmployeeRole, Permission, EmployeePermissionRelation
from .admin_pagination import admin_pagination


# Change the site header
admin.site.site_header = "Welcare Laboratory Management System"

# Change the site title
admin.site.site_title = "Welcare"

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(EmployeeRole)
@admin_pagination(per_page=5)
class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('role',)  # Display the 'role' field in the list view
    list_filter = ('role',)   # Add a filter sidebar for 'role'
    search_fields = ('role',) # Add a search bar for 'role'
    ordering = ('role',)
    
    fieldsets = (
        ('Role Information', {
            'fields': ('role',),
        }),
    )


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_name',)
    # Add any other customization you need for the Permission model admin.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('employee_id', 'first_name', 'last_name', 'email', 'mobile')
    list_editable = ('first_name', 'last_name', 'email')
    # Add any other customization you need for the Employee model admin.

@admin.register(EmployeePermissionRelation)
class EmployeePermissionRelationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'permission', 'permission_status')
    list_filter = ('permission_status',)
    search_fields = ('employee__employee_id', 'permission__permission_name')
    # Add any other customization you need for the EmployeePermissionRelation model admin.
