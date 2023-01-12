import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization

# comando donde se le pide al usuario ingresar una palabra
palabra = str.encode(input("Ingrese una palabra de maximo 16 letras: "))

with open("destino_public.txt", "rb") as key_file:
    pub_key = serialization.load_pem_private_key(key_file.read(),password=None)
with open("origen_private.txt", "rb") as key_file:
    pri_key = serialization.load_pem_public_key(key_file.read())