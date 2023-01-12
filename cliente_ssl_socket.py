import socket
import ssl

def programa_cliente():
    host = socket.gethostname()  # Direcccion del servidor (se asume servidor se ejecuta en la misma máquina)
    port = 5000  # numero de puerto del servidor
    client_cert = "client.crt"
    client_key = "client.key"
    context = ssl.SSLContext()
    context.load_cert_chain(client_cert, client_key)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crear socket
    client_socket = context.wrap_socket(client_socket,)
    client_socket.connect((host, port))  # intentar conexion SSL/TCP con servidor

    message = input(" -> ")  # leer mensaje  desde teclado

    while message.lower().strip() != 'chao':
        client_socket.send(message.encode())  #enviar mensaje
        data = client_socket.recv(1024).decode()  # recibir respuesta

        print('Recibido del servidor: ' + data)  # se muestra en consola

        message = input(" -> ")  # pida otra entrada

    client_socket.close()  # cierre de la coneccion


if __name__ == '__main__':
    programa_cliente()
