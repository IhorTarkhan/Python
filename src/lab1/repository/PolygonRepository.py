from typing import Optional

from src.lab1.XmlService import XmlService
from src.lab1.entity.Polygon import Polygon


class PolygonRepository:
    @staticmethod
    def find_polygon_by_id(_id: str) -> Optional[Polygon]:
        return XmlService.get_polygon_by_id(_id)

    @staticmethod
    def find_all_polygons() -> [Polygon]:
        return XmlService.get_all_polygons()

    @staticmethod
    def save_all_polygon(polygons: [Polygon]) -> None:
        XmlService.save_all(polygons)

    @staticmethod
    def add_polygon(polygon: Polygon) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        polygons.append(polygon)
        XmlService.save_all(polygons)

    @staticmethod
    def delete_polygon_by_id(_id: str) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        deleted_element = None
        for polygon in polygons:
            if polygon.id == _id:
                deleted_element = polygon
        if deleted_element is not None:
            polygons.remove(deleted_element)
        else:
            raise KeyError("can not found polygon with id " + _id)
        XmlService.save_all(polygons)
