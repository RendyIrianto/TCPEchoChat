import socket
import threading

HOST = "127.0.0.1"

PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

name = input("Enter your name:")

client.sendall(name.encode())

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Goodbye")
        break
    client.sendall(message.encode())
    data = client.recv(1024)
    print("Server echoed:", data.decode())

client.close()