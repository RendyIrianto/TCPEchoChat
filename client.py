import socket
import threading

HOST = "127.0.0.1"

PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

name = input("Enter your name: ")

client.sendall(name.encode())

def user_message():
    message = input("You: ")
    if message.lower() == "exit":
        return "Goodbye"
    else:
        return message 

while True:
    thread = threading.Thread(target=user_message)
    thread.start()
    client.sendall(message.encode())
    data = client.recv(1024)
    print(data.decode())

client.close()