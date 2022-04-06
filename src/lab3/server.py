import socket as socket_util

from src.lab2.repository.PolygonRepositorySQLite import PolygonRepositorySQLite
from src.lab2.repository.VertexRepositorySQLite import VertexRepositorySQLite
from src.lab3.const import *
from src.lab3.converters import to_json, from_json

socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(10)

polygon_repository = PolygonRepositorySQLite()
vertex_repository = VertexRepositorySQLite()


def process(data: str) -> str:
    split = data.split()
    if split[0] == "find_polygon_by_id":
        return to_json(polygon_repository.find_polygon_by_id(split[1]))
    if split[0] == "find_all_polygons":
        return to_json(polygon_repository.find_all_polygons())
    if split[0] == "add_polygon":
        return to_json(polygon_repository.add_polygon(from_json(split[1])))
    if split[0] == "delete_polygon_by_id":
        return to_json(polygon_repository.delete_polygon_by_id(split[1]))

    if split[0] == "find_vertex_by_id":
        return to_json(vertex_repository.find_vertex_by_id(split[1]))
    if split[0] == "find_all_vertex_in_polygon":
        return to_json(vertex_repository.find_all_vertex_in_polygon(split[1]))
    if split[0] == "add_vertex_to_polygon_by_id":
        return to_json(vertex_repository.add_vertex_to_polygon_by_id(split[1], from_json(split[2])))
    if split[0] == "update_vertex_by_id":
        return to_json(vertex_repository.update_vertex_by_id(split[1], split[2], split[3]))
    if split[0] == "delete_vertex_by_id":
        return to_json(vertex_repository.delete_vertex_by_id(split[1]))


while True:
    connection, _ = socket.accept()
    request = connection.recv(BUFFER_SIZE)
    request_str: str = request.decode(ENCODING)
    print("request = " + request_str)
    response_str = process(request_str)
    print("response = " + response_str)
    print()
    response = response_str.encode(ENCODING)
    connection.send(response)
    connection.close()
