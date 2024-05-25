import speech_recognition as sr

def voice_recognition():
    voz = sr.Recognizer()

    with sr.Microphone() as mic:
        voz.adjust_for_ambient_noise(mic)
        audio = voz.listen(mic)
        text = voz.recognize_google(audio, language='en-GB')
        return text
