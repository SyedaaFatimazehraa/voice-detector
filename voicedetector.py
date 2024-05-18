import speech_recognition as sr
import pyttsx3

# Initialize Speech Recognition
recognizer = sr.Recognizer()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen()
        if "hello" in command or "hi" in command or "hey" in command:
            speak("Hello! How can I assist you?")
        elif "how are you" in command:
            speak("I'm fine, thank you!")
        elif "what's your name" in command:
            speak("I am your voice assistant!")
        elif "what can you do" in command:
            speak("I can answer your questions, tell you the time, and much more!")
        elif "tell me which library you have used" in command:
            speak("speech recognition! ")
        elif "bye" in command:
            speak("Goodbye have a nice day!")
            break
        else:
            speak("Sorry, I didn't understand that command.")
