from voiceRec import *
from func import *
import playsound


while True:
    try:
        text = voice_recognition().lower()
        if "alexa" in text:
            playsound.playsound('../sounds/ball-origin-beep.mp3')
            text = voice_recognition().lower()
            print('Tu: ' + text)
            text_generated = diferent_func(text)
            print('Bot: ' + text_generated)
            speak = speaking(text_generated)
    except:
        pass