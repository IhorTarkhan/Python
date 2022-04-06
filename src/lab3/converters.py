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
