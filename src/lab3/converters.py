import json

from src.entity.Polygon import Polygon
from src.entity.Vertex import Vertex


def __polygon_to_dictionary(p: Polygon) -> dict:
    _data = p.__dict__
    _data["points"] = list(map(lambda x: x.__dict__, p.points))
    return _data


def to_json_vertex(data: Vertex) -> str:
    return json.dumps(data.__dict__)


def to_json_polygon(data: Polygon) -> str:
    return json.dumps(__polygon_to_dictionary(data))


def to_json_vertex_list(data: [Vertex]) -> str:
    return json.dumps(list(map(lambda x: x.__dict__, data)))


def to_json_polygon_list(data: [Polygon]) -> str:
    dictionary_data = list(map(__polygon_to_dictionary, data))
    return json.dumps(dictionary_data)


def from_json_vertex(data: str) -> Vertex:
    pass


def from_json_polygon(data: str) -> Polygon:
    pass


def from_json_vertex_list(data: str) -> [Vertex]:
    pass


def from_json_polygon_list(data: str) -> [Polygon]:
    pass


vertex_json_1 = to_json_vertex(Vertex("1", "2", "3"))
polygon_json_1 = to_json_polygon(Polygon("1"))
polygon_json_2 = to_json_polygon(Polygon("1", [Vertex("1", "2", "3"), Vertex("1", "2", "3")]))
vertex_list_json_1 = to_json_vertex_list([Vertex("1", "2", "3"), Vertex("1", "2", "3")])
polygon_list_json_1 = to_json_polygon_list([Polygon("1", [Vertex("1", "2", "3"), Vertex("1", "2", "3")]), Polygon("1")])

print(vertex_json_1)
print(polygon_json_1)
print(polygon_json_2)
print(vertex_list_json_1)
print(polygon_list_json_1)
