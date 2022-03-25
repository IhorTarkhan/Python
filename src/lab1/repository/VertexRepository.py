from typing import Optional

from src.lab1.XmlService import XmlService
from src.entity.Polygon import Polygon
from src.entity.Vertex import Vertex


class VertexRepository:
    @staticmethod
    def find_vertex_by_id(_id: str) -> Optional[Vertex]:
        return XmlService.get_vertex_by_id(_id)

    @staticmethod
    def find_all_vertex_in_polygon(polygon_id: str) -> [Vertex]:
        return XmlService.get_all_vertexes_by_polygon_id(polygon_id)

    @staticmethod
    def add_vertex_to_polygon_by_id(_id: str, vertex: Vertex) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            if polygon.id == _id:
                polygon.points.append(vertex)
        XmlService.save_all(polygons)

    @staticmethod
    def update_vertex_by_id(_id: str, new_x: str, new_y: str) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            for vertex in polygon.points:
                if vertex.id == _id:
                    vertex.x = new_x
                    vertex.y = new_y
        XmlService.save_all(polygons)

    @staticmethod
    def delete_vertex_by_id(_id: str) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            deleted_element = None
            for vertex in polygon.points:
                if vertex.id == _id:
                    deleted_element = vertex
            if deleted_element is not None:
                polygon.points.remove(deleted_element)
        XmlService.save_all(polygons)
