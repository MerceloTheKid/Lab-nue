from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

#Se crea la llave privada y la llave publica
llave_privada_1 = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
llave_publica_1 = llave_privada_1.public_key()
llave_privada_2 = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
llave_publica_2 = llave_privada_2.public_key()

#transformacion de llave privada a foramte PEM
pem_private_key1 = llave_privada_1.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
pem_private_key2 = llave_privada_2.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

#transformacion de llave publica a formato PEM
public_key_pem1 = llave_publica_1.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode("utf-8")  
public_key_pem2 = llave_publica_2.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode("utf-8")  


#guarda en archivo privado key1 y 2
with open('llave1_priv.pem', 'wb') as myprivatekey:
    myprivatekey.write(pem_private_key1)
with open('llave2_priv.pem', 'wb') as myprivatekey:
    myprivatekey.write(pem_private_key2)

#guarda en archivo publico key1 y 2
with open('llave1_pub.pem', 'w') as mypublickey:
    mypublickey.write(public_key_pem1)
with open('llave2_pub.pem', 'w') as mypublickey:
    mypublickey.write(public_key_pem2)