import json
import os  # <- This was missing
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import google.generativeai as genai
from order_saver import save_order

# Set your Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_response(user_input, order_state):
    if "history" not in order_state:
        order_state["history"] = []

    with open("menu.json", "r") as f:
        menu = json.load(f)

    prompt = f"""
You are a helpful pizza ordering assistant. Ask the user about:
- Pizza types from the menu
- Optional toppings and extras
- Dietary preferences (e.g., vegan, halal)
- Delivery address
Then confirm the order and prepare it in structured JSON.

Menu: {json.dumps(menu, indent=2)}
Conversation so far:
{chr(10).join(order_state['history'])}
User: {user_input}
Bot:"""

    response = model.generate_content(prompt)
    answer = response.text.strip()

    order_state["history"] += [f"User: {user_input}", f"Bot: {answer}"]

    if "order" in answer.lower():
        save_order(answer)

    return answer, order_state
