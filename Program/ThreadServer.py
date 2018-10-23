# -*- coding: utf-8 -*-
from Tkinter import *
from  GUI2 import newWindow
import traceback

def novaConn(conn,usuarios):
    while 1:
        try:
            data = conn.recv(1024)  # Recebe os dados
            if not data: break
            print "Servidou recebeu data: " + str(data)
            msgRec = str(data).split("-+;+-")
            for linha in msgRec:
                msgRecA = linha.split("-+,+-")
                print "Servidou recebeu linha: " + str(linha)

                if (msgRecA[0]=="Mensagem-chat"):
                    mensagemChat(usuarios,msgRecA)

        except Exception as e:
            print('Um erro ocorreu!')
            traceback.print_exc()
            print e
            break
    conn.close()

def mensagemChat(usuarios,msgRecA):
    print "mensagemChat: started"
    porta = msgRecA[1]
    id = getIDPort(porta,usuarios)
    print id
    if (usuarios[id]['Janela']==True ):
        usuarios[id]['ChatText'].insert(INSERT, str(porta)+': ' + msgRecA[2] + "\n")
    else:
        print "abrindo janela"
        newWindow(usuarios[id], id)
        usuarios[id]['ChatText'].insert(INSERT, str(porta)+': ' + msgRecA[2] + "\n")



def getIDPort(porta,usuarios):
    print "getIDPort: started"
    i=0
    for valor in usuarios:
        if (valor['ip']==porta):
            return i
        i=+1
    print "Erro Porta==usuario nao encontrado"
    return -1

