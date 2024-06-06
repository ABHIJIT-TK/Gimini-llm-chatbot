from dotenv import load_dotenv
load_dotenv() 

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro") 

chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        break
    
    response = chat.send_message(user_input, stream=True)
    print("Bot:", response[0].text)
