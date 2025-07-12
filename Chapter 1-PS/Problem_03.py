# Install an external module and use it to perform an operation of your interest.
import pyjokes
import pyttsx3

joke = pyjokes.get_joke()
engine = pyttsx3.init()

print(joke)
engine.say(joke)
engine.runAndWait()