# -*- coding: utf-8 -*-
import socket
import sqlite3
from Controll_functions import *

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
            Valor['online'] = checkOnlineOne(str(linha[1]),str(linha[2]))
            usuarios.append (Valor)
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

if __name__ == "__main__":
    usuarios= getUsuariosDB()
    #print usuarios[1]
    for valor in usuarios:
        print valor['ip']
        #Listbox.insert(END, usuarios[i].valor['ip'] + ':' + usuarios[i].valor['porta'] + '        Status' +                       usuarios[i].valor['online'])