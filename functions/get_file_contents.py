import os

MAX_CHARS = 10000

def get_file_contents(working_directory, file_path):
    if not file_path:
        return "Error: No file path was provided"
    else:
        file_path = os.path.join(working_directory, file_path)

    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(file_path)   

    try:
        # file is outside working directory
        if (not file_abs.startswith(f"{working_abs}/")):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'     

        # file is not a file
        if not os.path.isfile(file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # read contents of the file
        with open(file_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(file_abs) > MAX_CHARS:
                file_content_string = file_content_string + f' [...File "{file_path}" truncated at 10000 characters]'
            
        return file_content_string
    
    except Exception as e:
        return f"Error: Use of standard library functions raised an exception:\n{e}"