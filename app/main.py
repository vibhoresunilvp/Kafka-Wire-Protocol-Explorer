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
    # 1. Extract correlation_id
    correlation_id = data[8:12]

    # 2. Response body
    error_code = (0).to_bytes(2, "big")

    api_keys_array_len = b"\x02"          # 1 element → 1 + 1
    api_key = (18).to_bytes(2, "big")
    min_version = (0).to_bytes(2, "big")
    max_version = (4).to_bytes(2, "big")
    api_key_tag_buffer = b"\x00"

    throttle_time_ms = (0).to_bytes(4, "big")
    response_tag_buffer = b"\x00"

    body = (
        error_code +
        api_keys_array_len +
        api_key +
        min_version +
        max_version +
        api_key_tag_buffer +
        throttle_time_ms +
        response_tag_buffer
    )

    # 3. message_size = header + body
    message_size = (len(correlation_id) + len(body)).to_bytes(4, "big")

    return message_size + correlation_id + body

def main():
    print("Logs from your program will appear here!")
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, _ = server.accept() # wait for client
    data = connection.recv(1024)
    connection.sendall(parse_response(data))


if __name__ == "__main__":
    main()
