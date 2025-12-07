import socket  # noqa: F401

def parse_response(data) -> bytes:
    message_size = "00000000"
    correlation_id = data[8:12]

    return bytes.fromhex(message_size + correlation_id)

def main():
    print("Logs from your program will appear here!")
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, _ = server.accept() # wait for client
    data = connection.recv(1024)
    print(int.from_bytes(data[8:12], byteorder="big"))
    connection.sendall(parse_response(data))


if __name__ == "__main__":
    main()
