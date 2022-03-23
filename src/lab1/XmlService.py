from typing import Optional
from xml.dom.minidom import Document
from xml.dom.minidom import Element
from xml.dom.minidom import parse

from lxml import etree
from lxml.etree import XMLSyntaxError

from src.lab1.entity.Polygon import Polygon
from src.lab1.entity.Vertex import Vertex


class XmlService:
    XML_FILE: str = "resources/sample.xml"
    DOCUMENT_PREFIX: str = '<!DOCTYPE geometry SYSTEM "sample.dtd" >'

    @staticmethod
    def __dtd_validate() -> None:
        parser = etree.XMLParser(dtd_validation=True)
        try:
            etree.parse(XmlService.XML_FILE, parser)
        except XMLSyntaxError as e:
            print(e)
            raise e

    @staticmethod
    def get_all_polygons() -> [Polygon]:
        XmlService.__dtd_validate()
        result: [Polygon] = []
        with parse(XmlService.XML_FILE) as dom:
            dom: Document = dom
            for polygon in dom.getElementsByTagName("polygon"):
                polygon: Element = polygon
                if polygon.nodeType == polygon.ELEMENT_NODE:
                    vertexes: [Vertex] = []
                    for vertex in polygon.childNodes:
                        vertex: Element = vertex
                        if vertex.nodeType == vertex.ELEMENT_NODE:
                            vertexes.append(
                                Vertex(vertex.getAttribute("id"), vertex.getAttribute("x"), vertex.getAttribute("y")))
                    result.append(Polygon(polygon.getAttribute("id"), vertexes))
        return result

    @staticmethod
    def get_polygon_by_id(search_id: str) -> Optional[Polygon]:
        XmlService.__dtd_validate()
        with parse(XmlService.XML_FILE) as dom:
            dom: Document = dom
            for polygon in dom.getElementsByTagName("polygon"):
                polygon: Element = polygon
                if polygon.nodeType == polygon.ELEMENT_NODE:
                    if search_id == polygon.getAttribute("id"):
                        vertexes: [Vertex] = []
                        for vertex in polygon.childNodes:
                            vertex: Element = vertex
                            if vertex.nodeType == vertex.ELEMENT_NODE:
                                vertexes.append(
                                    Vertex(vertex.getAttribute("id"), vertex.getAttribute("x"),
                                           vertex.getAttribute("y")))
                        return Polygon(polygon.getAttribute("id"), vertexes)
        return None

    @staticmethod
    def get_all_vertexes_by_polygon_id(search_id: str) -> [Vertex]:
        XmlService.__dtd_validate()
        with parse(XmlService.XML_FILE) as dom:
            dom: Document = dom
            for polygon in dom.getElementsByTagName("polygon"):
                polygon: Element = polygon
                if polygon.nodeType == polygon.ELEMENT_NODE:
                    if search_id == polygon.getAttribute("id"):
                        vertexes: [Vertex] = []
                        for vertex in polygon.childNodes:
                            vertex: Element = vertex
                            if vertex.nodeType == vertex.ELEMENT_NODE:
                                vertexes.append(
                                    Vertex(vertex.getAttribute("id"), vertex.getAttribute("x"),
                                           vertex.getAttribute("y")))
                        return vertexes
        return []

    @staticmethod
    def get_vertex_by_id(search_id: str) -> Optional[Vertex]:
        XmlService.__dtd_validate()
        with parse(XmlService.XML_FILE) as dom:
            dom: Document = dom
            for vertex in dom.getElementsByTagName("vertex"):
                vertex: Element = vertex
                if vertex.nodeType == vertex.ELEMENT_NODE:
                    if search_id == vertex.getAttribute("id"):
                        return Vertex(vertex.getAttribute("id"), vertex.getAttribute("x"), vertex.getAttribute("y"))
        return None

    @staticmethod
    def save_all(polygons: [Polygon]) -> None:
        XmlService.__dtd_validate()
        document: Document = Document()
        geometry: Element = document.createElement('geometry')
        document.appendChild(geometry)
        for polygon in polygons:
            polygon: Polygon = polygon
            polygon_element: Element = document.createElement("polygon")
            polygon_element.setAttribute("id", polygon.id)
            for vertex in polygon.points:
                vertex_element: Element = document.createElement("vertex")
                vertex_element.setAttribute("id", vertex.id)
                vertex_element.setAttribute("x", vertex.x)
                vertex_element.setAttribute("y", vertex.y)
                polygon_element.appendChild(vertex_element)
            geometry.appendChild(polygon_element)
        element = etree.fromstring(document.toxml())
        etree.indent(element, space="    ")
        result = etree.tostring(element, doctype=XmlService.DOCUMENT_PREFIX, encoding="UTF-8",
                                pretty_print=True, xml_declaration=True)
        with open(XmlService.XML_FILE, "wb") as file:
            file.write(result)
