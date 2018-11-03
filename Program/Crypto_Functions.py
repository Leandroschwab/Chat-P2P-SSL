import os

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
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
        public_key = private_key.publickey()
        # print(private_key.exportKey(format='PEM'))
        # print(public_key.exportKey(format='PEM'))

        VarData['myprivatekey'] = private_key
        VarData['mypublickey'] = public_key
        print VarData['mypublickey']
        prv_file = open('Data/' + str(VarData['porta']) + "/private.pem", "w")
        prv_file.write("{}".format(private_key.exportKey()))
        pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "w")
        pub_file.write("{}".format(public_key.exportKey()))


#def createAES(Vardata, userValor,porta):


if __name__ == "__main__":
    #key = 'mysecretpassword'
    key = Random.new().read(16)
    print key.encode('hex')

    plaintext = 'secret Message A'

    AEScipher = AES.new(key, AES.MODE_ECB)

    ciphertext = AEScipher.encrypt(plaintext)
    #print ciphertext
    # Resulting ciphertext in hex
    print ciphertext.encode('hex')

