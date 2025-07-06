import socket 
import threading 

HOST = "127.0.0.1" 

PORT = 65432

clients = []

def handle_client(conn, addr):
    try:
        print(f"New connection from {addr}")
        while True:
            name = conn.recv(1024).decode
            print(name)
            if not name:
                break
            conn.sendall(name)

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        clients.remove(conn)
        conn.close()
        print(f"Connection with {addr} closed")



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is listening...")

try:
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(clients)
        
except KeyboardInterrupt:
    print("\nShutting down server...")
    server.close()
