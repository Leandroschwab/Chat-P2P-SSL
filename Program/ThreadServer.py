# -*- coding: utf-8 -*-
import socket
import time
from Tkinter import *
from Crypto.PublicKey import RSA
import traceback

from DB_Funcions import addUsuarioDB



def novaConn(conn, usuarios, VarData):
    while 1:
        try:
            data = conn.recv(1024)  # Recebe os dados
            if not data: break
            #print "Servidou recebeu data: " + str(data)
            msgRec = str(data).split("-+;+-")
            for linha in msgRec:
                msgRecA = linha.split("-+,+-")
                #print "Servidou recebeu linha: " + str(linha)

                if (msgRecA[0] == "Mensagem-chat"):
                    print "mensagem chat"

                    mensagemChat(usuarios, msgRecA, VarData)
                if (msgRecA[0] == "TesteOnline"):
                    print "recebi teste online"

                    porta = msgRecA[1]
                    ip = msgRecA[2]
                    PortaCliente = getIDPort(porta,usuarios)
                    if (PortaCliente == -1):
                        pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "r")
                        pubread = pub_file.read()
                        connS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
                        connS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        connS.connect(
                            (ip, int(porta)))  # Abre uma conexão com IP e porta especificados
                        mensagem = "publicKey-+,+-" + str(VarData['porta']) + "-+,+-" + str(VarData['ip'])+ "-+,+-"+ pubread + "-+;+-"

                        connS.sendall(mensagem)
                        connS.close()

                if (msgRecA[0] == "publicKey"):
                    print "recebi publickey"
                    print linha
                    porta = msgRecA[1]
                    ip = msgRecA[2]
                    public_key = RSA.importKey(msgRecA[3])
                    pub_file = open('Data/' + str(VarData['porta']) +"/"+ porta +"public.pem", "w")
                    pub_file.write("{}".format(public_key.exportKey()))
                    addUsuarioDB(ip, porta, VarData)

                    Valor = {}
                    Valor['ip'] = ip
                    Valor['porta'] = porta
                    usuarios.append(Valor)

                    pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "r")
                    pubread = pub_file.read()
                    connS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
                    connS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    connS.connect(
                        (ip, int(porta)))  # Abre uma conexão com IP e porta especificados
                    mensagem = "publicKey2-+,+-" + str(VarData['porta']) + "-+,+-" + str(
                        VarData['ip']) + "-+,+-" + pubread + "-+;+-"

                    connS.sendall(mensagem)
                    connS.close()

                if (msgRecA[0] == "publicKey2"):
                    print "recebi publickey"
                    print linha
                    porta = msgRecA[1]
                    ip = msgRecA[2]
                    Valor = {}
                    Valor['ip'] = ip
                    Valor['porta'] = porta
                    usuarios.append(Valor)
                    public_key = RSA.importKey(msgRecA[3])
                    pub_file = open('Data/' + str(VarData['porta']) + "/" + porta + "public.pem", "w")
                    pub_file.write("{}".format(public_key.exportKey()))
                    addUsuarioDB(ip, porta, VarData)


        except Exception as e:
            print('Um erro ocorreu!')
            traceback.print_exc()
            print e
            break
    conn.close()


def mensagemChat(usuarios, msgRecA, VarData):
    print "mensagemChat: started"
    porta = msgRecA[1]
    id = getIDPort(porta, usuarios)  #int
    try:
        if (usuarios[id]['Janela'] == True):  # verifica se a janela com o outro usuario ja esta aberta

            usuarios[id]['ChatText'].insert(INSERT, str(porta) + ': ' + msgRecA[2] + "\n")
        else:
            print "else: janela esta fechada "
            VarData['openChat'] = str(id) + "$+$" + msgRecA[2]

    except Exception as e:
        print "Exception : janela esta fechada  "
        VarData['openChat'] = str(id) + "$+$" + msgRecA[2]

def getIDPort(porta, usuarios):
    print "getIDPort: started"
    i = 0
    for Valor in usuarios:
        if (Valor['porta'] == porta):
            return i
        i = i + 1
    print "Erro Porta==usuario nao encontrado"
    return -1
