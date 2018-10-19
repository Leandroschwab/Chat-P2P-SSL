# -*- coding: utf-8 -*-

import socket

def checkOnlineOne(ip,porta):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect((ip, porta))  # Abre uma conexão com IP e porta especificados
        conn.close()
        return True
    except Exception as e:
        #print('Usuario Offline' + ip + ':' + porta)
        #print e
        return False

