# Speech-to-Image-Generator_Model

**🗣️ AI-Powered Speech-to-Image Generator**
This project records speech, transcribes it into text using OpenAI Whisper, and generates an image based on the transcribed text using OpenAI DALL-E 3.

**📂 Project Structure**

📦 AI-Speech-to-Image
├── app.py                         # Core Python script for audio processing and image generation
├── Assignment_2.1_walkthrough.py   # Streamlit app to interact with the system
├── requirements.txt                # Python dependencies
├── recorded_audio.wav              # Sample recorded audio file
├── modified_image.png              # AI-generated image output
├── Week2_2.1_App.pdf               # PDF walkthrough of the project
├── Gen_AI_Assignment_2.1.ipynb     # Jupyter Notebook version of the project
└── README.md                       # Documentation


**🚀 Features**
✅ Speech-to-Text with OpenAI Whisper – Converts audio into text.
✅ Text-to-Image with DALL-E 3 – Generates images from transcribed text.
✅ Real-Time Audio Recording – Captures user speech directly.
✅ Streamlit Web Interface – User-friendly UI to interact with the system.
✅ Downloadable AI-Generated Images – Save and use generated images.

**📂 File Descriptions**
**1️⃣ app.py (Main Program)**
**📌 Purpose:**
Records audio, transcribes it using OpenAI Whisper, and then generates an image using DALL-E 3.
📌 Key Functionalities: ✅ Records user audio for 15 seconds.
✅ Transcribes speech using OpenAI Whisper.
✅ Generates an image based on transcription.
✅ Displays & saves the generated image.
✅ Allows audio playback.

**2️⃣ Assignment_2.1_walkthrough.py (Streamlit Web App)**
**📌 Purpose:**

Provides a Graphical User Interface (GUI) for users to upload audio, transcribe speech, and generate images interactively.
📌 Key Functionalities: ✅ Accepts user-uploaded audio files.
✅ Transcribes audio using Whisper API.
✅ Uses transcription to generate an AI image.
✅ Displays the generated image within the Streamlit app.

**3️⃣ Gen_AI_Assignment_2.1.ipynb (Jupyter Notebook)**
**📌 Purpose:**

Step-by-step walkthrough of the project implementation in Jupyter Notebook.
📌 Key Functionalities: ✅ Allows testing of individual functions interactively.
✅ Visualizes generated images in a notebook environment.
✅ Records and plays back audio within Jupyter.

**4️⃣ requirements.txt (Dependencies)**
**📌Purpose:**

Contains all required Python libraries.

**🛠 Installation & Setup**
1️⃣ Clone the Repository
git clone https://github.com/Bealux007/AI-Speech-to-Image.git
cd AI-Speech-to-Image
**2️⃣ Create a Virtual Environment**
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
**3️⃣ Install Dependencies**
pip install -r requirements.txt
**4️⃣ Set Up API Keys**
OPENAI_API_KEY=your-api-key-here

**🚀 Running the Application**
1️⃣ Run the Streamlit Web App
streamlit run Assignment_2.1_walkthrough.py

Open the Streamlit web interface.
Upload an audio file and generate an image.

2️⃣ Run the Core Python Script
python app.py

Records speech, transcribes it, and generates an AI image.

**📜 License**
MIT License. Free to use and modify!

**🔗 Contribute**
Pull requests are welcome! If you find a bug, open an issue.
