class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

    def __repr__(self):
        return f"<EquilateralTriangle side={self.side_1}>"
