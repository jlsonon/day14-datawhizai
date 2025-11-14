import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AIEngine:
    def __init__(self, model="llama-3.1-8b-instant"):
        self.model = model
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    def ask(self, prompt):
        try:
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                return "⚠️ Error: GROQ_API_KEY not found. Please set it in your .env file. Get your API key from https://console.groq.com/"
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error: {str(e)}\n\n💡 Tip: Make sure your GROQ_API_KEY is set correctly in the .env file."