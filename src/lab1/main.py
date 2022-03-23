from src.lab1.entity.Polygon import Polygon
from src.lab1.entity.Vertex import Vertex
from src.lab1.repository.PolygonRepository import PolygonRepository

polygons = None
if __name__ == "__main__":
    print("All polygons:")
    polygons = PolygonRepository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()

    print("Polygon with id 2:")
    print(PolygonRepository.find_polygon_by_id("2"))
    print()

    new_polygon = Polygon("3", [Vertex("10", "4.3", "17.0")])
    print(f"Added polygon {new_polygon}, result after:")
    PolygonRepository.add_polygon(new_polygon)
    polygons = PolygonRepository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()
