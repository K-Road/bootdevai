import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        resolved_full_path = os.path.abspath(full_path)
        resolved_working_dir = os.path.abspath(working_directory)

        if not (
            resolved_full_path == resolved_working_dir
            or resolved_full_path.startswith(resolved_working_dir + os.sep)
        ):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(resolved_full_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed = subprocess.run(
            ["python", file_path] + args,
            cwd=working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )

        output = ""
        if completed.stdout:
            output += f"STDOUT:\n{completed.stdout}"
        if completed.stderr:
            output += f"\nSTDERR:\n{completed.stderr}"
        if completed.returncode != 0:
            output += f"\nProcess exited with code {completed.returncode}"
        if not completed.stdout and not completed.stderr:
            return "No output produced."

        return output.strip()

    except Exception as e:
        return f"Error: executing Python file: {e}"
