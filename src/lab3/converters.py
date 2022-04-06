import json

from src.common_data.entity.Polygon import Polygon
from src.common_data.entity.Vertex import Vertex


def __polygon_to_dictionary(data: Polygon) -> dict:
    response = data.__dict__
    response["points"] = list(map(lambda x: x.__dict__, data.points))
    return response


def __vertex_from_dictionary(data: dict) -> Vertex:
    return Vertex(data["id"], data["x"], data["y"])


def __polygon_from_dictionary(data: dict) -> Polygon:
    return Polygon(data["id"], list(map(__vertex_from_dictionary, data["points"])))


def _to_json_vertex(data: Vertex) -> str:
    return json.dumps(data.__dict__)


def _to_json_polygon(data: Polygon) -> str:
    return json.dumps(__polygon_to_dictionary(data))


def _to_json_vertex_list(data: [Vertex]) -> str:
    return json.dumps(list(map(lambda x: x.__dict__, data)))


def _to_json_polygon_list(data: [Polygon]) -> str:
    dictionary_data = list(map(__polygon_to_dictionary, data))
    return json.dumps(dictionary_data)


def _from_json_vertex(data: str) -> Vertex:
    loads: dict = json.loads(data)
    return __vertex_from_dictionary(loads)


def _from_json_polygon(data: str) -> Polygon:
    loads: dict = json.loads(data)
    return __polygon_from_dictionary(loads)


def _from_json_vertex_list(data: str) -> [Vertex]:
    loads: list = json.loads(data)
    return list(map(__vertex_from_dictionary, loads))


def _from_json_polygon_list(data: str) -> [Polygon]:
    loads: list = json.loads(data)
    return list(map(__polygon_from_dictionary, loads))


def to_json(data) -> str:
    if data is None:
        return "None"
    if type(data) is Vertex:
        return _to_json_vertex(data).replace(" ", "")
    if type(data) is Polygon:
        return _to_json_polygon(data).replace(" ", "")
    if type(data) is list:
        if type(data[0]) is Vertex:
            return _to_json_vertex_list(data).replace(" ", "")
        if type(data[0]) is Polygon:
            return _to_json_polygon_list(data).replace(" ", "")


def from_json(data: str):
    if data == "None":
        return None
    loads = json.loads(data)
    if type(loads) is dict:
        try:
            return _from_json_vertex(data)
        except KeyError:
            pass
        try:
            return _from_json_polygon(data)
        except KeyError:
            pass
    if type(loads) is list:
        try:
            return _from_json_vertex_list(data)
        except KeyError:
            pass
        try:
            return _from_json_polygon_list(data)
        except KeyError:
            pass
