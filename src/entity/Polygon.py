from src.entity.Vertex import Vertex


class Polygon:
    def __init__(self, _id: str, points: [Vertex] = None):
        self.id: str = _id
        self.points: [Vertex] = [] if points is None else points

    def __repr__(self):
        return 'Polygon(id={0}, points={1})'.format(self.id, self.points)
