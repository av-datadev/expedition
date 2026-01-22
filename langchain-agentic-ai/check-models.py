import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- AVAILABLE MODELS ---")
try:
    # In the new SDK, we just iterate and print the name directly
    # We skip checking 'supported_generation_methods' to avoid the crash
    for m in client.models.list():
        # Only print models that look like Flash or Pro to reduce noise
        if "flash" in m.name or "pro" in m.name:
            print(m.name)
except Exception as e:
    print(f"List Error: {e}")