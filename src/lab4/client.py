import xmlrpc.client

from src.lab4.const import HOST, PORT

s = xmlrpc.client.ServerProxy('http://' + HOST + ':' + PORT.__str__())
print(s.system.listMethods())
print(s.find_all_polygons())
print(s.mul(2, 3))
