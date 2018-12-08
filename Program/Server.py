# -*- coding: utf-8 -*-
import socket
from ThreadServer import *
from threading import Thread

########################################################################################################################
#Thread-server que gerencia as conexoes recebidas
########################################################################################################################
def server(s, VarData, usuarios):


    i = 0
    print "Servidor Rodando"
    while 1:
        try:
            s.listen(1)  # espera chegar pacotes na porta especificada
            conn, addr = s.accept()  # Aceita uma conexão
            #print "server: Aceitou uma nova conexao"
            #print 'Connected by', addr
            t = Thread(target=novaConn, args=(conn, usuarios,VarData))
            t.start()
        except Exception as e:
            print('server: Um erro ocorreu!')
            traceback.print_exc()
            print e
            break
