import json

from src.entity.Polygon import Polygon
from src.entity.Vertex import Vertex


def __polygon_to_dictionary(data: Polygon) -> dict:
    response = data.__dict__
    response["points"] = list(map(lambda x: x.__dict__, data.points))
    return response


def __vertex_from_dictionary(data: dict) -> Vertex:
    return Vertex(data["id"], data["x"], data["y"])


def __polygon_from_dictionary(data: dict) -> Polygon:
    return Polygon(data["id"], list(map(__vertex_from_dictionary, data["points"])))


def to_json_vertex(data: Vertex) -> str:
    return json.dumps(data.__dict__)


def to_json_polygon(data: Polygon) -> str:
    return json.dumps(__polygon_to_dictionary(data))


def to_json_vertex_list(data: [Vertex]) -> str:
    return json.dumps(list(map(lambda x: x.__dict__, data)))


def to_json_polygon_list(data: [Polygon]) -> str:
    dictionary_data = list(map(__polygon_to_dictionary, data))
    return json.dumps(dictionary_data)


def to_json(data) -> str:
    if type(data) is Vertex:
        return to_json_vertex(data)
    if type(data) is Polygon:
        return to_json_polygon(data)
    if type(data) is list:
        if type(data[0]) is Vertex:
            return to_json_vertex_list(data)
        if type(data[0]) is Polygon:
            return to_json_polygon_list(data)


def from_json_vertex(data: str) -> Vertex:
    loads: dict = json.loads(data)
    return __vertex_from_dictionary(loads)


def from_json_polygon(data: str) -> Polygon:
    loads: dict = json.loads(data)
    return __polygon_from_dictionary(loads)


def from_json_vertex_list(data: str) -> [Vertex]:
    loads: list = json.loads(data)
    return list(map(__vertex_from_dictionary, loads))


def from_json_polygon_list(data: str) -> [Polygon]:
    loads: list = json.loads(data)
    return list(map(__polygon_from_dictionary, loads))


def from_json(data: str):
    loads = json.loads(data)
    if type(loads) is dict:
        try:
            return from_json_vertex(data)
        except KeyError:
            pass
        try:
            return from_json_polygon(data)
        except KeyError:
            pass
    if type(loads) is list:
        try:
            return from_json_vertex_list(data)
        except KeyError:
            pass
        try:
            return from_json_polygon_list(data)
        except KeyError:
            pass


vertex_json_1 = to_json(Vertex("1", "2", "3"))
polygon_json_1 = to_json(Polygon("1"))
polygon_json_2 = to_json(Polygon("1", [Vertex("1", "2", "3"), Vertex("1", "2", "3")]))
vertex_list_json_1 = to_json([Vertex("1", "2", "3"), Vertex("1", "2", "3")])
polygon_list_json_1 = to_json([Polygon("1", [Vertex("1", "2", "3"), Vertex("1", "2", "3")]), Polygon("1")])

print(vertex_json_1)
print(polygon_json_1)
print(polygon_json_2)
print(vertex_list_json_1)
print(polygon_list_json_1)
print()
print(from_json(vertex_json_1))
print(from_json(polygon_json_1))
print(from_json(polygon_json_2))
print(from_json(vertex_list_json_1))
print(from_json(polygon_list_json_1))
