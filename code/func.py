from g4f import client

def diferent_func(text:str):
    if "play" in text:
        text.index('play')+4

    else:
        cliente = client.Client()
        response = cliente.chat.completions.create(messages=[{"role":"user", "content":text}], model="gpt-3.5-turbo")
        return response.choices[0].message.content.strip()



