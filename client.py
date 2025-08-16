import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ").strip() or "Anonymous"
client.sendall(name.encode())

stop_event = threading.Event()

def recv_loop():
    try:
        while not stop_event.is_set():
            data = client.recv(1024)
            if not data:
                print("\n[Disconnected by server]")
                stop_event.set()
                break
            print(data.decode(), end="")
    except Exception as e:
        if not stop_event.is_set():
            print(f"\n[Receive error: {e}]")
        stop_event.set()

threading.Thread(target=recv_loop, daemon=True).start()

try:
    while not stop_event.is_set():
        msg = input("You: ")
        if msg.strip().lower() in {"exit", "/exit", "/quit"}:
            stop_event.set()
            break
        try:
            client.sendall((msg + "\n").encode())
        except Exception as e:
            print(f"[Send error: {e}]")
            stop_event.set()
            break
except KeyboardInterrupt:
    pass
finally:
    try:
        client.shutdown(socket.SHUT_RDWR)
    except Exception:
        pass
    client.close()
