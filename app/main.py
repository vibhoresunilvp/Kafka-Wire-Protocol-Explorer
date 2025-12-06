import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept() # wait for client
    data = connection.recv(1024)
    correlation_id = 7
    print(data)
    message_val = len(data).to_bytes(4, byteorder="big")
    correlation_val = correlation_id.to_bytes(4, byteorder="big")
    data = message_val+correlation_val
    print(data.hex())
    connection.sendall(data)


if __name__ == "__main__":
    main()
