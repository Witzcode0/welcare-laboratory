import uuid
import hashlib
import random
import string
import os

def generate_alnum_random_string(digit):
    """
    This function return alphaNumeric random string with provided length
    """
    unique_id = uuid.uuid4()
    hashed_id = hashlib.sha256(str(unique_id).encode()).hexdigest()
    alphanumeric_id = ''.join(random.choices(string.ascii_letters + string.digits, k=digit))
    return alphanumeric_id

def generate_employee_id(digit):
    """
    This function return unique id for "EMPLOYEE/STAFF"
    Example : 
    staff_id = <six-digit-id>_WL
    """
    return generate_alnum_random_string(digit).upper() + '_WL'

def generate_employee_password(digit):
    """
    This function return  default password for "EMPLOYEE/STAFF"
    Example : 
    default_password = <eight-digit-id>_CODE
    """
    alphanumeric_id = generate_alnum_random_string(digit)
    return generate_alnum_random_string(digit).upper() + '_CODE'


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