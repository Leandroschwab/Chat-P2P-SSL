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


def getUsuariosDB():                                #retorna uma matriz/lista no formato usuario=getUsuariosDB()
    print "getUsuariosDB: started"                  #pode chamar utilizando usuario[i]['ip'] ou usuario[i]['porta']
    usuarios = []
    connSQL = sqlite3.connect('Database/user.db')
    cursor = connSQL.cursor()
    cursor.execute("SELECT * FROM Users;")
    data = cursor.fetchall()
    i = 1
    if data:
        for linha in data:
            Valor={}
            Valor['ip']= str(linha[1])
            Valor['porta'] = str(linha[2])
            print i
            usuarios.append (Valor)
            #usuarios[i] = [str(linha[1]), str(linha[2])]


            i = i + 1
    connSQL.close()
    return usuarios

def addUsuarioDB(ip,porta):                         #addUsuarioDB("123.456.779.231","5050")
    print "addUsuarioDB: started"
    connSQL = sqlite3.connect('Database/user.db')
    cursor = connSQL.cursor()
    insert_stmt=(
        "INSERT INTO Users(ip,porta) VALUES ('"+ip+"','"+porta+"')")
    cursor.execute(insert_stmt)
    connSQL.commit()
    connSQL.close()
    print "addUsuarioDB: finish"

def checkOnlineAll():
    connSQL = sqlite3.connect('Database/user.db')
    cursor = connSQL.cursor()
    cursor.execute("SELECT * FROM Users;")
    data = cursor.fetchall()
    if data:
        for linha in data:
            checkOnlineOne(str(linha[1]), str(linha[2]))
    connSQL.close()


if __name__ == "__main__":

    addUsuarioDB("123.456.779.231","5050")
    usuarios =  getUsuariosDB()
    print usuarios