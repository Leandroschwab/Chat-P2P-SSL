# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from threading import Thread

from Server import *

t = Thread(target=server, args=())
t.start()


def Send():
    Var = Chat.get(1.0, END)
    Chat.delete(1.0, END)
    print Var
    # Msg.configure(state='enabled')
    Msg.insert(INSERT, 'Eu: ' + Var + "\n")
    # Msg.configure(state='disabled')

    return Var


root = Tk()
root.title('Chat p2p')
root.geometry('800x600+276+77')
root.configure(background="#d9d9d9")

Header = Frame(root)
Header.configure(width=125, highlightbackground="#d9d9d9", background="#d9d9d9", relief=RAISED, borderwidth="2")
Header.place(relx=0.0, rely=0.0, relheight=0.126, relwidth=1.005)

Nome = Label(Header)
Nome.configure(anchor=W, background="#d9d9d9", text='Andre Felipe Tavares')
Nome.place(relx=0.013, rely=0.133, height=51, width=484)

Convidar = Button(Header)
Convidar.configure(background="#d9d9d9", text='Convidar')
Convidar.place(relx=0.863, rely=0.267, height=34, width=97)

Label_IP = Label(Header)
Label_Port = Label(Header)
Label_IP.configure(background="#d9d9d9", text='Ip')
Label_Port.configure(background="#d9d9d9", text='Porta')
Label_IP.place(relx=0.675, rely=0.133, height=21, width=144)
Label_Port.place(relx=0.675, rely=0.533, height=21, width=144)

Body = Frame(root)
Body.configure(relief=GROOVE, borderwidth="2", background="#d9d9d9", width='800')
Body.place(relx=0.0, rely=0.118, relheight=0.664, relwidth=1.005)

TSeparator1 = ttk.Separator(Body)
TSeparator1.configure(orient="vertical")
TSeparator1.place(relx=0.656, rely=-0.013, relheight=1.013)

Msg = Text(Body)
Msg.configure(width='10', xscrollcommand='True')
Msg.insert(END, 'Teste \n')
Msg.place(relx='0.088', rely='0.076', relheight='0.889', relwidth='0.489')

Listbox = Listbox(Body)
Listbox.configure(width='214', yscrollcommand='True')
Listbox.insert(END, 'André Felipe Tavares' + '        Status')
Listbox.place(relx='0.7', rely='0.076', relheight='0.891', relwidth='0.268')

Frame3 = Frame(root)
Frame3.configure(relief=GROOVE, borderwidth="2", background="#d9d9d9", width='800')
Frame3.place(relx='0.0', rely='0.773', relheight='0.227', relwidth='1.005')

Button_Send = Button(Frame3)
Button_Send.configure(background="#d9d9d9", text='Send')
Button_Send.configure(command=Send)
Button_Send.place(relx='0.788', rely='0.148', height='84', width='127')

Chat = Text(Frame3)
Chat.configure(borderwidth="2", font='Helvetica 14')
Chat.place(relx='0.088', rely='0.222', height='70', relwidth='0.655')

root.mainloop()
