# -*- coding: utf-8 -*-
import socket
from ThreadServer import *
from threading import Thread, Lock, BoundedSemaphore, Semaphore

def server(usuarios,):
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = input("digite a porta: ")
                  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4,tipo de socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) #liga o socket com IP e porta


    print "Servidor Rodando"
    while 1:
        s.listen(1)  # espera chegar pacotes na porta especificada
        conn, addr = s.accept()  # Aceita uma conexão
        print "Aceitou uma nova conexao"
        print 'Connected by', addr
        t = Thread(target=novaConn, args=(conn,usuarios))
        t.start()

