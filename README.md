## AI-Based Chatbot for Car Dealerships (LLM + NLP Prototype)

This is a prototype AI chatbot that simulates a smart assistant in a car dealership using **Large Language Models (LLMs)** and **Natural Language Processing (NLP)** techniques. It is built with Python and OpenAI’s GPT-3.5-turbo API.

---
## Objectives
To develop a functional, AI-based chatbot using Large Language Models (LLMs) that simulates a car dealership assistant.

To apply NLP concepts and prompt engineering for user-friendly interaction.

To showcase how LLMs can be adapted for training, information support, or customer guidance.

---
## Project Overview

The chatbot interacts with users in natural language and answers questions about:
- Available car models
- Pricing and fuel types
- Financing options
- Summarized customer reviews

The assistant is **prompt-engineered** to answer only using predefined car inventory and review data — ensuring **factual grounding** and **relevant NLP-style conversation**.

---

## Key Features

| Feature                 | Description                                                   |
|-------------------------|---------------------------------------------------------------|
| GPT-3.5 Integration   | Uses OpenAI API for context-aware response generation          |
| Prompt Engineering    | Custom prompt constrains the assistant to factual dealership data |
| NLP-Like Responses     | Handles pricing, reviews, financing, and intent automatically |
| Customer Reviews      | Pulls summary text from a structured Python dictionary        |
| Secure API Key        | Uses `.env` for OpenAI key management                        |
| CLI Interface         | Command-line conversation loop for demo or testing            |

---
## Methodology
Define Scope:

- Limit responses to only three car models and their reviews.

- Keep logic grounded to avoid hallucinated responses.

- Design Prompt Template:

- Combine inventory + user question + review into a prompt sent to the LLM.

- Use instruction-style system messages to control AI tone and limits.

- Integrate GPT-3.5:

- Use OpenAI API for NLP response generation.

- Secure the API key using .env and python-dotenv.

- Simulate NLP Flow:

- Parse user input.

- Inject into dynamic prompt.

- Get response and display it in the terminal.


## Sample Conversation
You: What cars are available?
Bot: We currently offer:

Tesla Model 3 (Electric, 2024) - €38,000

BMW X5 (Diesel, 2023) - €52,000

Toyota Corolla (Petrol, 2022) - €22,500


---

## How It Works

1. User enters a question in the terminal (e.g., “How much is the BMW X5?”)
2. The system generates a custom prompt including:
   - Static car inventory
   - Relevant customer reviews
   - User question
3. This prompt is sent to the OpenAI GPT-3.5 API using `ChatCompletion`
4. The AI returns a natural, context-aware answer based only on the embedded knowledge

---

## Applications
🛠️ Training Assistant Prototype — Could support Siemens Energy by summarizing documents or answering FAQs for internal training.

🧾 Customer Support Bot — Helps users decide between product options or plans.

📚 E-learning Use Case — Explain topics, translate complex terms, or simulate learner conversations.

📈 Portfolio AI Project — Demonstrates LLM usage, Python backend, and user interaction design.

---

## Limitations
Currently supports only 3 car models (static data).

No database integration or memory — cannot learn from past inputs.

Needs internet and OpenAI API key to work.

Not fully optimized for multilingual or domain-specific accuracy.

