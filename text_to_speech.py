import pyttsx3 

text = "Hello, how are you doing today?"
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 'rate-70')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)
engine.runAndWait()

