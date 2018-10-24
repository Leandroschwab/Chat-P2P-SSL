# -*- coding: utf-8 -*-
from Tkinter import *
import socket

def checkOnlineOne(ip,porta):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect((ip, int(porta)))  # Abre uma conexão com IP e porta especificados
        conn.close()
        return True
    except Exception as e:
        #print('Usuario Offline ' + ip + ':' + porta)
        #print e
        return False

def checkOnlineALL(usuarios,VarData):
    print "checando usuarios"
    VarData['Listbox'].delete(0, END)
    print "Clear"
    for Valor in usuarios:
        if int(Valor['porta'])!=int(VarData['porta']):
            Valor['online']= checkOnlineOne(Valor['ip'],Valor['porta'])
            VarData['Listbox'].insert(END, Valor['ip'] + ':' + Valor['porta'] + "       status: " + str(Valor['online']))
    VarData['root'].after(10000, checkOnlineALL,usuarios,VarData)