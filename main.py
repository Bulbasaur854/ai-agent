import os, sys, textwrap
from dotenv import load_dotenv
from google import genai

def main():
    args = sys.argv[1:]
    if not args:
        print('Usage:\n\tpython main.py "your prompt here"')
        print('Example:\n\tpython main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    print_intro()

    # load gemini api key from `.env` using `dotenv` library
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # create a new instance of Gemini client using the api key
    client = genai.Client(api_key=api_key)

    #  get a response from Gemini using user input
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=user_prompt
    )

    # print response + prompt and response tokens
    print(textwrap.fill(response.text, width=60))
    print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    
    print_outro()
    
def print_intro():    
    print("\n" + "=" * 60)
    print("AI Code Assistant".center(60))
    print("=" * 60 + "\n")

def print_outro():    
    print("\n" + "-" * 60)
    print("Closing program. Thanks for using the AI assistant!".center(60))
    print("-" * 60 + "\n")

if __name__ == "__main__":
    main()