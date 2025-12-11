import socket  # noqa: F401

# Task 4: Handle ApiVersions requests

# Request Header (v2)
#     [0, 4] -> message size
#     [4, 6] -> Api key
#     [6, 8] -> api version
#     [8, 12] -> correlation id
#     [12, 14] -> client id length
#     [14, 23] -> client id contents
#     [23, 24] -> tag buffer




def parse_response(data) -> bytes:
    correlation_id = data[8:12]
    api_version = data[6:8]
    error_code = 35
    api_version_hex = int.from_bytes(api_version, "big")
    print(f"api_version: {api_version_hex}")
    if(0 <= api_version_hex <= 4):
        error_code = 0
    error_code = error_code.to_bytes(2, "big")
    print(f"error_code: {int.from_bytes(error_code, "big")}")
    print(f"correlation_id: {int.from_bytes(correlation_id, "big")}")
    print(f"error_code: {int.from_bytes(error_code, "big")}")

    message_size = (0).to_bytes(4, byteorder="big")
    return message_size+correlation_id+error_code+message_size

def main():
    print("Logs from your program will appear here!")
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, _ = server.accept() # wait for client
    data = connection.recv(1024)
    connection.sendall(parse_response(data))


if __name__ == "__main__":
    main()
