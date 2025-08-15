import os

def get_file_content(working_directory, file_path):
    MAX_FILE_LENGTH = 10000
    try:
        full_path = os.path.join(working_directory, file_path)
        resolved_full_path = os.path.abspath(full_path)
        resolved_working_dir = os.path.abspath(working_directory)

        # Check if file_path is inside working_directory
        if not (resolved_full_path == resolved_working_dir or resolved_full_path.startswith(resolved_working_dir + os.sep)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if it is a file
        if not os.path.isfile(resolved_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file content
        with open(resolved_full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Truncate if longer than MAX_FILE_LENGTH
        if len(content) > MAX_FILE_LENGTH:
            truncated_msg = f' [...File "{file_path}" truncated at {MAX_FILE_LENGTH} characters]'
            return content[:MAX_FILE_LENGTH] + truncated_msg

        return content

    except Exception as e:
        return f"Error: {str(e)}"
