import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def chatbot():
    print("Hello! I'm your chatbot. You can ask me questions. If you want to exit, type 'bye'.")
    
    while True:
        user_input = input("Enter your message: ")
        
        if user_input.lower() == 'bye':
            break

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )

        print(chat_completion.choices[0].message.content)

chatbot()