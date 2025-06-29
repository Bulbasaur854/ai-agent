import os
from google.genai import types

def write_file(working_directory, file_path, content):
    if not file_path:
        return "Error: No file path was provided"
    else:
        file_path = os.path.join(working_directory, file_path)

    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(file_path)  

    try:
        # file is outside working directory
        if (not file_abs.startswith(f"{working_abs}/")):
            return f'Error: Cannot get contents of "{file_path}" as it is outside the permitted working directory'   
          
        # if a directory exists where a file should be, abort
        if os.path.isdir(file_abs):
            return f'Error: "{file_path}" exists as a directory, expected a file'

        # if the file path does not exist, create it
        if not os.path.exists(file_abs):
            os.makedirs(os.path.dirname(file_abs), exist_ok=True)                   
        
        # overwrite / write contents to file in file path
        with open(file_abs, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: Use of standard library functions raised an exception:\n{e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)