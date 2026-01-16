
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import google.genai as genai


#Pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3 .init()
newsapi = "f97d71eaa7ef4f298c0e8f2f58d78067"

def speak (text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    try:
        client = genai.Client(api_key="Enter-Your-API-Key-Here")
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=command,
        )
        reply = response.text
        print("Jarvis:", reply)
        speak_gtts(reply)
        return reply
    except Exception as e:
        print("AI Error:", e)
        speak_gtts("Sorry, I could not process that.")
        return None


def speak_gtts(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processcommand(c):
   if "open google" in c.lower():
      webbrowser.open("http://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("http://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("http://youtube.com")
   elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")

   elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
   elif "news" in c.lower():
       r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

       if r.status_code == 200:
         #parse the json response
         data = r.json()

         #Extract the articles
         articles = data.get('articles' , [])

         #print the headlines
         for article in articles:
            speak_gtts(article['title'])
   
   else:
      aiprocess(c)



if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
    #Listen to the wake word 'Jarvis'
    #obtain audio from the microphone
      r = sr.Recognizer()

      print("recognize....")
      try:
        with sr.Microphone()as source:
         print("Listening.....")
         audio = r.listen(source , timeout=2 , phrase_time_limit=1)
        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
              speak_gtts("Ya")
              #Listen for command
              try:
                  with sr.Microphone()as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Recognized command: {command}")
                    processcommand(command)
              except Exception as e:
                  print(f"Command recognition error: {e}")

      except Exception as e:
         print ("Error; {0}".format(e))




