# -*- coding: utf-8 -*-
from Tkinter import *
import socket


def checkOnlineOne(ip, porta,VarData):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect((ip, int(porta)))  # Abre uma conexão com IP e porta especificados
        mensagem = "TesteOnline-+,+-" + str(VarData['porta']) + "-+,+-" + str(VarData['ip']) + "-+;+-"

        conn.sendall(mensagem)
        conn.close()

        return True
    except Exception as e:
        # print('Usuario Offline ' + ip + ':' + porta)
        # print e
        return False


def checkOnlineALL(usuarios, VarData):
    #print "checando usuarios"
    VarData['ListboxOnline'].delete(0, END)
    VarData['ListboxOffline'].delete(0, END)
    for Valor in usuarios:
        # if int(Valor['porta'])!=int(VarData['porta']):
        Valor['online'] = checkOnlineOne(Valor['ip'], Valor['porta'],VarData)
        if Valor['online']:
            VarData['ListboxOnline'].insert(END,
                                            Valor['ip'] + ':' + Valor['porta'])
        else:
            VarData['ListboxOffline'].insert(END,
                                             Valor['ip'] + ':' + Valor['porta'])
    VarData['root'].after(5000, checkOnlineALL, usuarios, VarData)




