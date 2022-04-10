from typing import Optional

from src.common_data.entity.Polygon import Polygon
from src.common_data.entity.Vertex import Vertex
from src.lab1.XmlService import XmlService
from src.common_data.repository.VertexRepository import VertexRepository


class VertexRepositoryXml(VertexRepository):
    def find_vertex_by_id(self, _id: str) -> Optional[Vertex]:
        return XmlService.get_vertex_by_id(_id)

    def find_all_vertex_in_polygon(self, polygon_id: str) -> [Vertex]:
        return XmlService.get_all_vertexes_by_polygon_id(polygon_id)

    def add_vertex_to_polygon_by_id(self, _id: str, vertex: Vertex) -> bool:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            if polygon.id == _id:
                polygon.points.append(vertex)
        XmlService.save_all(polygons)
        return True

    def update_vertex_by_id(self, _id: str, new_x: str, new_y: str) -> bool:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            for vertex in polygon.points:
                if vertex.id == _id:
                    vertex.x = new_x
                    vertex.y = new_y
        XmlService.save_all(polygons)
        return True

    def delete_vertex_by_id(self, _id: str) -> bool:
        polygons: [Polygon] = XmlService.get_all_polygons()
        for polygon in polygons:
            deleted_element = None
            for vertex in polygon.points:
                if vertex.id == _id:
                    deleted_element = vertex
            if deleted_element is not None:
                polygon.points.remove(deleted_element)
        XmlService.save_all(polygons)
        return True
