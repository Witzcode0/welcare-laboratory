import uuid
import hashlib
import random
import string
import os


def generate_employee_id(digit):
    """
    This function return unique id and default password for "EMPLOYEE/STAFF"
    Example : 
    staff_id = <six-digit-id>_EMP
    default_password = <eight-digit-id>_EMP
    """
    unique_id = uuid.uuid4()
    hashed_id = hashlib.sha256(str(unique_id).encode()).hexdigest()
    alphanumeric_id = ''.join(random.choices(string.ascii_letters + string.digits, k=digit))
    if digit == 8:
        # for default password
        return alphanumeric_id.upper() + '_CODE'
    elif digit == 6:
        # for employee id
        return alphanumeric_id.upper() + '_WL'
    else:
        return alphanumeric_id

def custom_file_name(instance, filename):
    """
    This function return unique file-name
    Example :
    file-format - <dir-name>/<unique-hex-string>.ext
    """
    # Get the file's extension
    ext = filename.split('.')[-1]

    # Generate a unique name for the file
    unique_filename = f"{uuid.uuid4().hex}.{ext}"

    # Return the new file path
    return os.path.join(f'{instance.DIR_NAME}/', unique_filename)