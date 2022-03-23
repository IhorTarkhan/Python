from src.lab1.XmlService import XmlService
from src.lab1.entity.Polygon import Polygon
from src.lab1.entity.Vertex import Vertex

XmlService.dtd_validate()

print(XmlService.get_all_polygons())
print(XmlService.get_polygon_by_id("1"))
print(XmlService.get_all_vertexes_by_polygon_id("1"))
print(XmlService.get_vertex_by_id("1"))

XmlService.save_all(XmlService.get_all_polygons())


def find_all_polygons() -> [Polygon]:
    return XmlService.get_all_polygons()


def save_all_polygon(polygons: [Polygon]) -> None:
    XmlService.save_all(polygons)


def add_polygon(polygon: Polygon) -> None:
    polygons: [Polygon] = XmlService.get_all_polygons()
    polygons.append(polygon)
    XmlService.save_all(polygons)


def add_vertex_to_polygon_by_id(_id: str, vertex: Vertex) -> None:
    polygons: [Polygon] = XmlService.get_all_polygons()
    for polygon in polygons:
        if polygon.id == _id:
            polygon.points.append(vertex)
    XmlService.save_all(polygons)


def update_vertex_by_id(_id: str, new_x: str, new_y: str) -> None:
    polygons: [Polygon] = XmlService.get_all_polygons()
    for polygon in polygons:
        for vertex in polygon.points:
            if vertex.id == _id:
                vertex.x = new_x
                vertex.y = new_y
    XmlService.save_all(polygons)


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


update_vertex_by_id("1", "14", "41")
