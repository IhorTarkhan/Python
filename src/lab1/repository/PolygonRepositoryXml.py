from typing import Optional

from src.common_data.entity.Polygon import Polygon
from src.lab1.XmlService import XmlService
from src.common_data.repository.PolygonRepository import PolygonRepository


class PolygonRepositoryXml(PolygonRepository):
    def find_polygon_by_id(self, _id: str) -> Optional[Polygon]:
        return XmlService.get_polygon_by_id(_id)

    def find_all_polygons(self) -> [Polygon]:
        return XmlService.get_all_polygons()

    def add_polygon(self, polygon: Polygon) -> None:
        polygons: [Polygon] = XmlService.get_all_polygons()
        polygons.append(polygon)
        XmlService.save_all(polygons)

    def delete_polygon_by_id(self, _id: str) -> None:
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
