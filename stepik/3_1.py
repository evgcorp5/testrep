class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to_origin(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        return None

    def get_distance(self, point2):
        if not isinstance(point2, Point):
            print('Передана не точка')
            return None
        if hasattr(self, 'x') and hasattr(self, 'y') and hasattr(point2, 'x') and hasattr(point2, 'y'):
            return (abs(self.x - point2.x) ** 2 + abs(self.y - point2.y) ** 2) ** 0.5
        print('Координаты не заданы')
        return None

    def display(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            print(f"Point({self.x}, {self.y})")
        else:
            print('Координаты не заданы')