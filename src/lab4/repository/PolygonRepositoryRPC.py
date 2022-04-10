import xmlrpc.client
from typing import Optional

from src.common_data.entity.Polygon import Polygon
from src.common_data.repository.PolygonRepository import PolygonRepository
from src.lab3.converters import from_json, to_json
from src.lab4.const import HOST, PORT

s = xmlrpc.client.ServerProxy('http://' + HOST + ':' + PORT.__str__())


class PolygonRepositoryRPC(PolygonRepository):
    def find_polygon_by_id(self, _id: str) -> Optional[Polygon]:
        return s.find_polygon_by_id(_id)

    def find_all_polygons(self) -> [Polygon]:
        return s.find_all_polygons()

    def add_polygon(self, polygon: Polygon) -> bool:
        return from_json(s.add_polygon_json(to_json(polygon)))

    def delete_polygon_by_id(self, _id: str) -> bool:
        return s.delete_polygon_by_id(_id)
