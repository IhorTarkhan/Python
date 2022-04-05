import json
import socket as socket_util

from src.entity.Vertex import Vertex

HOST = 'localhost'
PORT = 55000
ENCODING = 'UTF-8'

socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
data = Vertex("1213", "12", "13")

socket.connect((HOST, PORT))
request_str: str = json.dumps(data.__dict__)
request: bytes = request_str.encode(ENCODING)
socket.send(request)
response: bytes = socket.recv(1024)
response_str = response.decode(ENCODING)
socket.close()

print(response_str)
loads: Vertex = json.loads(response_str)
print(loads["id"])
