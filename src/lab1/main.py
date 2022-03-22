from src.lab1.XmlService import XmlService

XmlService.dtd_validate()

print(XmlService.get_all_polygons())
print(XmlService.get_polygon_by_id("1"))
print(XmlService.get_all_vertexes_by_polygon_id("1"))
print(XmlService.get_vertex_by_id("1"))

XmlService.save_all(XmlService.get_all_polygons())
