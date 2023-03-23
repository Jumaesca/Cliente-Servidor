import socket

# Definimos la dirección IP y el puerto donde el servidor estará escuchando
HOST = '127.0.0.1'  # Dirección IP local
PORT = 5000        # Puerto de escucha

# Creamos un objeto socket para el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Configuramos el socket para que pueda ser reutilizado después de cerrarse
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Vinculamos el objeto socket al host y puerto especificados
server_socket.bind((HOST, PORT))
# Ponemos el servidor en modo escucha
server_socket.listen()

# Definimos una función para procesar las solicitudes de búsqueda


def procesar_busqueda(busqueda):
    # Aquí implementamos la lógica de búsqueda
    # Por ejemplo, puedes buscar en una base de datos o en un archivo
    # En este caso, simplemente devolvemos un mensaje de respuesta
    return f"Resultado de búsqueda para '{busqueda}': ... "


# Bucle principal del servidor
while True:
    # Esperamos a que un cliente se conecte
    print('Esperando conexiones entrantes...')
    client_socket, address = server_socket.accept()
    print(f'Conexión entrante desde {address}')

    # Recibimos la solicitud de búsqueda del cliente
    busqueda = client_socket.recv(1024).decode()
    print(f"Solicitud de búsqueda recibida: '{busqueda}'")

    # Procesamos la solicitud de búsqueda y preparamos la respuesta
    respuesta = procesar_busqueda(busqueda)

    # Enviamos la respuesta al cliente
    client_socket.send(respuesta.encode())

    # Cerramos la conexión con el cliente
    client_socket.close()
