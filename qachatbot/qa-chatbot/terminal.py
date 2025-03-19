import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Load the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Get input from the user
user_input = input("Enter your prompt: ")

# Generate content
response = model.generate_content(user_input)

# Print the response
print("\nAI Response:\n", response.text)


# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
                
# model = genai.GenerativeModel(model_name= "gemini-2.0-flash") # Load the model 

# response = model.generate_content("Hello, how are you?") # Generate content

# print(response.text) # Print the response


