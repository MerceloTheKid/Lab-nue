import base64
from Crypto import Random 
from Crypto.PublicKey import RSA

def toBase64(string):
    return base64.b64encode(string)
def generate_keys():

    modulus_length = 256*4
    private_key = RSA.generate(modulus_length, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key

pri, pub = generate_keys()

#print(pri, pub)



private_key = pri.exportKey()
public_key = pub.exportKey()


#print(private_key, "\n\n\n", public_key)

text_file = open ("destino.txt", "w")
n = text_file.write(pub.exportKey().decode("utf-8"))
text_file.close()

text_file = open ("origen.txt", "w")
n = text_file.write(pri.exportKey().decode("utf-8"))
text_file.close()
