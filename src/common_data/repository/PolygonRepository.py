from typing import Optional

from src.common_data.entity.Polygon import Polygon


class PolygonRepository:
    def find_polygon_by_id(self, _id: str) -> Optional[Polygon]:
        pass

    def find_all_polygons(self) -> [Polygon]:
        pass

    def add_polygon(self, polygon: Polygon) -> bool:
        pass

    def delete_polygon_by_id(self, _id: str) -> bool:
        pass
