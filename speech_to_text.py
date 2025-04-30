import speech_recognition as sr

# Initialize the recognizer
def speech_to_text():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and listen
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            voice_data = recognizer.recognize_google(audio)
            print("You said:", voice_data)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
