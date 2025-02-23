import os
import openai
import speech_recognition as sr
import wave
import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
from IPython.display import display, Audio, Image as IPImage

# Load OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your actual key

# Function to Record Real-Time Audio
def record_audio(filename="recorded_audio.wav", duration=15, sample_rate=44100):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("🎙 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=duration)

    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    
    return filename

# Function to Transcribe Audio Using OpenAI Whisper
def transcribe_audio(audio_file):
    with open(audio_file, "rb") as audio:
        response = openai.Audio.transcribe(model="whisper-1", file=audio)
    return response["text"]

# Function to Generate AI Image Using DALL-E 3
def generate_image(prompt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response["data"][0]["url"]
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))
    return img

# Record Audio
audio_path = record_audio(duration=15)
print("✅ Recording Completed")

# Transcribe Audio
transcription = transcribe_audio(audio_path)
print(f"📝 **Transcription:** {transcription}")

# Generate AI-modified Image
modified_image = generate_image(transcription)

# Display Original and Modified Images
uploaded_image = Image.open("path_to_your_uploaded_image.jpg")  # Replace with the path to your uploaded image
display(IPImage(filename="path_to_your_uploaded_image.jpg", width=400, caption="📸 Original Image"))  # Replace with the path to your uploaded image
display(modified_image)

# Provide Download Option
modified_image.save("modified_image.png")
print("📥 AI-Generated Image saved as 'modified_image.png'.")

# Embed Audio
display(Audio(filename=audio_path))