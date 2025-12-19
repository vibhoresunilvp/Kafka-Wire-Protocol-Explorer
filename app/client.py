def handle(client):
    try:
        while True:
            request = client.recv(1024)
            if not request:
                client.close()
                break
            else:
                response = create_api_version_response(request)
                client.sendall(response)
    except Exception as e:
        print(f"Error {e}")

def create_api_version_response(request):
    message = Message.from_bytes(request)
    request_api_version = message.header.request_api_version
    request_api_key = message.header.request_api_key
    correlation_id = message.header.correlation_id

    if request_api_version > 4: 
        error_code = 35
    else:
        error_code = 0
    
    api_version = ApiVersion(qpi_key=request_api_key, min_version=0)
    api_version_array = ApiVersionArray(api_versions=[api_version])
    api_version_response = ApiVersionResponse(
        header=ResponseHeader(correlation_id=correlation_id),
        body=ApiVersionResponeBody(
            error_code=error_code,
            api_version=api_version_array
        )
    )
    return create_api_version_response
    
