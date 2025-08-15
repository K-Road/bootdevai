import os
from google.genai import types

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

def get_files_info(working_directory, directory="."):
    fullpath = os.path.join(working_directory, directory)
    
    resolved_fullpath = os.path.abspath(fullpath)
    resolved_working_dir = os.path.abspath(working_directory)

    if not (resolved_fullpath == resolved_working_dir or resolved_fullpath.startswith(resolved_working_dir + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(resolved_fullpath):
        return f'Error: "{directory}" is not a directory'

    entries = os.listdir(resolved_fullpath)
    lines = []
    for entry in entries:
        full_path = os.path.join(resolved_fullpath, entry)
        try:
            is_dir = os.path.isdir(full_path)
            file_size = os.path.getsize(full_path) if not is_dir else 0
            lines.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        except Exception as e:
            return (f"Error: ({e})")

    return "\n".join(lines)

