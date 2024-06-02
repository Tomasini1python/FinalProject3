from g4f import client
import datetime
from pywhatkit import *
import requests

def diferent_func(text:str):
    if "play" in text:
        playonyt(text[text.index('play')+4:])
        return f"playing {text[text.index('play')+4]}"

    elif "what time is it" in text:
        hours = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        time = f'{hours} : {min}'
        return time

    elif "what is the weather like in" in text:
        city = text[len('what is the weather like in')+1:]
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=523d29d6950b43bae1b373b563154b71')
        weather_json = weather.json()
        info = f'Sky: {weather_json["weather"]["main"]}; Temperature: {float(weather_json["main"]["temp"])-273.15}'
        print(info)
        return info

    elif "is the weather like in" in text:
        city = text[len('what is the weather like in')+1:]
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=523d29d6950b43bae1b373b563154b71')
        weather_json = weather.json()
        info = f'Sky: {weather_json["weather"]["main"]}; Temperature: {float(weather_json["main"]["temp"])-273.15}'
        print(info)
        return info

    else:
        cliente = client.Client()
        response = cliente.chat.completions.create(messages=[{"role":"user", "content":text}], model="gpt-3.5-turbo")
        return response.choices[0].message.content.strip()