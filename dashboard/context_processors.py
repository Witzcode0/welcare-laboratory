# context_processors.py

from main.models import Employee, EmployeePermissionRelation
from .decorators import authentication_required

@authentication_required
def employee_data(request):
    if hasattr(request, 'employee'):
        employee = request.employee
        employee_permissions = request.employee_permissions
        employee_role = employee.role

        return {
            'employee_data': {
                'employee_id': employee.employee_id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'mobile': employee.mobile,
                'role': employee_role.role,
                'is_active': employee.is_active,
                'is_staff': employee.is_staff,
                'permissions': [
                    {
                        'permission_name': permission.permission.permission_name,
                        'permission_status': permission.permission_status,
                    }
                    for permission in employee_permissions
                ],
            }
        }
    else:
        # Return an empty dictionary if no employee is authenticated
        return {}

