import time
import os
import google.generativeai as genai

# Set your API key
API_KEY = "AIzaSyCrYgbhj_FXhWURAOfCP0P9aXuU_OmauNc"

def generate_veo_video(prompt, output_filename="generated_video.mp4"):
    """
    Generate a video using Google's Veo model.
    
    Args:
        prompt (str): The text prompt describing the video to generate
        output_filename (str): Name of the output video file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Configure the API
        genai.configure(api_key=API_KEY)
        
        print("Starting Veo video generation...")
        print(f"Prompt: {prompt}")
        
        # Use the Veo model for video generation
        model = genai.GenerativeModel('veo-3.0-generate-preview')
        
        # Generate the video
        print("Generating video (this may take several minutes)...")
        response = model.generate_content(prompt)
        
        # Check if we got a video response
        if hasattr(response, 'video') and response.video:
            # Save the video
            with open(output_filename, 'wb') as f:
                f.write(response.video)
            print(f"Video saved to {output_filename}")
            return True
        else:
            print("No video was generated in the response.")
            print("Response type:", type(response))
            print("Response content:", response)
            return False
            
    except Exception as e:
        print(f"Error during video generation: {e}")
        return False

def main():
    """Main function to run the video generation."""
    
    print("=== Google Veo Video Generator ===")
    print("Using Veo 3.0 model for video generation")
    print()
    
    # Your prompt for the video
    prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.

A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""
    
    # Generate the video
    success = generate_veo_video(prompt, "dialogue_video.mp4")
    
    if success:
        print("Video generation completed successfully!")
    else:
        print("Video generation failed. Please check your API key and Veo model access.")

if __name__ == "__main__":
    main()
