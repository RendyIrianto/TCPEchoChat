import socket 

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
conn, addr = server.accept()
print("Connected by", addr)


conn.close()
server.close()