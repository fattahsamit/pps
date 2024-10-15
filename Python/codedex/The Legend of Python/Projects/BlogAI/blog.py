import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

model_config = {
    "temperature": 0.3,
    "top_p": 0.99,
    "top_k": 0,
    "max_output_tokens": 400,
}

def generate_blog(paragraph_topic):
    # Create a GenerativeModel instance
    model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=model_config)

    # Generate content based on a prompt
    response = model.generate_content(f"Write a paragraph about the following topic. {paragraph_topic}")

    # Retrieve the generated text
    retrieve_blog = response.text

    return retrieve_blog


# Example usage
blog_paragraph = generate_blog("Why NYC is better than your Dhaka city.")
print(blog_paragraph)