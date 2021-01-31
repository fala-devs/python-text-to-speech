#https://pypi.org/project/pyttsx3/
#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 0.5)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#engine.save_to_file('Fala Devs, beleza?', 'arquivo.mp3')

engine.say('Fala Devs, beleza?')
engine.runAndWait()