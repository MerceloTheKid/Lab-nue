import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

#este es el proceso de codificado
cipher = Cipher(algorithms.AES(llave), modes.CBC(llave_secreta), backend=default_backend())
encryptor = cipher.encryptor()

#palabra ya codificada
cbc_ct = encryptor.update(padded_plain_text) + encryptor.finalize()

print('palabra cifrada:',cbc_ct)

#luego de codificar, guardames el codificado en este archivo
with open('codificar.txt', 'wb') as mykey:
    mykey.write(cbc_ct)
