import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    # Adjust for ambient noise and listen
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    