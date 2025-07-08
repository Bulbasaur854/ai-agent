import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import PRINT_WIDTH
from prompts import system_prompt
from call_function import call_function, available_functions

def main():
    load_dotenv()
    # print_intro() 

    # handle user input via command line arguments
    args = sys.argv[1:]
    if not args:
        print('\nUsage:\n\tpython main.py "your prompt here" [--verbose]')
        print('Example:\n\tpython main.py "How do I build a calculator app?"')
        print_outro()
        sys.exit(1)
    user_prompt = args[0]
    is_verbose = "--verbose" in sys.argv    

    # load gemini api key from `.env` using `dotenv` library
    api_key = os.environ.get("GEMINI_API_KEY")
    # create a new instance of gemini client using the api key
    client = genai.Client(api_key=api_key)   
    
    # print user prompt
    if is_verbose:
        print("\nUser prompt: \n")
        print(user_prompt)

    # list of `types.Content` to keep track of the whole conversation
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = generate_content(client, messages, is_verbose)

    # print prompt tokents and response tokens
    if is_verbose:
        print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}") 
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    print("\nResponse: \n")
    if response.function_calls:
        # print the calls to the functions
        for call in response.function_calls:
            result = call_function(call, is_verbose)
            if not result.parts[0].function_response.response:
                raise Exception("Error! 'call_function' got no response!")
            if is_verbose:
                print(f"--->\n{result.parts[0].function_response.response["result"]}")
    else:
        # print response
        print(response.text)

    # print_outro()

def generate_content(client, messages, is_verbose):
    # get a response from gemini using messages list to track the whole conversation
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    return response
    
def print_intro():    
    print("\n" + "=" * PRINT_WIDTH)
    print("AI Code Assistant".center(PRINT_WIDTH))
    print("=" * PRINT_WIDTH)

def print_outro():    
    print("\n" + "-" * PRINT_WIDTH)
    print("Closing program. Thanks for using the AI assistant!".center(PRINT_WIDTH))
    print("-" * PRINT_WIDTH + "\n")

if __name__ == "__main__":
    main()