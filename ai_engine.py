import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(query, context):
    prompt = f"""
    Answer the question based on the context.

    Context:
    {context}

    Question:
    {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]