import socket as socket_util

from src.lab3.const import *


def send(request: str) -> str:
    socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
    socket.connect((HOST, PORT))
    socket.send(request.encode(ENCODING))
    result = socket.recv(BUFFER_SIZE).decode(ENCODING)
    socket.close()
    return result
