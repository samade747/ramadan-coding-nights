import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@function_tool("get_weather")
def get_weather(city: str) -> str:
    """
    Get the weather of a city
    """

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"

    response = requests.get(url)
    data = response.json()

    return f"The weather in {city} is {data['weather'][0]['description']}"




agent = Agent(
    name = "Multi Agent",
    instructions = "You are a greeting agent. You are to greet the user. You are a weather agent. You are to get the weather of a city.",
    model = model,
    tools = [get_weather]
)


# user_question = input("Enter your question: ")

# result = Runner.run.sync(agent, user_question)




# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  # Print provider ID for debugging
    print(f"User data: {raw_user_data}")  # Print user data for debugging

    return default_user  # Return the default user object


# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message


# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")  # Get chat history from session

    history.append(
        {"role": "user", "content": message.content}
    )  # Add user message to history

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)






# import os  # For accessing environment variables
# import chainlit as cl  # Web UI framework for chat applications
# from dotenv import load_dotenv  # For loading environment variables
# from typing import Optional, Dict  # Type hints for better code clarity
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
# from tools.function_tool import function_tool  # Adjusted import path
# import requests  # For making HTTP requests

# # Load environment variables from .env file
# load_dotenv()

# #  Get the OpenAI API key from the environment variables
# gemini_api_key = os.getenv("GEMINI_API_KEY")


# provider = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguageapi.googleapis.com/v1beta/openai",
# )

# # Configure the Language Model
# model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


# # Decorator to handle OAuth callback from GitHub
# @cl.oauth_callback
# def oauth_callback(
#     provider_id: str,  # ID of the OAuth provider (GitHub)
#     token: str,  # OAuth access token
#     raw_user_data: Dict[str, str],  # User data from GitHub
#     default_user: cl.User,  # Default user object from Chainlit
# ) -> Optional[cl.User]:  # Return User object or None
#     """
#     Handle the OAuth callback from GitHub
#     Return the user object if authentication is successful, None otherwise
#     """

#     print(f"Provider: {provider_id}")  # Print provider ID for debugging
#     print(f"User data: {raw_user_data}")  # Print user data for debugging

#     return default_user  # Return the default user object


# # Handler for when a new chat session starts
# @cl.on_chat_start
# async def handle_chat_start():

#     cl.user_session.set("history", [])  # Initialize empty chat history

#     await cl.Message(
#         content="Hello! How can I help you today?"
#     ).send()  # Send welcome message


# @function_tool("get_weather")
# def get_weather(city: str) -> str:
#     """
#     Get the weather of a city
#     """

#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"

#     response = requests.get(url)
#     data = response.json()

#     return f"The weather in {city} is {data['weather'][0]['description']}"




# agent = Agent(
#     name = "Multi Agent",
#     instructions = "You are a greeting agent. You are to greet the user. You are a weather agent. You are to get the weather of a city.",
#     model = model,
#     tools = [get_weather]
# )

# user_question = input("Enter your question: ")

# result = Runner.run.sync(agent, user_question)


# # Handler for incoming chat messages
# @cl.on_message
# async def handle_message(message: cl.Message):

#     history = cl.user_session.get("history")  # Get chat history from session

#     history.append(
#         {"role": "user", "content": message.content}
#     )  # Add user message to history

#     result = await cl.make_async(Runner.run_sync)(agent, input=history)

#     response_text = result.final_output
#     await cl.Message(content=response_text).send()

#     history.append({"role": "assistant", "content": response_text})
#     cl.user_session.set("history", history)