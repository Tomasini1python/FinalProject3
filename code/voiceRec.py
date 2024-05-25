import speech_recognition as sr
import pyttsx3

def voice_recognition():
    voz = sr.Recognizer()

    with sr.Microphone() as mic:
        voz.adjust_for_ambient_noise(mic)
        audio = voz.listen(mic)
        text = voz.recognize_google(audio, language='en-GB')
        return text


def speaking(text):
    engine = pyttsx3.init()
    var = engine.getProperty('voices')
    engine.setProperty('voice', var[0].id)

    engine.say(text)
    engine.runAndWait()