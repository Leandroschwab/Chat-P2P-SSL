# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from threading import Thread

from Server import *

#t = Thread(target=server, args=())
#t.start()


def Send():
    global ChatEntry1 , ChatText1
    Var = ChatEntry1.get()
    print Var
    ChatEntry1.delete(0,END)
    # Msg.configure(state='enabled')
    ChatText1.insert(INSERT, 'Eu: ' + Var + "\n")
    # Msg.configure(state='disabled')

    return


def Add_Friend():
    global PORT_Entry, IP_Entry, ADD
    ADD = Toplevel(root)
    ADD.geometry('400x300+443+145')
    ADD.title('Invite')
    ADD.configure(background="#d9d9d9")

    Label1 = Label(ADD)
    Label1.place(relx=0.175, rely=0.167, height=21, width=63)
    Label1.configure(background="#d9d9d9",text='Digite o IP:')

    IP_Entry = Entry(ADD)
    IP_Entry.place(relx=0.475, rely=0.167, height=20, relwidth=0.41)

    PORT_Entry = Entry(ADD)
    PORT_Entry.place(relx=0.475, rely=0.4, height=20, relwidth=0.41)

    Label2 = Label(ADD)
    Label2.place(relx=0.125, rely=0.367, height=31, width=104)
    Label2.configure(background="#d9d9d9",text='Digite a Porta',width=104)

    Button1 = Button(ADD)
    Button1.place(relx=0.4, rely=0.667, height=44, width=87)
    Button1.configure(background="#d9d9d9",text='Adicionar',width=87,command=Add_Friend2)


def Add_Friend2():
    global PORT_Entry , IP_Entry ,ADD
    Temp = IP_Entry.get()
    Temp2 = PORT_Entry.get()
    print Temp
    Listbox.insert(END, Temp + '        Status')
    ADD.destroy()
    return

    ADD.mainloop()

def OpenChat(event):
    print 'hi'
    Chat = event.widget
    selection = Chat.curselection()
    Amigo = Chat.get(selection[0])
    newWindow(Amigo)

def newWindow(Amigo):
    global ChatEntry1 , ChatText1
    ChatWindow = Toplevel(root)
    ChatWindow.geometry("529x372+325+131")
    ChatWindow.title("Chat Window")
    ChatWindow.configure(background="#d9d9d9")

    ChatFrame1 = Frame(ChatWindow)
    ChatFrame1.place(relx=0.0, rely=0.0, relheight=0.148, relwidth=1.002)
    ChatFrame1.configure(relief=GROOVE,background="#d9d9d9",width=530)

   #ChatFrame4 = Frame(ChatWindow)
   #ChatFrame4.place(relx=0.019, rely=0.182, relheight=0.636, relwidth=0.557)
   #ChatFrame4.configure(relief=GROOVE,background="#d9d9d9",width=295)

   #ChatFrame5 = Frame(ChatWindow)
   #ChatFrame5.place(relx=0.66, rely=0.0, relheight=0.818, relwidth=0.311)
   #ChatFrame5.configure(relief=GROOVE,background="#d9d9d9",width=165)

    ChatFrame2 = Frame(ChatWindow)
    ChatFrame2.place(relx=0.0, rely=0.134, relheight=0.659, relwidth=1.002)
    ChatFrame2.configure(relief=GROOVE,background="#d9d9d9",width=530)

    ChatText1 = Text(ChatFrame2)
    ChatText1.place(relx=0.019, rely=0.082, relheight=0.873, relwidth=0.951)
    ChatText1.configure(width=504)

    ChatFrame3 = Frame(ChatWindow)
    ChatFrame3.place(relx=0.0, rely=0.78, relheight=0.228, relwidth=1.002)
    ChatFrame3.configure(relief=GROOVE,background="#d9d9d9",width=525)

    ChatEntry1 = Entry(ChatFrame3)
    ChatEntry1.place(relx=0.019, rely=0.118, height=60, relwidth=0.668)
    ChatEntry1.configure(width=354)

    ChatButton1 = Button(ChatFrame3)
    ChatButton1.place(relx=0.774, rely=0.235, height=44, width=87)
    ChatButton1.configure(background="#d9d9d9",text='Enviar',width=87)
    ChatButton1.configure(command=Send)

    return


root = Tk()
root.title('Chat p2p')
root.geometry('395x424+428+131')
root.configure(background="#d9d9d9")

Header = Frame(root)
Header.configure(width=125, background="#d9d9d9")
Header.place(relheight=0.126, relwidth=1.005)

Nome = Label(Header)
Nome.configure(anchor=W, background="#d9d9d9", text='Andre Felipe Tavares')
Nome.place(relx=0.013, rely=0.100, height=51, width=150)

Convidar = Button(Header)
Convidar.configure(background="#d9d9d9", text='Adicionar',command=Add_Friend)
Convidar.place(relx=0.785, rely=0.175, height=30, width=77)

Label_IP = Label(Header)
Label_Port = Label(Header)
Label_IP.configure(background="#d9d9d9", text='Ip')
Label_Port.configure(background="#d9d9d9", text='Porta')
Label_IP.place(relx=0.582, rely=0.118, height=21, width=34)
Label_Port.place(relx=0.582, rely=0.471, height=21, width=34)

Body = Frame(root)
Body.configure(relief=GROOVE, borderwidth="2", background="#d9d9d9", width='800')
Body.place(relx=0.0, rely=0.189, relheight=0.814, relwidth=1.005)

#TSeparator1 = ttk.Separator(Body)
#TSeparator1.configure(orient="vertical")
#TSeparator1.place(relx=0.656, rely=-0.013, relheight=1.013)

#Msg = Text(Body)
#Msg.configure(width='10', xscrollcommand='True')
#Msg.insert(END, 'Teste \n')
#Msg.place(relx='0.088', rely='0.076', relheight='0.889', relwidth='0.489')

Listbox = Listbox(Body)
Listbox.configure(width='214', yscrollcommand='True')
Listbox.bind("<Double-Button-1>", OpenChat)
Listbox.place(relx=0.228, rely=0.058, relheight=0.846,relwidth=0.567)

#Frame3 = Frame(root)
#Frame3.configure(relief=GROOVE, borderwidth="2", background="#d9d9d9", width='800')
#Frame3.place(relx='0.0', rely='0.773', relheight='0.227', relwidth='1.005')

#Button_Send = Button(Frame3)
#Button_Send.configure(background="#d9d9d9", text='Send')
#Button_Send.configure(command=Send)
#Button_Send.place(relx='0.788', rely='0.148', height='84', width='127')

#Chat = Text(Frame3)
#Chat.configure(borderwidth="2", font='Helvetica 14')
#Chat.place(relx='0.088', rely='0.222', height='70', relwidth='0.655')

root.mainloop()
