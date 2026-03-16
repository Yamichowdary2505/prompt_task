from google import genai
from dotenv import load_dotenv
import os
from embeddings import get_relevant_context

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat = client.chats.create(model="gemini-2.5-flash")

print("Advanced Chatbot with Embeddings")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Ask question to Chatbot: ")
    if user_input.lower() == "exit":
        break

    context = get_relevant_context(client, user_input)

    prompt = f"""
    Use the following context to answer the question.
    If the answer is not in the context, answer from your own knowledge.

    Context:
    {context}

    Question:
    {user_input}
    """

    response = chat.send_message(prompt)
    print("ChatBot: ", response.text)