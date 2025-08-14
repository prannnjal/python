import time
import os
import google.generativeai as genai

# Set your API key
API_KEY = "AIzaSyCrYgbhj_FXhWURAOfCP0P9aXuU_OmauNc"

def list_available_models():
    """List available models to see what's accessible."""
    try:
        genai.configure(api_key=API_KEY)
        models = genai.list_models()
        print("Available models:")
        for model in models:
            print(f"- {model.name}")
        return models
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def generate_content(prompt, output_filename="generated_content.txt"):
    """
    Generate content using Google's Generative AI.
    
    Args:
        prompt (str): The text prompt describing the content to generate
        output_filename (str): Name of the output file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Configure the API
        genai.configure(api_key=API_KEY)
        
        print("Starting content generation...")
        print(f"Prompt: {prompt}")
        
        # Try different models
        models_to_try = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-pro']
        
        for model_name in models_to_try:
            try:
                print(f"Trying model: {model_name}")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(f"Create a story based on: {prompt}")
                
                print("Generated content:")
                print(response.text)
                
                # Save the response to a text file
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                
                print(f"Content saved to {output_filename}")
                return True
                
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                continue
        
        print("All models failed. Please check your API key and permissions.")
        return False
            
    except Exception as e:
        print(f"Error during generation: {e}")
        return False

def main():
    """Main function to run the generation."""
    
    print("=== Google Generative AI Content Generator ===")
    print("Note: Video generation with Veo model requires specific API access.")
    print("This script will generate text content based on your prompt instead.")
    print()
    
    # Your prompt for the content
    prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.

A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""
    
    # First, let's see what models are available
    print("Checking available models...")
    available_models = list_available_models()
    print()
    
    # Generate content
    success = generate_content(prompt, "dialogue_story.txt")
    
    if success:
        print("Generation completed successfully!")
    else:
        print("Generation failed. Please check your API key and permissions.")

if __name__ == "__main__":
    main()
