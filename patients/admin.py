from django.contrib import admin
from .models import Patient, Payment

class PaymentInline(admin.TabularInline):
    model = Payment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'mobile_number', 'conditions')
    search_fields = ('first_name', 'last_name', 'mobile_number')
    inlines = [PaymentInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('patient','date_and_time', 'total_payment', 'paid_payment', 'rest_payment', 'status')
    list_filter = ('status',)
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__mobile_number')

    def save_model(self, request, obj, form, change):
        # Automatically calculate and update the rest_payment field when saving a payment
        obj.rest_payment = obj.total_payment - obj.paid_payment
        super().save_model(request, obj, form, change)