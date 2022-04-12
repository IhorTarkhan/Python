from django.http import HttpResponse

from src.common_data.entity.Polygon import Polygon
from src.common_data.entity.Vertex import Vertex
from src.lab2.repository.PolygonRepositorySQLite import PolygonRepositorySQLite
from src.lab2.repository.VertexRepositorySQLite import VertexRepositorySQLite

styles = """
<style>
    body {
        font-family: arial, sans-serif;
        width: 500px;
        margin: auto;
    }

    h3 {
        text-align: center;
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    thead tr {
        background-color: aquamarine;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
"""

vertex_repository = VertexRepositorySQLite()
polygon_repository = PolygonRepositorySQLite()


def polygon_to_html(polygon: Polygon):
    return """
    <tr>
        <td>%s</td>
        <td><a href="vertexes/%s">%s</a></td>
    </tr>""" % (polygon.id, polygon.id, len(polygon.points))


def vertex_to_html(vertex: Vertex):
    return """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>""" % (vertex.id, vertex.x, vertex.y)


def polygons(request):
    polygon_list = polygon_repository.find_all_polygons()
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Polygons</title>
        %s
    </head>
    <body>
        <h3>Polygons</h3>
        <table>
            <thead>
                <tr>
                    <th>id</th>
                    <th>Vertex count</th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
""" % (styles, ''.join([polygon_to_html(p) for p in polygon_list])))


def vertexes(request, polygon_id):
    vertex_list = vertex_repository.find_all_vertex_in_polygon(polygon_id)
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Vertexes</title>
        %s
    </head>
    <body>
        <h3>Vertexes</h3>
        <table>
            <thead>
                <tr>
                    <th>id</th>
                    <th>x</th>
                    <th>y</th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
""" % (styles, ''.join([vertex_to_html(v) for v in vertex_list])))
