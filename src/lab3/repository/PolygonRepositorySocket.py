from typing import Optional

from src.common_data.entity.Polygon import Polygon
from src.lab3.client import send
from src.lab3.converters import from_json, to_json
from src.common_data.repository.PolygonRepository import PolygonRepository


class PolygonRepositorySocket(PolygonRepository):
    def find_polygon_by_id(self, _id: str) -> Optional[Polygon]:
        return from_json(send("find_polygon_by_id " + _id))

    def find_all_polygons(self) -> [Polygon]:
        return from_json(send("find_all_polygons"))

    def add_polygon(self, polygon: Polygon) -> None:
        return from_json(send("add_polygon " + to_json(polygon)))

    def delete_polygon_by_id(self, _id: str) -> None:
        return from_json(send("delete_polygon_by_id " + _id))
