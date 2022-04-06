import socket as socket_util

from src.lab3.converters import *

HOST = 'localhost'
PORT = 55000
ENCODING = 'UTF-8'
BUFFER_SIZE = 1024

data = Vertex("1213", "12", "13")


def send(request: str) -> str:
    socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
    socket.connect((HOST, PORT))
    socket.send(request.encode(ENCODING))
    result = socket.recv(BUFFER_SIZE).decode(ENCODING)
    socket.close()
    return result


response = send(to_json_vertex(data))
print(response)
print(from_json_vertex(response))
