# Import the necessary libraries
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from a .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Define the configuration for the model
model_config = {
    "temperature": 0.3, # Adjusts the randomness of the output
    "top_p": 0.99, # Controls the diversity of the output
    "top_k": 0, # Controls the number of top tokens to consider
    "max_output_tokens": 400 # Maximum number of tokens in the output
}

# Generates a blog paragraph based on the provided topic.
def generate_blog(paragraph_topic):

    # Create a GenerativeModel instance with the specified configuration
    model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=model_config)

    # Generate content based on the provided prompt
    response = model.generate_content(f"Write a paragraph about the following topic. {paragraph_topic}")

    # Retrieve the generated text
    retrieve_blog = response.text

    # Return the generated paragraph
    return retrieve_blog


# Interactive loop to continuously prompt the user for topics
keep_writing = True

while keep_writing:
    # Prompt the user to decide whether to write a paragraph or stop
    answer = input('Write a paragraph? Y for yes, anything else for no. ')
    
    if answer.upper() == 'Y':
        # If yes, prompt for the topic and generate the paragraph
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        # If not, set the flag to stop the loop
        keep_writing = False

# Thank the user for using the blog generator
print("Thank you for using the 🤖 AI Blog Generator!")