# 🤖 JARVIS - AI Voice Assistant

## 📖 Description

JARVIS is an AI-powered voice assistant built with Python. It uses speech recognition to listen for the wake word "Jarvis" and responds to various commands using text-to-speech. The assistant can open websites, play music from YouTube, fetch news headlines, and process general queries using Google's Gemini AI model.

## ✨ Features

- 🎤 **Wake Word Detection**: Responds only when "Jarvis" is spoken
- 🌐 **Website Opening**: Open Google, Facebook, YouTube, and LinkedIn
- 🎵 **Music Playback**: Play songs from a predefined library via YouTube
- 📰 **News Updates**: Fetch and speak top news headlines from the US
- 🧠 **AI Processing**: Handle any other queries using Google Gemini AI
- 🔊 **Text-to-Speech**: Uses Google TTS and Pygame for audio output

## 🛠️ Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/T786-eng/Mega-project1---JARVIS-.git
   cd <repo-directory>
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   - In `01_main.py`, replace `"Enter-Your-API-Key-Here"` with your actual Google Gemini API key
   - The NewsAPI key is already included in the code

## 🚀 Usage

1. **Run the assistant**:
   ```
   python 01_main.py
   ```

2. **Interact with JARVIS**:
   - Say "Jarvis" to wake it up
   - Wait for the confirmation sound
   - Give commands such as:
     - "Open Google" - Opens Google in your browser
     - "Play skyfall" - Plays the song "Skyfall" on YouTube
     - "News" - Speaks the top news headlines
     - Any other phrase - Processed by AI for a response

## 📁 Project Structure

- `01_main.py`: Main application script containing the voice assistant logic
- `client.py`: Example script for interacting with Google Gemini API
- `musicLibrary.py`: Dictionary of song names and their YouTube links
- `test_speech.py`: Script to test wake word detection
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## 📋 Requirements

- 🐍 Python 3.8 or higher
- 🎙️ Working microphone for speech input
- 🌐 Internet connection for API calls and web browsing
- 🔊 Speakers or headphones for audio output

## 📦 Dependencies

- `speech_recognition`: For converting speech to text
- `pyttsx3`: Offline text-to-speech engine
- `requests`: For making HTTP requests to NewsAPI
- `gtts`: Google Text-to-Speech for AI responses
- `pygame`: For playing audio files
- `google-genai`: For interacting with Google Gemini AI

## 🔧 Troubleshooting

- If speech recognition fails, check your microphone settings and internet connection
- Ensure your Google Gemini API key is valid and has quota
- For audio issues, verify Pygame and your audio drivers

## 🤝 Contributing

Feel free to fork the repository and submit pull requests for improvements or new features.

## 📄 License

This project is for educational purposes. Please respect API usage limits and terms of service.