import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import padding as paddin
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# comando donde se le pide al usuario ingresar una palabra
palabra = str.encode(input("Ingrese una palabra de maximo 16 letras: "))

# usando padding rellenamos el string deseado, en este caso la palabra ingresada
padder = paddin.PKCS7(128).padder()
#print(len(palabra))
padded_plain_text = padder.update(palabra) + padder.finalize()
len(padded_plain_text)
#print(padded_plain_text)

with open("destino_public.pem", "rb") as key_file:
 pub_key = serialization.load_pem_public_key(key_file.read())
with open("origen_private.pem", "rb") as key_file:
 pri_key = serialization.load_pem_private_key(key_file.read(),password=None)

# #se firma el mensaje con RSA
firma = pri_key.sign(palabra, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

#este es el proceso de codificado
# cipher = Cipher(algorithms.AES(pub_key), modes.CBC(pri_key), backend=default_backend())
# encryptor = cipher.encryptor()

# # #palabra ya codificada
# cbc_ct = encryptor.update(padded_plain_text) + encryptor.finalize()

# #guarda firma y mensaje en archivos diferentes
# with open('mensaje.txt', 'wb') as mykey:
#     mykey.write(palabra)
# with open('firma.txt', 'wb') as mykey:
#     mykey.write(firma)
# with open('codificar.txt', 'wb') as mykey:
#     mykey.write(cbc_ct)