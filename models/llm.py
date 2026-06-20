from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

# Load API key
api_key = os.getenv("GROQ_API_KEY")

# Debug logs (visible in Render logs)
print("GROQ KEY FOUND:", api_key is not None)

if api_key:
    print("KEY PREFIX:", api_key[:4] + "...")
else:
    print("ERROR: GROQ_API_KEY missing!")

# Create LLM safely
try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        api_key=api_key
    )
    print("Groq LLM initialized successfully")

except Exception as e:
    print(f"Groq initialization failed: {str(e)}")
    llm = None