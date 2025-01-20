import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)