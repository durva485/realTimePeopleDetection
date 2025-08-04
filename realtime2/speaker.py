import pyttsx3
import threading

engine = pyttsx3.init()

def speak_async(text):
    def run():
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=run)
    thread.start()
