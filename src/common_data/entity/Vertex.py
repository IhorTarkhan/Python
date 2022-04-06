class Vertex:
    def __init__(self, _id: str, x: str, y: str):
        self.id: str = _id
        self.x: str = x
        self.y: str = y

    def __repr__(self):
        return 'Vertex(id={0}, x={1}, y={2})'.format(self.id, self.x, self.y)
