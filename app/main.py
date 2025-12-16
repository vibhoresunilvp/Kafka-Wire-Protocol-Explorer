import socket  # noqa: F401
from threading import Thread

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
    print(f"message_size: {int.from_bytes(message_size, 'big')}")
    print(f"correlation_id: {correlation_id}")
    print(f"error_code: {error_code}")
    print(f"api_keys_array_len: {api_keys_array_len}")
    print(f"api_key: {api_key}")
    print(f"min_version: {min_version}")
    print(f"max_version: {max_version}")
    print(f"api_key_tag_buffer: {api_key_tag_buffer}")
    print(f"throttle_time_ms: {throttle_time_ms}")
    print(f"response_tag_buffer: {response_tag_buffer}")

    return message_size + correlation_id + body

def handle_client(connection, addr):
    try:
        while True:
            data = connection.recv(1024)
            if(not data):
                break
            connection.sendall(parse_response(data))
    except Exception as exception:
        print("No Data")
    finally:
        connection.close()

def main():
    print("Logs from your program will appear here!")
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    server.listen()
    while True:
        connection, addr = server.accept()
    
        thread = Thread(target=handle_client, args=(connection, addr), daemon=True)
        thread.start()

if __name__ == "__main__":
    main()
