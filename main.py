import os, sys
from dotenv import load_dotenv
from google import genai

def main():
    if len(sys.argv) != 2:
        print("Too many / few arguments passed")
        sys.exit(1)

    # load gemini api key from `.env` using `dotenv` library
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # create a new instance of Gemini client using the api key
    client = genai.Client(api_key=api_key)

    #  get a response from Gemini
    model = "gemini-2.0-flash-001"
    contents = sys.argv[1]
    response = client.models.generate_content(
        model=model, contents=contents
    )

    # print response + prompt and response tokens
    print(f"""{response.text}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}""")

if __name__ == "__main__":
    main()