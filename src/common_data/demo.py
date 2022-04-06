from src.common_data.entity.Polygon import Polygon
from src.common_data.entity.Vertex import Vertex
from src.common_data.repository.PolygonRepository import PolygonRepository
from src.common_data.repository.VertexRepository import VertexRepository

polygons = None
vertexes = None


def polygons_demo(polygon_repository: PolygonRepository):
    global polygons
    print("All polygons:")
    polygons = polygon_repository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()

    print("Polygon with id 2:")
    print(polygon_repository.find_polygon_by_id("2"))
    print()

    new_polygon = Polygon("3", [Vertex("6", "4.3", "17.0")])
    print(f"Added polygon {new_polygon}, result after:")
    polygon_repository.add_polygon(new_polygon)
    polygons = polygon_repository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()

    print("Deleted polygon with id=3:")
    polygon_repository.delete_polygon_by_id("3")
    polygons = polygon_repository.find_all_polygons()
    print(f"length={len(polygons)}: {polygons}")
    print()


def vertexes_demo(polygon_repository: PolygonRepository, vertex_repository: VertexRepository):
    global vertexes
    print("All vertexes in polygon with id=2:")
    vertexes = vertex_repository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()

    print("Vertex with id 5:")
    print(vertex_repository.find_vertex_by_id("5"))
    print()

    new_vertex = Vertex("6", "4.3", "17.0")
    print(f"Added vertex {new_vertex} to polygon with id=2, result after:")
    vertex_repository.add_vertex_to_polygon_by_id("2", new_vertex)
    print(polygon_repository.find_polygon_by_id("2"))
    vertexes = vertex_repository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()

    print("Before update vertex with id=6:")
    print(vertex_repository.find_vertex_by_id("6"))
    vertex_repository.update_vertex_by_id("6", "13.1", "-69.0")
    print("After update vertex with id=6:")
    print(vertex_repository.find_vertex_by_id("6"))
    print()

    print("Deleted vertex with id=6:")
    vertex_repository.delete_vertex_by_id("6")
    print(polygon_repository.find_polygon_by_id("2"))
    vertexes = vertex_repository.find_all_vertex_in_polygon("2")
    print(f"length={len(vertexes)}: {vertexes}")
    print()


def demo(polygon_repository: PolygonRepository, vertex_repository: VertexRepository):
    polygons_demo(polygon_repository)
    print("------------------------------")
    vertexes_demo(polygon_repository, vertex_repository)
