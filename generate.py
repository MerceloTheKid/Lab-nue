from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization


def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

pri1, pub1 = generate_keys()
pri2, pub2 = generate_keys()

#transformacion de llave privada a foramte PEM
pri_1 = pri1.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
pri_2 = pri2.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

#transformacion de llave publica a formato PEM
pub_1 = pub1.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode("utf-8")  
pub_2 = pub2.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode("utf-8")  

with open ("destino_public.pem", "w") as mypublickey:
 mypublickey.write(pub_1)
with open ("origen_public.pem", "w") as mypublickey:
 mypublickey.write(pub_2)
with open ("destino_private.pem", "wb") as myprivatekey:
 myprivatekey.write(pri_1)
with open ("origen_private.pem", "wb") as myprivatekey:
 myprivatekey.write(pri_2)
