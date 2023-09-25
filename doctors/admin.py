from django.contrib import admin
from .models import Doctor  # Import the Doctor model from your app

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')
    list_filter = ('designation',)

    fieldsets = (
        (None, {
            'fields': ('name', 'designation', 'summary')
        }),
        ('Profile', {
            'fields': ('profile',)
        }),
    )

    # readonly_fields = ('profile',)  # Make the profile field read-only in the admin panel

    def has_delete_permission(self, request, obj=None):
        return False  # Disable the ability to delete doctor records in the admin panel

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('name', 'designation')  # Make name and designation read-only when editing
        return self.readonly_fields