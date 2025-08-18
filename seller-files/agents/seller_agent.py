from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Try to initialize client
api_key = os.getenv("OPENAI_API_KEY")
client = None
if api_key and api_key.startswith("sk-") and len(api_key) > 40:
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print("⚠️ Could not initialize OpenAI client:", e)
else:
    print("⚠️ No valid API key found, using dummy mode.")

class SellerAgent:
    def __init__(self):
        self.fallback_responses = [
            "I can offer you the best deal possible.",
            "This product is in high demand, so my price is fair.",
            "I might give a small discount, but not too much.",
            "If you buy now, I can reduce the price slightly."
        ]
        self.response_index = 0

    def respond(self, message: str):
        # If API client is available, try API call
        if client:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a seller agent negotiating price."},
                        {"role": "user", "content": message},
                    ],
                )
                return response.choices[0].message.content
            except Exception as e:
                print("⚠️ API request failed, switching to dummy mode:", e)

        # Fallback response
        reply = self.fallback_responses[self.response_index % len(self.fallback_responses)]
        self.response_index += 1
        return reply

