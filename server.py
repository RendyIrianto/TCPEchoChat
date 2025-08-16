import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 65432

stop_event = threading.Event()

def recv_loop(sock: socket.socket) -> None:
    try:
        while not stop_event.is_set():
            data = sock.recv(1024)
            if not data:
                print("\n[Disconnected by server]")
                stop_event.set()
                break
            print(data.decode(), end="")
    except Exception as e:
        if not stop_event.is_set():
            print(f"\n[Receive error: {e}]")
        stop_event.set()

def main() -> None:
    name = input("Enter your name: ").strip() or "Anonymous"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except Exception as e:
            print(f"[Failed to connect to {HOST}:{PORT}: {e}]")
            sys.exit(1)

        try:
            s.sendall(name.encode())
        except Exception as e:
            print(f"[Failed to send name: {e}]")
            return

        t = threading.Thread(target=recv_loop, args=(s,), daemon=True)
        t.start()

        try:
            while not stop_event.is_set():
                msg = input()
                if msg.strip().lower() in {"exit", "/exit", "/quit"}:
                    stop_event.set()
                    break
                try:
                    s.sendall((msg + "\n").encode())
                except Exception as e:
                    print(f"[Send error: {e}]")
                    stop_event.set()
                    break
        except KeyboardInterrupt:
            stop_event.set()
        finally:
            try:
                s.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass

if __name__ == "__main__":
    main()