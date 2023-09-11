import uuid
import os

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