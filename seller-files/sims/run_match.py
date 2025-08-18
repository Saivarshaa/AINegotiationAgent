import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def run_match(buyer_message: str):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("❌ GROQ_API_KEY not found. Please set it in your .env file.")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Updated to a supported model
        messages=[
            {"role": "system", "content": "You are a real estate seller agent. Answer briefly and persuasively."},
            {"role": "user", "content": buyer_message}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    buyer_message = "I’m looking for a 2BHK apartment near the city center."
    reply = run_match(buyer_message)
    print("Buyer:", buyer_message)
    print("Seller:", reply)

