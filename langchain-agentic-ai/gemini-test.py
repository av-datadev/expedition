import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

try:
    print("Sending request to Google Gemini...")
    response = llm.invoke("Hi, are you working?")
    print("Response received:")
    print(response.content)
except Exception as e:
    print(f"FAILED: {e}")