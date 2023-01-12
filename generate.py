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

pri1, pub1 = generate_keys()
pri2, pub2 = generate_keys()

text_file = open ("destino_public.txt", "w")
n = text_file.write(pub1.exportKey().decode("utf-8"))
text_file.close()

text_file = open ("origen_public.txt", "w")
n = text_file.write(pub2.exportKey().decode("utf-8"))
text_file.close()

text_file = open ("destino_private.txt", "w")
n = text_file.write(pri1.exportKey().decode("utf-8"))
text_file.close()

text_file = open ("origen_private.txt", "w")
n = text_file.write(pri2.exportKey().decode("utf-8"))
text_file.close()
