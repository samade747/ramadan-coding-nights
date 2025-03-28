import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",

)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


agent = Agent(
    name = "Greeting Agent",
    instructuion = "You are a greeting agent. You will greet the user with a greeting message.",
    model=model,
)

agent1 = Agent(
    name = "Teacher Agent",
    instructuion = "You are a greeting agent. You will greet the user with a greeting message.",
    model=model,
)

agent2 = Agent(
    name = "History Agent",
    instructuion = "You are a greeting agent. You will greet the user with a greeting message.",
    model=model,
)

agent3 = Agent(
    name = "Doctor Agent",
    instructuion = "You are a greeting agent. You will greet the user with a greeting message.",
    model=model,
)

agent4 = Agent(
    name = "Food Agent",
    instructuion = "You are a greeting agent. You will greet the user with a greeting message.",
    model=model,
)

# Get user input from the terminal
user_question = input("Please enter your question: ")


result = Runner.run_sync(agent, user_question)
print(result.final_output)