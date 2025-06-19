import os

MAX_CHARS = 10000

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
    
def get_file_content(working_directory, file_path):


    if not file_path:
        return "Error: No file path was provided"
    else:
        file_path = os.path.join(working_directory, file_path)

    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.abspath(file_path)   

    try:
        # file is outside working directory
        if (not file_abs.startswith(f"{working_abs}/")) and (not file_abs == working_abs):
            return f'Error: Cannot get contents of "{file_path}" as it is outside the permitted working directory'     

        # file is not a file
        if not os.path.isfile(file_abs):
            return f'Error: "{file_path}" is not a file'
        
        # read contents of the file
        with open(file_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(file_abs) > MAX_CHARS:
                file_content_string = file_content_string + f' [...File "{file_path}" truncated at 10000 characters]'
            
        return file_content_string
    
    except Exception as e:
        return f"Error: Use of standard library functions raised an exception:\n{e}"
