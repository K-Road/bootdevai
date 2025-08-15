import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    #print("Hello from bootdevai!")
    if len(sys.argv) < 2:
        print("Usage: python script.py 'Your prompt here'")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = False

    if len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            verbose = True

    messages = [ 
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    print(response.text)

    if verbose:
        print("User prompt: " + user_prompt)
        print("Prompt tokens: "+ str(response.usage_metadata.prompt_token_count))
        print("Response tokens: "+ str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()






