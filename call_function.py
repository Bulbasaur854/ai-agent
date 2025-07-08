from google.genai import types

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_contents import get_file_contents, schema_get_file_contents
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file

functions_keywords = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_contents,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    if function_call_part.name not in functions_keywords:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    function_to_call = functions_keywords[function_call_part.name]
    function_call_part.args["working_directory"] = "./calculator"
    result = function_to_call(**function_call_part.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )


            
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_contents,
        schema_run_python_file,
        schema_write_file
    ]
)