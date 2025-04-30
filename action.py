import text_to_speech
import speech_to_text
import datetime 
import webbrowser
import weather

def Action():

    user_data = speech_to_text.speech_to_text()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Jarvis")
        return "My name is Jarvis"
    
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hello, what are you doing")
        return "hello, what are you doing"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning Sir, How are you?")
        return "Good Morning Sir, How are you?"
    
    elif "time now" in user_data or "time kya hua hai" in user_data:
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M")
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/?flow_ctx=d915bfb6-036d-4f23-b6b3-fea53d7c61cd%3A1742498226")
        text_to_speech.text_to_speech("Spotify is ready for you")
        return "Spotify is ready for you"
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Opening Youtube for you")
        return "Opening Youtube for you"
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Opening Google for you")
        return "Opening Google for you"
    elif "weather" in user_data:
        ans = weather.get_weather()
        text_to_speech.text_to_speech(ans)  
        return ans
    else :
        text_to_speech.text_to_speech("Sorry, I didn't understand that.")
        return "Sorry, I didn't understand that."

    