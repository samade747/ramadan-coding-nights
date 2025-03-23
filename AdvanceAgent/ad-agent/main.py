import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel


# Load environment variables from .env file
load_dotenv()

#  Get the OpenAI API key from the environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguageapi.googleapis.com/v1beta/openai",
)

# Configure the Language Model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@cl.oauth_callback
def oauth_callback(
    provider_id: str, 
    token: str, 
    raw_user_data: Dict[str, str], 
    default_user: cl.User
) -> Optional[cl.User]:
    """
    handle the oauth callback from github 
    Return the user object if auth is successful, non otherwise
    """






agent = Agent(
    name = "Greeting Agent",
    instructions = "You are a greeting agent. You are to greet the user.",
    model = model,
)

user_question = input("Enter your question: ")

result = Runner.run.sync(agent, user_question)


