# -*- coding: utf-8 -*-
import socket
import sqlite3
from threading import *

def createDB():
    connSQL = sqlite3.connect('Database/user.db')
    cursor = connSQL.cursor()
    cursor.execute(
        "CREATE TABLE Info (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,variavel TEXT NOT NULL,valor TEXT);")
    cursor.execute(
        "CREATE TABLE Users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ip TEXT,porta TEXT);")
    connSQL.close()

createDB()

def checkOnlineOne(ip,porta):
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect((ip, porta))  # Abre uma conexão com IP e porta especificados
        conn.close()
    except Exception as e:
        print('Usuario Offline' + ip + ':' + porta)
        print e




def checkOnlineAll():
    connSQL = sqlite3.connect('Database/user.db')
    cursor = connSQL.cursor()
    cursor.execute("SELECT * FROM Users;")
    data = cursor.fetchall()
    if data:
    for linha in data:
        checkOnlineOne(str(linha[1]), str(linha[2]))
    connSQL.close()

ip= 
checkOnlineOne(127.0.0.1,porta)