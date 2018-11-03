# -*- coding: utf-8 -*-
import time
from Tkinter import *
import ttk

from threading import Semaphore
from Server import *
from DB_Funcions import *
from Controll_functions import *
from Crypto_Functions import *


def Send(ChatEntry1, ChatText1, Amigo):
    print "Send: Started"
    Var = ChatEntry1.get()
    ChatEntry1.delete(0, END)
    # Msg.configure(state='enabled')
    ChatText1.insert(INSERT, 'Eu: ' + Var + "\n")
    # Msg.configure(state='disabled')
    mensagem = "Mensagem-chat-+,+-" + str(VarData['porta']) + "-+,+-" + Var

    connS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
    connS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connS.connect((Amigo['ip'], int(Amigo['porta'])))  # Abre uma conexão com IP e porta especificados
    connS.sendall(mensagem)
    connS.close()

    return  # O que essa funçao retorna ?? ela ja nao insere o texto no "ChatText1.insert(INSERT, 'Eu: ' + Var + "\n")"


def Add_Friend():
    global PORT_Entry, IP_Entry, ADD
    ADD = Toplevel(root)
    ADD.geometry('400x300+443+145')
    ADD.title('Invite')
    ADD.configure(background="#d9d9d9")

    Label1 = Label(ADD)
    Label1.place(relx=0.175, rely=0.167, height=21, width=63)
    Label1.configure(background="#d9d9d9", text='Digite o IP:')

    IP_Entry = Entry(ADD)
    IP_Entry.place(relx=0.475, rely=0.167, height=20, relwidth=0.41)

    PORT_Entry = Entry(ADD)
    PORT_Entry.place(relx=0.475, rely=0.4, height=20, relwidth=0.41)

    Label2 = Label(ADD)
    Label2.place(relx=0.125, rely=0.367, height=31, width=104)
    Label2.configure(background="#d9d9d9", text='Digite a Porta', width=104)

    Button1 = Button(ADD)
    Button1.place(relx=0.4, rely=0.667, height=44, width=87)
    Button1.configure(background="#d9d9d9", text='Adicionar', width=87, command=Add_Friend2)


def Add_Friend2():
    global PORT_Entry, IP_Entry, ADD
    Temp = IP_Entry.get()
    Temp2 = PORT_Entry.get()

    addUsuarioDB(Temp, Temp2, VarData)  # add Usuario no Banco de dados

    print Temp
    Valor = {}
    Valor['ip'] = Temp
    Valor['porta'] = Temp2

    usuarios.append(Valor)
    ADD.destroy()
    return  # n entendi isso

    ADD.mainloop()


def OpenChat(event):
    print 'OpenChat: Started'
    Chat = event.widget
    selection = Chat.curselection()
    Amigo = usuarios[selection[0]]  # Amigo recebe um dicionario dom dadso do usuario q esta conectado
    newWindow(Amigo, selection[0])


def newWindow(Amigo, id):
    print "newWindow: Started"
    ChatWindow = Toplevel()
    ChatWindow.geometry("529x372+325+131")
    ChatWindow.title("Chat Window " + str(Amigo['ip']) + ":" + Amigo['porta'])
    ChatWindow.configure(background="#d9d9d9")

    ChatFrame1 = Frame(ChatWindow)
    ChatFrame1.place(relx=0.0, rely=0.0, relheight=0.148, relwidth=1.002)
    ChatFrame1.configure(relief=GROOVE, background="#d9d9d9", width=530)

    ChatFrame2 = Frame(ChatWindow)
    ChatFrame2.place(relx=0.0, rely=0.134, relheight=0.659, relwidth=1.002)
    ChatFrame2.configure(relief=GROOVE, background="#d9d9d9", width=530)

    ChatText1 = Text(ChatFrame2)
    ChatText1.place(relx=0.019, rely=0.082, relheight=0.873, relwidth=0.951)
    ChatText1.configure(width=504)

    ChatFrame3 = Frame(ChatWindow)
    ChatFrame3.place(relx=0.0, rely=0.78, relheight=0.228, relwidth=1.002)
    ChatFrame3.configure(relief=GROOVE, background="#d9d9d9", width=525)

    ChatEntry1 = Entry(ChatFrame3)
    ChatEntry1.place(relx=0.019, rely=0.118, height=60, relwidth=0.668)
    ChatEntry1.configure(width=354)

    ChatButton1 = Button(ChatFrame3)
    ChatButton1.place(relx=0.774, rely=0.235, height=44, width=87)
    ChatButton1.configure(background="#d9d9d9", text='Enviar', width=87)
    ChatButton1.configure(command=lambda *args: Send(ChatEntry1, ChatText1, Amigo))

    usuarios[id]['Janela'] = True  # armazena a informaçao q a janela esta aberta
    usuarios[id]['ChatText'] = ChatText1  # armazena a informaçao do local da janela,
    # para ser usado pelo servidor escrever na janela
    ChatWindow.protocol("WM_DELETE_WINDOW",
                        lambda: on_closing_chat(id, ChatWindow))  # executa o comando avisando q a janela fechou
    ChatWindow.mainloop()
    return


def newWindow2(Amigo, id, mensagem):
    print "newWindow: Started"
    ChatWindow = Toplevel()
    ChatWindow.geometry("529x372+325+131")
    ChatWindow.title("Chat Window " + str(Amigo['ip']) + ":" + Amigo['porta'])
    ChatWindow.configure(background="#d9d9d9")

    ChatFrame1 = Frame(ChatWindow)
    ChatFrame1.place(relx=0.0, rely=0.0, relheight=0.148, relwidth=1.002)
    ChatFrame1.configure(relief=GROOVE, background="#d9d9d9", width=530)

    ChatFrame2 = Frame(ChatWindow)
    ChatFrame2.place(relx=0.0, rely=0.134, relheight=0.659, relwidth=1.002)
    ChatFrame2.configure(relief=GROOVE, background="#d9d9d9", width=530)

    ChatText1 = Text(ChatFrame2)
    ChatText1.place(relx=0.019, rely=0.082, relheight=0.873, relwidth=0.951)
    ChatText1.configure(width=504)

    ChatFrame3 = Frame(ChatWindow)
    ChatFrame3.place(relx=0.0, rely=0.78, relheight=0.228, relwidth=1.002)
    ChatFrame3.configure(relief=GROOVE, background="#d9d9d9", width=525)

    ChatEntry1 = Entry(ChatFrame3)
    ChatEntry1.place(relx=0.019, rely=0.118, height=60, relwidth=0.668)
    ChatEntry1.configure(width=354)

    ChatButton1 = Button(ChatFrame3)
    ChatButton1.place(relx=0.774, rely=0.235, height=44, width=87)
    ChatButton1.configure(background="#d9d9d9", text='Enviar', width=87)
    ChatButton1.configure(command=lambda *args: Send(ChatEntry1, ChatText1, Amigo))

    usuarios[id]['Janela'] = True  # armazena a informaçao q a janela esta aberta
    usuarios[id]['ChatText'] = ChatText1  # armazena a informaçao do local da janela,
    ChatText1.insert(INSERT, Amigo['porta'] + ': ' + mensagem + "\n")

    # para ser usado pelo servidor escrever na janela
    ChatWindow.protocol("WM_DELETE_WINDOW",
                        lambda: on_closing_chat(id, ChatWindow))  # executa o comando avisando q a janela fechou

    ChatWindow.mainloop()

    return


def openNewChat(usuarios, VarData):
    print "openNewChat: iniciado"
    print "openNewChat: Lock"
    VarData['mutex'].acquire()
    if (VarData['openChat'] != ""):
        data = VarData['openChat'].split("$+$")
        id = int(data[0])

        print "janela estava fechada "

        print "openNewChat: UnLock"
        VarData['mutex'].release()
        VarData['openChat'] = ""
        VarData['Openboolean'] = True
        VarData['root'].after(1000, openNewChat, usuarios, VarData)
        newWindow2(usuarios[id], id, data[1])
    print "openNewChat: UnLock"
    VarData['mutex'].release()
    VarData['root'].after(1000, openNewChat, usuarios, VarData)


def on_closing_chat(id, ChatWindow):  # executa quando fecha a janela do chat
    print "on_closing_chat: fechando a janela"
    usuarios[id]['Janela'] = False  # armazena a informaçao q a janela esta fechada

    ChatWindow.destroy()


if __name__ == "__main__":
    global usuarios
    global VarData
    VarData = {}
    VarData['nome'] = "nome"  # raw_input("digite a nome: ")
    VarData['porta'] = input("digite a porta: ")
    VarData['mutex'] = Semaphore()
    VarData['openChat'] = ""
    VarData['Openboolean'] = False

    root = Tk()
    root.title('Chat p2p ' + str(VarData['porta']))
    root.geometry('600x524+368+93')
    root.configure(background="#d9d9d9")

    VarData['root'] = root

    Header = Frame(root)
    Header.place(relx=0.0, rely=0.0, relheight=0.258, relwidth=1.008)
    Header.configure(background="#d9d9d9", width=605)

    Nome_Label = Label(Header)
    Nome_Label.place(relx=0.0, rely=0.0, height=51, width=604)
    Nome_Label.configure(background="#d9d9d9", text=VarData['nome'], width=604)

    IP = Label(Header)
    IP.place(relx=0.182, rely=0.444, height=31, width=194)
    IP.configure(justify=LEFT, anchor=W, background="#d9d9d9", text=socket.gethostbyname(socket.gethostname()),
                 width=194)

    Porta = Label(Header)
    Porta.place(relx=0.182, rely=0.741, height=31, width=74)
    Porta.configure(background="#d9d9d9", text=VarData['porta'], width=74)

    Adicionar_Amigo = Button(Header)
    Adicionar_Amigo.place(relx=0.562, rely=0.444, height=64, width=177)
    Adicionar_Amigo.configure(background="#d9d9d9", text='Adicionar Amigo', command=Add_Friend, width=177)

    IP_Label = Label(Header)
    IP_Label.place(relx=0.0, rely=0.444, height=31, width=104)
    IP_Label.configure(background="#d9d9d9", text='Ip:', width=104)

    Porta_Label = Label(Header)
    Porta_Label.place(relx=0.0, rely=0.741, height=31, width=104)
    Porta_Label.configure(background="#d9d9d9", text='Porta:', width=104)

    Listbox_online = Listbox(root)
    Listbox_online.place(relx=0.083, rely=0.363, relheight=0.576, relwidth=0.34)
    Listbox_online.bind("<Double-Button-1>", OpenChat)
    Listbox_online.configure(background="white", font="TkFixedFont", width=204)

    Listbox_offline = Listbox(root)
    Listbox_offline.place(relx=0.6, rely=0.363, relheight=0.576, relwidth=0.34)
    Listbox_offline.configure(background="white", font="TkFixedFont", width=204)

    VarData['ListboxOnline'] = Listbox_online
    VarData['ListboxOffline'] = Listbox_offline

    Online = Label(root)
    Online.place(relx=0.083, rely=0.267, height=41, width=204)
    Online.configure(background="#d9d9d9", text='Online', width=204)

    Offline = Label(root)
    Offline.place(relx=0.65, rely=0.267, height=31, width=134)
    Offline.configure(background="#d9d9d9", text='Offline', width=134)

    createDB(VarData)  # Cria caso nao exista o banco de dados
    createMyKeys(VarData)  #

    usuarios = getUsuariosDB(VarData)  # pega todos usuario no banco de dados

    HOST = ''  # Symbolic name meaning all available interfaces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, VarData['porta']))  # liga o socket com IP e porta

    print "iniciando servidor"
    t = Thread(target=server, args=(s, VarData, usuarios))
    t.start()
    checkOnlineALL(usuarios, VarData)
    openNewChat(usuarios, VarData)

    root.mainloop()
