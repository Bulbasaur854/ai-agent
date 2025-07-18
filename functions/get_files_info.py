import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    if not directory or directory == ".":
        directory = working_directory
    else:
        directory = os.path.join(working_directory, directory)

    working_abs = os.path.abspath(working_directory)
    directory_abs = os.path.abspath(directory)   

    try:
        # directory is outside working directory
        if (not directory_abs.startswith(f"{working_abs}/")) and (not directory_abs == working_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'     

        # directory is not a directory
        if not os.path.isdir(directory_abs):
            return f'Error: "{directory}" is not a directory'
        
        directory_list = os.listdir(directory_abs)
        contents = []
        for dir in directory_list:
            dir_abs = directory_abs + "/" + dir
            contents.append(f"- {dir}: file_size={os.path.getsize(dir_abs)} bytes, is_dir={os.path.isdir(dir_abs)}")
        
        return "\n".join(contents)
    
    except Exception as e:
        return f"Error: Use of standard library functions raised an exception:\n{e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)