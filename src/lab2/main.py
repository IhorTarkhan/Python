from src.common_data.demo import demo
from src.lab2.repository.PolygonRepositorySQLite import PolygonRepositorySQLite
from src.lab2.repository.VertexRepositorySQLite import VertexRepositorySQLite

demo(PolygonRepositorySQLite(), VertexRepositorySQLite())
