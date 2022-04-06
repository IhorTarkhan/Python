from typing import Optional

from src.common_data.entity.Vertex import Vertex
from src.lab3.client import send
from src.lab3.converters import from_json, to_json
from src.common_data.repository.VertexRepository import VertexRepository


class VertexRepositorySocket(VertexRepository):
    def find_vertex_by_id(self, _id: str) -> Optional[Vertex]:
        return from_json(send("find_vertex_by_id " + _id))

    def find_all_vertex_in_polygon(self, polygon_id: str) -> [Vertex]:
        return from_json(send("find_all_vertex_in_polygon " + polygon_id))

    def add_vertex_to_polygon_by_id(self, _id: str, vertex: Vertex) -> None:
        return from_json(send("add_vertex_to_polygon_by_id " + _id + " " + to_json(vertex)))

    def update_vertex_by_id(self, _id: str, new_x: str, new_y: str) -> None:
        return from_json(send("update_vertex_by_id " + _id + " " + new_x + " " + new_y))

    def delete_vertex_by_id(self, _id: str) -> None:
        return from_json(send("delete_vertex_by_id " + _id))
