from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

#se ingresa el texto por teclado y se guarda en una variable
text = str.encode(input("Ingrese un texto: "))

#se abren las llaves privada y publica 1
with open("llave1_priv.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(),password=None)
with open("llave1_pub.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

#se firma el mensaje con RSA
firma = private_key.sign(text, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

#guarda firma y mensaje en archivos diferentes
with open('mensaje.txt', 'wb') as mykey:
    mykey.write(text)
with open('firma.txt', 'wb') as mykey:
    mykey.write(firma)