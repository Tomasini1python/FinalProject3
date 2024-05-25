from voiceRec import *
from func import *

while True:
    text = voice_recognition()
    print(text)
    text_generated = diferent_func(text)
    print(text_generated)
    speak = speaking(text_generated)






