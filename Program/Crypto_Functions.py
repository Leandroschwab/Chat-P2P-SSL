import os

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES


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
        public_key = private_key.publickey()
        # print(private_key.exportKey(format='PEM'))
        # print(public_key.exportKey(format='PEM'))

        VarData['myprivatekey'] = private_key
        VarData['mypublickey'] = public_key

        prv_file = open('Data/' + str(VarData['porta']) + "/private.pem", "w")
        prv_file.write("{}".format(private_key.exportKey()))
        pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "w")
        pub_file.write("{}".format(public_key.exportKey()))


if __name__ == "__main__":
    ''' print "ok"
 
     key = 'mysecretpassword'
     plaintext = 'secret Message A'
 
     encobj = AES.new(key, AES.MODE_ECB)
     ciphertext = encobj.encrypt(plaintext)
 
     # Resulting ciphertext in hex
     print ciphertext.encode('hex')'''
