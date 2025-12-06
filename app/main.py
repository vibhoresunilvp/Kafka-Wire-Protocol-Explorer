import socket  # noqa: F401

def parse_response() -> bytes:
    message_size = "00000000"
    correlation_id = "00000007"

    return bytes.fromhex(message_size + correlation_id)

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, _ = server.accept() # wait for client
    connection.sendall(parse_response())


if __name__ == "__main__":
    main()
