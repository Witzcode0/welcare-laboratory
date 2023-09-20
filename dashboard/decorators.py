import jwt
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from main.models import Employee, EmployeePermissionRelation

def authentication_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.session.get('employee_token')
            secret_key = settings.SECRET_KEY
            decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
            employee = Employee.objects.get(employee_id=decoded_token['user_id'])
            request.employee = employee  # Store the authenticated employee in the request object
            
            # Retrieve related data from EmployeePermissionRelation for the authenticated employee
            employee_permissions = EmployeePermissionRelation.objects.filter(employee=employee)
            
            # Add the related data to the request object
            request.employee_permissions = employee_permissions
            
            return view_func(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            messages.error(request, "Your session has expired. Please log in again.")
            return redirect('login_view')
        except jwt.DecodeError:
            messages.error(request, "Authentication failed. Please log in again.")
            return redirect('login_view')
        except Employee.DoesNotExist:
            messages.error(request, "Employee not found. Please log in again.")
            return redirect('login_view')
    
    return wrapper
