"""
AI-Based Chatbot for Car Dealerships (LLM + NLP Prototype)
Powered by: OpenAI GPT-3.5 Turbo
"""

import openai
import os
from dotenv import load_dotenv

# Load environment variable from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Static inventory data 
inventory = """
Available Cars:
1. Tesla Model 3 (Electric, 2024) - €38,000
2. BMW X5 (Diesel, 2023) - €52,000
3. Toyota Corolla (Petrol, 2022) - €22,500

Financing Options:
- 3.9% APR for 36 months (good credit required)
- 10% down payment minimum
- Leasing available for select models
"""

# Summarized customer reviews for NLP context
car_reviews = {
    "Tesla Model 3": "Customers praise its performance and futuristic features like Autopilot. Some mention cabin noise and build inconsistencies.",
    "BMW X5": "Highly rated for luxury and power. Some users report expensive maintenance.",
    "Toyota Corolla": "Known for reliability and efficiency. Some feel the design is too simple."
}

# Generate a prompt combining inventory, reviews, and user query
def generate_prompt(user_input):
    selected_model = None
    for model in car_reviews:
        if model.lower() in user_input.lower():
            selected_model = model
            break

    review_info = car_reviews.get(selected_model, "No customer reviews found for this model.")
    prompt = f"""
You are a helpful, professional AI assistant working at a car dealership.

ONLY use the following dealership data to answer questions. Do not invent cars, prices, or reviews.

Inventory:
{inventory}

Customer Review Summary for {selected_model if selected_model else "N/A"}:
{review_info}

User: {user_input}
Assistant:"""
    return prompt

# Chat loop (NLP-based interaction with GPT)
def run_chatbot():
    print("Welcome to the AI Car Dealership Assistant (LLM + NLP)")
    print("Ask about pricing, financing, or what people think of a model. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for visiting. Goodbye!")
            break

        prompt = generate_prompt(user_input)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=300
            )
            reply = response['choices'][0]['message']['content']
            print(f"Bot: {reply}\n")

        except Exception as e:
            print(f"Bot: Sorry, there was an error: {e}\n")

if __name__ == "__main__":
    run_chatbot()
