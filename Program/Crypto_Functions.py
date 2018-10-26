import os

from Crypto.PublicKey import RSA


def createMyKeys(VarData):
    try:
        os.mkdir('Data/' + str(VarData['porta']))
    except Exception as e:
        print "pasta do usuario ja existe"

    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    print(private_key.exportKey(format='PEM'))
    print(public_key.exportKey(format='PEM'))

    prv_file = open('Data/' + str(VarData['porta']) + "/private.pem", "w")
    prv_file.write("{}".format(private_key.exportKey()))

    pub_file = open('Data/' + str(VarData['porta']) + "/public.pem", "w")
    pub_file.write("{}".format(public_key.exportKey()))

