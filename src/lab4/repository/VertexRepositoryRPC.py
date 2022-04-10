import xmlrpc.client
from typing import Optional

from src.common_data.entity.Vertex import Vertex
from src.common_data.repository.VertexRepository import VertexRepository
from src.lab3.converters import from_json, to_json
from src.lab4.const import HOST, PORT

s = xmlrpc.client.ServerProxy('http://' + HOST + ':' + PORT.__str__())


class VertexRepositoryRPC(VertexRepository):
    def find_vertex_by_id(self, _id: str) -> Optional[Vertex]:
        return s.find_vertex_by_id(_id)

    def find_all_vertex_in_polygon(self, polygon_id: str) -> [Vertex]:
        return s.find_all_vertex_in_polygon(polygon_id)

    def add_vertex_to_polygon_by_id(self, _id: str, vertex: Vertex) -> None:
        return from_json(s.add_vertex_to_polygon_by_id_json(_id, to_json(vertex)))

    def update_vertex_by_id(self, _id: str, new_x: str, new_y: str) -> None:
        return s.update_vertex_by_id(_id, new_x, new_y)

    def delete_vertex_by_id(self, _id: str) -> None:
        return s.delete_vertex_by_id(_id)
