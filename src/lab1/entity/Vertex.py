class Vertex:
    def __init__(self, _id: str, x: float, y: float):
        self.id: str = _id
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        return 'Vertex(id={0}, x={1}, y={2})'.format(self.id, self.x, self.y)
