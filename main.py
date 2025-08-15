import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info,schema_get_files_info
import json


def main():
    #print("Hello from bootdevai!")
    if len(sys.argv) < 2:
        print("Usage: python script.py 'Your prompt here'")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = False
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model_name = "gemini-2.0-flash-001"

    if len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            verbose = True

    messages = [ 
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
    )

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    working_directory = os.path.abspath("calculator")
    
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            args = function_call_part.args
            directory = args.get("directory", ".")
            # Call your actual function
            result = get_files_info(working_directory, directory)
            print(result)
    else:
        print(response.text)
    

    if verbose:
        print("User prompt: " + user_prompt)
        print("Prompt tokens: "+ str(response.usage_metadata.prompt_token_count))
        print("Response tokens: "+ str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()






