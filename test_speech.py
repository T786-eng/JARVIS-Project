import speech_recognition as sr

r = sr.Recognizer()

print("Testing wake word 'jarvis'...")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for 'jarvis'...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(f"Recognized: {word}")
            if word.lower() == "jarvis":
                print("Wake word detected!")
                break
    except sr.WaitTimeoutError:
        print("Timeout: No speech detected. Trying again...")
    except sr.UnknownValueError:
        print("Could not understand audio. Trying again...")
    except sr.RequestError as e:
        print(f"Request error: {e}")
        break
    except Exception as e:
        print(f"Error: {e}")
        break
