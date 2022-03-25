from src.entity.Polygon import Polygon
from src.entity.Vertex import Vertex
from src.lab1.repository.PolygonRepository import PolygonRepository
from src.lab1.repository.VertexRepository import VertexRepository

polygons = None
vertexes = None


def polygons_demo():
    global polygons
    print("All polygons:")
    polygons = PolygonRepository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()

    print("Polygon with id 2:")
    print(PolygonRepository.find_polygon_by_id("2"))
    print()

    new_polygon = Polygon("3", [Vertex("6", "4.3", "17.0")])
    print(f"Added polygon {new_polygon}, result after:")
    PolygonRepository.add_polygon(new_polygon)
    polygons = PolygonRepository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()

    print("Deleted polygon with id=3:")
    PolygonRepository.delete_polygon_by_id("3")
    polygons = PolygonRepository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()


def vertexes_demo():
    global vertexes
    print("All vertexes in polygon with id=2:")
    vertexes = VertexRepository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()

    print("Vertex with id 5:")
    print(VertexRepository.find_vertex_by_id("5"))
    print()

    new_vertex = Vertex("6", "4.3", "17.0")
    print(f"Added vertex {new_vertex} to polygon with id=2, result after:")
    VertexRepository.add_vertex_to_polygon_by_id("2", new_vertex)
    print(PolygonRepository.find_polygon_by_id("2"))
    vertexes = VertexRepository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()

    print("Before update vertex with id=6:")
    print(VertexRepository.find_vertex_by_id("6"))
    VertexRepository.update_vertex_by_id("6", "13.1", "-69.0")
    print("After update vertex with id=6:")
    print(VertexRepository.find_vertex_by_id("6"))
    print()

    print("Deleted vertex with id=6:")
    VertexRepository.delete_vertex_by_id("6")
    print(PolygonRepository.find_polygon_by_id("2"))
    vertexes = VertexRepository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()


if __name__ == "__main__":
    polygons_demo()
    print("------------------------------")
    vertexes_demo()
