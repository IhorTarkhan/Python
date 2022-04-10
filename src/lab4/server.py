from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer

from src.lab2.repository.PolygonRepositorySQLite import PolygonRepositorySQLite
from src.lab2.repository.VertexRepositorySQLite import VertexRepositorySQLite
from src.lab3.converters import from_json
from src.lab4.const import HOST, PORT


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


polygon_repository = PolygonRepositorySQLite()
vertex_repository = VertexRepositorySQLite()


class FunctionalClass(PolygonRepositorySQLite, VertexRepositorySQLite):
    def add_vertex_to_polygon_by_id_json(self, _id, value):
        return self.add_vertex_to_polygon_by_id(_id, from_json(value))

    def add_polygon_json(self, value):
        return self.add_polygon(from_json(value))


with SimpleXMLRPCServer((HOST, PORT), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_instance(FunctionalClass())
    server.serve_forever()
