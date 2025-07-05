import socket 
import threading 

HOST = "127.0.0.1" 

PORT = 65432

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()
    print(f"Connection with {addr} closed")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is listening...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
