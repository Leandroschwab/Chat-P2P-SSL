# -*- coding: utf-8 -*-
from Tkinter import *

import traceback

def novaConn(conn,usuarios,VarData):
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
                    mensagemChat(usuarios,msgRecA,VarData)

        except Exception as e:
            print('Um erro ocorreu!')
            traceback.print_exc()
            print e
            break
    conn.close()

def mensagemChat(usuarios,msgRecA,VarData):
    print "mensagemChat: started"
    porta = msgRecA[1]
    id = getIDPort(porta,usuarios)
    print id
    try:
        if (usuarios[id]['Janela']==True ):
            usuarios[id]['ChatText'].insert(INSERT, str(porta)+': ' + msgRecA[2] + "\n")
        else:
            print "janela esta fechada "
    except Exception as e:
        print "janela esta fechada "


def getIDPort(porta,usuarios):
    print "getIDPort: started"
    for valor in usuarios:
        if (valor['porta']==porta):
            return i
    print "Erro Porta==usuario nao encontrado"
    return -1

