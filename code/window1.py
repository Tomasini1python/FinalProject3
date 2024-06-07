from tkinter import *
from voiceRec import *
from func import *
import os





def Add():
    text = En_input.get()
    En_input.delete(0, END)

    tx_teste.configure(state='normal')
    tx_teste.insert('end', f'Tu: {text}\n')
    tx_teste.configure(state='disable')

    Func(text.lower())


def Func(texto):

    try:
        thing = diferent_func(texto)
    except:
        thing = 'Something went wrong... please report it...'


    tx_teste.configure(state='normal')
    tx_teste.insert('end', f'Nexa: {thing}\n')
    tx_teste.configure(state='disable')

    if speak == True:
        speaking(thing)
    else:
        pass


def Speak():
    global speak
    print(tx_teste.get('1.0', END))
    if speak == True:
        speak = False
    if speak == False:
        speak = True


def Saving():
    name = En_name.get()
    txt = tx_teste.get('1.0', END)

    tx_teste.option_clear()

    print(txt)

    with open(f'../LOG/{name}.txt', 'w') as file:
        file.write(txt)

    ls_conversas.insert(0, f'{name}.txt')


def Chat(event):
    tx_teste.configure(state='normal')
    tx_teste.delete('1.0', END)
    cs = ls_conversas.curselection()
    with open(f'../LOG/{ls_conversas.get(cs)}', 'r') as file:
        tx_teste.insert(END, file.read())

    tx_teste.configure(state='disable')



# Colors

white = '#ffffff'
back = '#0d0038'
cinza = '#2E2E2E'

# Essencial

speak = False


# window

root = Tk()
root.geometry('600x600+1+1')
root.title('NEXA AI')
root.wm_resizable(width=False, height=False)
root.configure(bg=back)

add = PhotoImage(file='../images/icons8-paper-airplane-25.png')
plus = PhotoImage(file='../images/icons8-save-25.png')
speak_img = PhotoImage(file='../images/icons8-speak-25.png')

# Title

Lb_title = Label(root, text='NEXA AI', font='IrishGrover 55', fg=white, bg=back)
Lb_title.place(width=282, height=91, x=159, y=0)

# Chat

Cv = Canvas(root, bg='#15005A')
Cv.place(x=171, y=112, width=422, height=393)

SC_text = Scrollbar(Cv, bg='#15005A')
SC_text.pack(side=RIGHT, fill=Y)

tx_teste = Text(Cv, state='disable', bg='#15005A', fg=white)
tx_teste.pack()

# Conversas

Cv2 = Canvas(root, bg=cinza, bd=0, relief='ridge')
Cv2.place(x=14, y=112, width=142, height=480)

ls_conversas = Listbox(Cv2, bg=cinza, fg=white)
for e in os.listdir('../LOG'):
    ls_conversas.insert(0, e)
ls_conversas.bind('<Double-1>', Chat)
ls_conversas.place(x=0, y=30, width=142, height=450)

Sc_ls = Scrollbar(ls_conversas)
Sc_ls.pack(side=RIGHT, fill=Y)

Bt_save = Button(Cv2, image=plus, command=Saving)
Bt_save.place(x=3, y=3, width=25, height=25)

En_name = Entry(Cv2)
En_name.place(x=33, y=4, width=100, height=23)

# Inputs

En_input = Entry(root, font='Arial 12')
En_input.place(width=390, height=27, x=171, y=528)

Bt_add = Button(root, image=add, command=Add)
Bt_add.place(width=27, height=27, x=566, y=528)

Bt_speak = Checkbutton(root, image=speak_img, command=Speak)
Bt_speak.place(width=50, height=27, x=543, y=566)



root.mainloop()
