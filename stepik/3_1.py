class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to_origin(self):
        self._check_coordinates()
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def display(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            print(f"Point({self.x}, {self.y})")
        else:
            print('Координаты не заданы')

    def get_distance(self, obj):
        if not isinstance(obj, Point):
            raise TypeError("Передан объект, который не является точкой")

        self._check_coordinates()
        obj._check_coordinates()
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5

    def _check_coordinates(self):
        if not hasattr(self, 'x') or not hasattr(self, 'y'):
            raise AttributeError("Координаты точки не заданы")
