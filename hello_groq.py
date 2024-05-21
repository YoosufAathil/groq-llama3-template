import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can LLMs enhance the functionality of a Java-based backend system",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)