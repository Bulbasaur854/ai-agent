import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    if not file_path:
        return "Error: No file path was provided"

    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(os.path.join(working_directory, file_path)) 

    # file is outside working directory
    if (not file_abs.startswith(f"{working_abs}/")):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # the file does not exist
    if not os.path.exists(file_abs):
        return f'Error: File "{file_path}" not found.'
    
    # provided file is not a python file
    if not file_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try: 
        commands = ["python3", file_abs]
        if args:
            commands.extend(args)
        # execute the python file
        run_result = subprocess.run(commands, timeout=30, capture_output=True, text=True, cwd=working_abs)

        output = []
        if run_result.stdout:
            output.append(f"STDOUT:\n{run_result.stdout}")
        if run_result.stderr:
            output.append(f"STDERR:\n{run_result.stderr}")
        if run_result.returncode != 0:
            output.append(f"Process exited with code {run_result.returncode}")
        
        return "\n".join(output) if output else "No ouput produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)