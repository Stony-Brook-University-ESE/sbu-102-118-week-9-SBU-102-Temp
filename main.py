#!/usr/bin/env python3

import os
import sys
import google.genai as genai
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip, CompositeVideoClip

def check_requirements():
    """Check if all required files and environment variables are present"""
    
    # Check for Gemini API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: Gemini API key not found!")
        print("Please set your API key as an environment variable:")
        print("export GEMINI_API_KEY='your-api-key-here'")
        print("Or create a .env file with GEMINI_API_KEY=your-api-key-here")
        return False
    
    # Check for background video
    if not os.path.exists('background.mp4'):
        print("ERROR: background.mp4 not found!")
        print("Please add a background video file named 'background.mp4' to the project directory")
        return False
    
    return True

def generate_script(topic):
    """Generate a motivational script using Google Gemini API"""
    
    print("Generating motivational script...")
    
    # Configure Gemini API with new client
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    
    prompt = f"""Write a motivational and inspiring script about {topic}. 
    The script should be:
    - 30-60 seconds long when spoken
    - Uplifting and positive
    - Easy to understand
    - Suitable for a general audience
    
    Please write only the script text, no additional formatting or instructions."""
    
    try:
        # Use the new API to generate content with the latest model
        response = client.models.generate_content(
            model='models/gemini-2.5-flash',
            contents=prompt
        )
        script = response.text.strip()
        
        # Save script to file
        with open('script.txt', 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"Script saved to 'script.txt'")
        return script
        
    except Exception as e:
        print(f"Error generating script: {e}")
        return None

def generate_voiceover(script):
    """Generate voiceover audio from script using Google Text-to-Speech (Free)"""
    
    print("Generating voiceover...")
    
    try:
        # Create TTS object with English language
        # You can change the language code: 'en' (English), 'es' (Spanish), 'fr' (French), etc.
        tts = gTTS(text=script, lang='en', slow=False)
        
        # Save audio to file
        tts.save("voiceover.mp3")
        print("Voiceover saved to 'voiceover.mp3'")
        return True
        
    except Exception as e:
        print(f"Error generating voiceover: {e}")
        return False

def create_final_video():
    """Combine background video with voiceover to create final video"""
    
    print("Creating final video...")
    
    try:
        # Load the background video
        video = VideoFileClip("background.mp4")
        
        # Load the voiceover audio
        audio = AudioFileClip("voiceover.mp3")
        
        # Get the duration of the audio
        audio_duration = audio.duration
        
        # If video is longer than audio, trim the video
        if video.duration > audio_duration:
            video = video.with_duration(audio_duration)
        # If audio is longer than video, loop the video
        elif audio_duration > video.duration:
            # Calculate how many times to loop the video
            loops_needed = int(audio_duration / video.duration) + 1
            video_clips = [video] * loops_needed
            video = CompositeVideoClip(video_clips).with_duration(audio_duration)
        
        # Set the audio of the video to our voiceover
        final_video = video.with_audio(audio)
        
        # Write the final video file
        final_video.write_videofile(
            "final_video.mp4",
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        print("Final video saved to 'final_video.mp4'")
        
        # Clean up
        video.close()
        audio.close()
        final_video.close()
        
        return True
        
    except Exception as e:
        print(f"Error creating final video: {e}")
        return False

def main():
    """Main function to run the motivational video generator"""
    
    print("=== Motivational Video Generator ===")
    print()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Get topic from user
    print("What motivational topic would you like to create a video about?")
    topic = input("Topic: ").strip()
    
    if not topic:
        print("No topic provided. Exiting.")
        sys.exit(1)
    
    print(f"\nCreating motivational video about: {topic}")
    print("-" * 50)
    
    # Step 1: Generate script
    script = generate_script(topic)
    if not script:
        print("Failed to generate script. Exiting.")
        sys.exit(1)
    
    # Step 2: Generate voiceover
    if not generate_voiceover(script):
        print("Failed to generate voiceover. Exiting.")
        sys.exit(1)
    
    # Step 3: Create final video
    if not create_final_video():
        print("Failed to create final video. Exiting.")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("SUCCESS! Your motivational video has been created.")
    print("Files created:")
    print("- script.txt (generated script)")
    print("- voiceover.mp3 (generated audio)")
    print("- final_video.mp4 (final video)")
    print("=" * 50)

if __name__ == "__main__":
    main()