from g4f import client
import datetime
from pywhatkit import *

def diferent_func(text:str):
    if "play" in text:
        playonyt(text[text.index('play')+4:])
        return f"playing {text[text.index('play')+4]}"
    elif "what time is it" in text:
        hours = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        time =f'{hours} : {min}'
        return time
    elif "let's play" in text:
        pass
    else:
        cliente = client.Client()
        response = cliente.chat.completions.create(messages=[{"role":"user", "content":text}], model="gpt-3.5-turbo")
        return response.choices[0].message.content.strip()



