from voiceRec import *
from func import *

print('speak:')
while True:
    text = voice_recognition()
    print('Tu: '+text)
    text_generated = diferent_func(text)
    print('Bot: '+text_generated)
    speak = speaking(text_generated)

