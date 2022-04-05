import socket as socket_util

HOST = 'localhost'
PORT = 55000
ENCODING = 'UTF-8'

socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(10)


def process(request: str):
    return request


while True:
    connection, _ = socket.accept()
    request = connection.recv(1024)
    request_str: str = request.decode(ENCODING)
    response_str = process(request_str)
    response = request_str.encode(ENCODING)
    connection.send(response)
conn.close()
