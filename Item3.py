from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

# se abren los archivo del llave publica, firma y mensaje del emisor
with open("llave1_pub.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())
with open("firma.txt", "rb") as key_file:
    firma =key_file.read()
with open("mensaje.txt", "rb") as key_file:
    mensaje = key_file.read()

#se utiliza try except para obtener el error y mostrarlo en pantalla si la firma es valida o invalida
try:
    public_key.verify(firma, mensaje, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    print("Firma Valida")
except:
  print("Firma No Valida")