from typing import Optional

from src.common_data.entity.Vertex import Vertex
from src.lab2.SqlService import SqlService
from src.common_data.repository.VertexRepository import VertexRepository


class VertexRepositorySQLite(VertexRepository):
    def find_vertex_by_id(self, _id: str) -> Optional[Vertex]:
        return SqlService.sql_get_element(
            lambda row: Vertex(row[0], row[1], row[2]),
            "SELECT id, x, y, polygon_id FROM vertex WHERE id = :search_id;",
            {"search_id": _id}
        )

    def find_all_vertex_in_polygon(self, polygon_id: str) -> [Vertex]:
        return SqlService.sql_get_list(
            lambda row: Vertex(row[0], row[1], row[2]),
            "SELECT id, x, y, polygon_id FROM vertex WHERE polygon_id = :polygon_id;",
            {"polygon_id": polygon_id}
        )

    def add_vertex_to_polygon_by_id(self, _id: str, vertex: Vertex) -> None:
        SqlService.sql_execute(
            "INSERT INTO vertex VALUES (:id, :x, :y, :polygon_id);",
            {"id": vertex.id, "x": vertex.x, "y": vertex.y, "polygon_id": _id})

    def update_vertex_by_id(self, _id: str, new_x: str, new_y: str) -> None:
        SqlService.sql_execute(
            "UPDATE vertex SET x = :x, y = :y WHERE id = :id;",
            {"id": _id, "x": new_x, "y": new_y})

    def delete_vertex_by_id(self, _id: str) -> None:
        SqlService.sql_execute(
            "DELETE FROM vertex WHERE id = :id;",
            {"id": _id})
