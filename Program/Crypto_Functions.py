# -*- coding: utf-8 -*-
import os
import socket

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random


def createMyKeys(VarData):
    if os.path.exists('Data/' + str(VarData['porta']) + '/private.pem'):
        print 'Carregando chaves!'
        prv_file = open('Data/' + str(VarData['porta']) + "/private.pem", "r")
        pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "r")
        private_key = RSA.importKey(prv_file.read())
        public_key = RSA.importKey(pub_file.read())
        VarData['myprivatekey'] = private_key
        VarData['mypublickey'] = public_key

    else:
        print 'Criando chave privada!'
        private_key = RSA.generate(1024)
        print 'Criando chave publica!'
        public_key = private_key.publickey()
        VarData['myprivatekey'] = private_key
        VarData['mypublickey'] = public_key
        print private_key.exportKey()
        print public_key.exportKey()
        prv_file = open('Data/' + str(VarData['porta']) + "/private.pem", "w")
        prv_file.write("{}".format(private_key.exportKey()))
        pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "w")
        pub_file.write("{}".format(public_key.exportKey()))


def createSession_key(VarData, userValor):
    print "createSession_key: started"
    session_key = Random.new().read(16)
    print "Criando chave AES" + session_key.encode('hex')

    Clientepub_file = open('Data/' + str(VarData['porta']) + "/" + str(userValor['porta']) + "public.pem", "r")
    Clientpublic_key = RSA.importKey(Clientepub_file.read())
    cipher_rsa = PKCS1_OAEP.new(Clientpublic_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    mensagem = "ChatAES-+,+-" + str(VarData['porta']) + "-+,+-" + enc_session_key + "-+;+-"

    userValor['ChatAESKey'] = session_key

    connS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # qw12IPv4,tipo de socket
    connS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connS.connect((userValor['ip'], int(userValor['porta'])))  # Abre uma conexão com IP e porta especificados
    connS.sendall(mensagem)
    connS.close()


if __name__ == "__main__":
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    session_key = Random.new().read(16)
    print session_key.encode('hex')


    data = raw_input("digite: ")
    size = len(data)
    zeros = (16-size%16)
    for i in range(zeros):
        data +=" "
    print data + " " + str(len(data))
    cipher_aes = AES.new(session_key, AES.MODE_ECB )
    ciphertext = cipher_aes.encrypt(data)
    print ciphertext.encode('hex')
    text =cipher_aes.decrypt(ciphertext)
    print text
    '''
    plaintext = 'secret Message A'

    AEScipher = AES.new(key, AES.MODE_ECB)

    ciphertext = AEScipher.encrypt(plaintext)
    #print ciphertext
    # Resulting ciphertext in hex
    print ciphertext.encode('hex')

'''
