import os, sys, textwrap
from dotenv import load_dotenv
from google import genai
from google.genai import types

PRINT_WIDTH = 80

def main():
    args = sys.argv[1:]
    if not args:
        print('Usage:\n\tpython main.py "your prompt here"')
        print('Example:\n\tpython main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = args[0]
    is_verbose = False
    if len(args) == 2:
        if args[1] == "--verbose":
            is_verbose = True

    # list of `types.Content` to keep track of the whole conversation
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    print_intro()

    # load gemini api key from `.env` using `dotenv` library
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    # create a new instance of gemini client using the api key
    client = genai.Client(api_key=api_key)
    # get a response from gemini using messages list to track the whole conversation
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )

    # print user prompt, prompt tokents and response tokens
    if is_verbose:
        print("\nUser prompt: \n")
        print(textwrap.fill(user_prompt, width=PRINT_WIDTH))
        print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}") 
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # print response
    print("\nResponse: \n")
    print(textwrap.fill(response.text, width=PRINT_WIDTH))

    print_outro()
    
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