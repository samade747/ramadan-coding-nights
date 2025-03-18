import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

genai.configure(api_key=os.getenv["GOOGLE_API_KEY"])
                
model = genai.GeneratorExit(model_name= "gemini-20,") # Load the model 

response = model.generate_content_async("Hello, how are you?") # Generate content

print(response.text) # Print the response


print(response.text) # Print the response