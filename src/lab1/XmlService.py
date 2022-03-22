from typing import Optional
from xml.dom.minidom import Document
from xml.dom.minidom import Element
from xml.dom.minidom import parse

from lxml import etree
from lxml.etree import XMLSyntaxError

from src.lab1.entity.Polygon import Polygon
from src.lab1.entity.Vertex import Vertex


class XmlService:
    XML_FILE = "resources/sample.xml"

    @staticmethod
    def dtd_validate() -> None:
        parser = etree.XMLParser(dtd_validation=True)
        try:
            etree.parse(XmlService.XML_FILE, parser)
        except XMLSyntaxError as e:
            print(e)
            raise e

    @staticmethod
    def get_all_polygons() -> [Polygon]:
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
        with parse(XmlService.XML_FILE) as dom:
            dom: Document = dom
            for vertex in dom.getElementsByTagName("vertex"):
                vertex: Element = vertex
                if vertex.nodeType == vertex.ELEMENT_NODE:
                    if search_id == vertex.getAttribute("id"):
                        return Vertex(vertex.getAttribute("id"), vertex.getAttribute("x"), vertex.getAttribute("y"))
        return None
