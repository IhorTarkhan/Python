from typing import Optional

from src.entity.Polygon import Polygon
from src.entity.Vertex import Vertex
from src.lab2.SqlService import SqlService
from src.repository.PolygonRepository import PolygonRepository


def fill_polygons_by_vertexes(polygons, row):
    for polygon in polygons:
        if polygon.id == row[3]:
            polygon.points.append(Vertex(row[0], row[1], row[2]))


class PolygonRepositorySQLite(PolygonRepository):
    def find_polygon_by_id(self, _id: str) -> Optional[Polygon]:
        vertexes = SqlService.sql_get_list(
            lambda row: Vertex(row[0], row[1], row[2]),
            "SELECT id, x, y, polygon_id FROM vertex WHERE polygon_id = :search_id;",
            {"search_id": _id})
        return SqlService.sql_get_element(
            lambda row: Polygon(row[0], vertexes),
            "SELECT id FROM polygon WHERE id = :search_id;",
            {"search_id": _id})

    def find_all_polygons(self) -> [Polygon]:
        polygons = SqlService.sql_get_list(
            lambda row: Polygon(row[0]),
            "SELECT id FROM polygon;")

        SqlService.sql_get_list(
            lambda row: fill_polygons_by_vertexes(polygons, row),
            "SELECT id, x, y, polygon_id FROM vertex;")

        return polygons

    def add_polygon(self, polygon: Polygon) -> None:
        SqlService.sql_execute(
            "INSERT INTO polygon VALUES (:id);",
            {"id": polygon.id})

    def delete_polygon_by_id(self, _id: str) -> None:
        SqlService.sql_execute(
            "DELETE FROM polygon WHERE id = :id;",
            {"id": _id})
