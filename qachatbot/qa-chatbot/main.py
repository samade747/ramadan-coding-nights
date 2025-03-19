import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

gemini_api_key = os.environ["GEMINI_API_KEY"]

# Configure the API key
genai.configure(api_key=gemini_api_key)

# Load the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Get input from the user
@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! How can I assist you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = model.generate_content(user_input)
    response_text = response.text if response else "I'm sorry, I don't understand that."
    await cl.Message(content=response_text).send()