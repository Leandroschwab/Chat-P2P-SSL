# -*- coding: utf-8 -*-

import traceback
def novaConn(conn,):
    while 1:
        try:
            data = conn.recv(1024)  # Recebe os dados
            if not data: break
            print "Servidou recebeu data: " + str(data)
            msgRec = str(data).split("-+,+-")
            for linha in msgRec:
                msgRecA = linha.split("-,-")
                print "Servidou recebeu linha: " + str(linha)

        except Exception as e:
            print('Um erro ocorreu!')
            traceback.print_exc()
            print e
            break
    conn.close()
