import socket
import threading
from app.client import handle

HOST = "localhost"
PORT = 9092

def main():
    print(f"Server started on {HOST} and {PORT}")
    try: 
        with socket.create_server(HOST, PORT, reuse_port=True) as server:
            while True:
                client, addr = server.accept()
                threading.Thread(target=handle, args=(client,), daemon=True).start()
    except Exception as e:
        print(f"Server error {e}")

if __name__ == "__main__":
    main()
