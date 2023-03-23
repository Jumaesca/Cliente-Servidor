import socket

# Definimos la dirección IP y el puerto del servidor
HOST = '127.0.0.1'  # Dirección IP local del servidor
PORT = 5000        # Puerto de escucha del servidor

# Creamos un objeto socket para el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectamos el objeto socket al host y puerto del servidor
client_socket.connect((HOST, PORT))

# Enviamos la solicitud de búsqueda al servidor
busqueda = input("Introduce tu búsqueda: ")
client_socket.send(busqueda.encode())

# Recibimos la respuesta del servidor y la imprimimos en pantalla
respuesta = client_socket.recv(1024).decode()
print(respuesta)

# Cerramos la conexión con el servidor
client_socket.close()
