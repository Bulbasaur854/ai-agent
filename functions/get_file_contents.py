import os
from google.genai import types
from config import MAX_CHARS

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
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)