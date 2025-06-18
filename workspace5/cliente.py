#!/usr/bin/env python3
# import socket

# # Crear socket TCP/IP
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Conectar al servidor
# client_socket.connect(('172.17.144.21', 5000))
# print("📡 Conectado al servidor. Escribe operaciones como:suma,resta,div,mul")
# print("   10,5,suma   o   8,0,div")
# print("   Escribe 'salir' para salir.")

# while True:
#     # Leer entrada del usuario
#     user_input = input(">>> ").strip()
#     if not user_input:
#         continue

#     # Enviar entrada al servidor
#     client_socket.sendall(user_input.encode("utf-8"))

#     # Si es "quit", salimos del bucle y cerramos
#     if user_input.lower() == "salir":
#         break

#     # Recibir y mostrar la respuesta del servidor
#     try:
#         response = client_socket.recv(1024).decode("utf-8")
#         print(f"Servidor: {response}")
#     except:
#         print("Error recibiendo respuesta del servidor.")
#         break

# # Cerrar el socket
# client_socket.close()
# print("[*] Conexión cerrada.")









# #!/usr/bin/env python3
# import socket    # Para conexiones TCP/IP
# import json      # Para manejar JSON

# # Crear un socket TCP
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Conectarse al servidor en localhost y puerto 5000
# # Cambia "localhost" por la IP del servidor si es otra computadora
# client_socket.connect(('172.17.144.21', 5000))
# print("[*] Conectado al servidor.")

# print("Envía operaciones en lote en formato JSON.")
# print("Ejemplo:")
# print('[{"n1": 5, "n2": 3, "op": "suma"},{"n1": 10, "n2": 2, "op": "resta"},{"n1": 7, "n2": 3, "op": "mul"},{"n1": 8, "n2": 4, "op": "div"}]')
# print("O escribe 'quit' para salir.")

# while True:
#     # Leer entrada del usuario (cadena JSON o 'quit')
#     user_input = input(">>> ").strip()

#     # Si el usuario quiere salir, enviar 'quit' al servidor y cerrar
#     if user_input.lower() == "quit":
#         client_socket.sendall("quit".encode("utf-8"))
#         break

#     try:
#         # Intentar convertir la entrada a un objeto JSON (lista de operaciones)
#         json_data = json.loads(user_input)

#         # Enviar los datos serializados como JSON al servidor
#         client_socket.sendall(json.dumps(json_data).encode("utf-8"))

#         # Esperar respuesta del servidor (máximo 4096 bytes)
#         response = client_socket.recv(4096).decode("utf-8")

#         # Convertir respuesta JSON a lista de resultados
#         results = json.loads(response)

#         print("Respuesta del servidor:")
#         # Mostrar cada resultado u error recibido
#         for i, r in enumerate(results):
#             if "result" in r:
#                 print(f"  Operación {i+1}: RESULTADO = {r['result']}")
#             else:
#                 print(f"  Operación {i+1}: ERROR = {r['error']}")

#     except json.JSONDecodeError:
#         # Si la entrada no es JSON válido
#         print("Entrada JSON inválida. Por favor ingresa una lista válida de operaciones.")
#     except Exception as e:
#         # Cualquier otro error inesperado
#         print("Error:", str(e))

# # Cerrar la conexión con el servidor
# client_socket.close()
# print("[*] Conexión cerrada.")








# #!/usr/bin/env python3
import socket    # Para conexiones TCP/IP
import json      # Para manejar JSON
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.17.144.21', 5000))  # Cambia si es otro host

# Esperar la petición de nombre del servidor
server_msg = client_socket.recv(1024).decode("utf-8")
print("Servidor:", server_msg)

# Enviar nombre del cliente
name = input("Tu nombre: ").strip()
if not name:
    name = "Desconocido"
client_socket.sendall(name.encode("utf-8"))

print("[*] Conectado al servidor. Puedes enviar operaciones o mensajes.")
print("Envía operaciones en JSON o mensajes para chatbot.")
print("Ejemplo operaciones: [{\"n1\":5,\"n2\":3,\"op\":\"add\"}]")
print("Escribe 'quit' para salir.")

while True:
    user_input = input(">>> ").strip()

    if user_input.lower() == "quit":
        client_socket.sendall("quit".encode("utf-8"))
        break

    try:
        json_data = json.loads(user_input)
        client_socket.sendall(json.dumps(json_data).encode("utf-8"))
        response = client_socket.recv(4096).decode("utf-8")
        results = json.loads(response)
        print("Respuesta del servidor:")
        for i, r in enumerate(results):
            if "result" in r:
                print(f"  Operación {i+1}: RESULTADO = {r['result']}")
            else:
                print(f"  Operación {i+1}: ERROR = {r['error']}")
    except json.JSONDecodeError:
        client_socket.sendall(user_input.encode("utf-8"))
        response = client_socket.recv(4096).decode("utf-8")
        print("Chatbot responde:", response)

client_socket.close()
print("[*] Conexión cerrada.")
import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.17.144.21', 5000))  # Cambia si es otro host

# Esperar la petición de nombre del servidor
server_msg = client_socket.recv(1024).decode("utf-8")
print("Servidor:", server_msg)

# Enviar nombre del cliente
name = input("Tu nombre: ").strip()
if not name:
    name = "Desconocido"
client_socket.sendall(name.encode("utf-8"))

print("[*] Conectado al servidor. Puedes enviar operaciones o mensajes.")
print("Envía operaciones en JSON o mensajes para chatbot.")
print("Ejemplo operaciones: [{\"n1\":5,\"n2\":3,\"op\":\"add\"}]")
print("Escribe 'quit' para salir.")

while True:
    user_input = input(">>> ").strip()

    if user_input.lower() == "quit":
        client_socket.sendall("quit".encode("utf-8"))
        break

    try:
        json_data = json.loads(user_input)
        client_socket.sendall(json.dumps(json_data).encode("utf-8"))
        response = client_socket.recv(4096).decode("utf-8")
        results = json.loads(response)
        print("Respuesta del servidor:")
        for i, r in enumerate(results):
            if "result" in r:
                print(f"  Operación {i+1}: RESULTADO = {r['result']}")
            else:
                print(f"  Operación {i+1}: ERROR = {r['error']}")
    except json.JSONDecodeError:
        client_socket.sendall(user_input.encode("utf-8"))
        response = client_socket.recv(4096).decode("utf-8")
        print("Chatbot responde:", response)

client_socket.close()
print("[*] Conexión cerrada.")