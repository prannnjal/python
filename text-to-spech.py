import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List all available voices
voices = engine.getProperty('voices')
print("Available Voices:\n")
for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.name} ({voice.id}) - Lang: {voice.languages}")

# Choose a voice
voice_index = int(input("\nEnter the voice index you want to use: "))
engine.setProperty('voice', voices[voice_index].id)

# Set speaking rate
rate = engine.getProperty('rate')
print(f"\nCurrent speaking rate: {rate}")
new_rate = input("Enter new speaking rate (leave blank to keep default): ")
if new_rate.strip():
    engine.setProperty('rate', int(new_rate))

# Set volume
volume = engine.getProperty('volume')
print(f"Current volume: {volume} (0.0 to 1.0)")
new_volume = input("Enter new volume (leave blank to keep default): ")
if new_volume.strip():
    engine.setProperty('volume', float(new_volume))

# Enter text to speak
text = input("\nEnter the text to speak: ")
engine.say(text)
engine.runAndWait()

# Save to file
save_choice = input("Do you want to save this as an MP3? (y/n): ")
if save_choice.lower() == "y":
    filename = input("Enter filename (e.g., output.mp3): ")
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Saved as {filename}")

print("\nDone!")
