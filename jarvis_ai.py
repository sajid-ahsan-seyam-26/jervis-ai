import webbrowser
import pyttsx3

# ----------------- Setup -----------------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ----------------- Main Jarvis -----------------
speak("Hello! I am Jarvis. What YouTube video should I search?")
query = input("Type the video name: ")  # <-- text input instead of voice

if query:
    speak(f"Searching YouTube for {query}")
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(search_url)
else:
    speak("No search query provided.")
