import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        resolved_full_path = os.path.abspath(full_path)
        resolved_working_dir = os.path.abspath(working_directory)

        # Check if file is inside working directory
        if not (
            resolved_full_path == resolved_working_dir
            or resolved_full_path.startswith(resolved_working_dir + os.sep)
        ):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Make sure directory exists
        os.makedirs(os.path.dirname(resolved_full_path), exist_ok=True)

        # Write content to file (overwrite)
        with open(resolved_full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
