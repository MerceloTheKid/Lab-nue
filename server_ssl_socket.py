#openssl req -newkey rsa:2048 -x509 -sha256 -days 365 -nodes -out client.crt -keyout client.key
#http://slproweb.com/products/Win32OpenSSL.html
import socket
import ssl

def programa_servidor():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # use puerto mayor a 1024
    client_cert = "client.crt"
    server_cert = "server.crt"
    server_key = "server.key"

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(server_cert, server_key)
    context.load_verify_locations(client_cert)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  # crear un socket
    server_socket.bind((host, port))  # Asignele nombre local y puerto escogido

    # configure cuando clientes el servidor puede atender simultaneamente
    server_socket.listen(2)

    conn, address = server_socket.accept()  # esperando un cliente, al llegar es aceptado
    print("Coneccion desde: " + str(address))
    conn = context.wrap_socket(conn, server_side=True)

    while True:
        # recibir flujo de datos. Se leeran nuevos datos por cada 1024 bytes recepcionados
        data = conn.recv(1024).decode()
        if not data:
            # Si no se reciben datos, terminar
            break
        print("desde el cliente: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # datos enviado al cliente

    conn.close()  # cierre conexion


if __name__ == '__main__':
    programa_servidor()
