import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os
from dialog_agent import get_ai_response

# Load Gemini API key from .env
load_dotenv()
order_state = {}

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"API error: {e}"

while True:
    try:
        user_input = listen()
        if user_input:
            response, order_state = get_ai_response(
                user_input,
                order_state
            )
            speak(response)
        else:
            speak("Sorry, I didn't catch that.")
    except KeyboardInterrupt:
        print("Exiting...")
        break