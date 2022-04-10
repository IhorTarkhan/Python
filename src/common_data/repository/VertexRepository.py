from typing import Optional

from src.common_data.entity.Vertex import Vertex


class VertexRepository:
    def find_vertex_by_id(self, _id: str) -> Optional[Vertex]:
        pass

    def find_all_vertex_in_polygon(self, polygon_id: str) -> [Vertex]:
        pass

    def add_vertex_to_polygon_by_id(self, _id: str, vertex: Vertex) -> bool:
        pass

    def update_vertex_by_id(self, _id: str, new_x: str, new_y: str) -> bool:
        pass

    def delete_vertex_by_id(self, _id: str) -> bool:
        pass
