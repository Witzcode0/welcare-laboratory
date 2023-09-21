from main.models import EmployeePermissionRelation

def authenticated_employee(request):
    # Check if the user is authenticated
    if hasattr(request, 'employee'):
        # You can add any additional data you need here
        employee_permissions = EmployeePermissionRelation.objects.filter(employee=request.employee)
        
        # Create an array of employee data
        employee_data = {
            'id': request.employee.id,
            'first_name': request.employee.first_name,
            'last_name': request.employee.last_name,
            'email': request.employee.email,
            'permissions': []

        }

        for permission_ in employee_permissions:
            permission_dict = {}
            permission_dict[str(permission_.permission)] = permission_.permission_status
            employee_data['permissions'].append(permission_dict)

        print(employee_data)

        return {
            'authenticated_employee': employee_data,
            'employee_permissions': employee_permissions,
        }
    return {}
