class Edge :
    def __init__(self, car1, car2):
        self.car1 = car1
        self.car2 = car2
        self.relative_x = abs(car1.x_position - car2.x_position)

    def get_car1(self):
        return self.car1

    def get_car2(self):
        return self.car2

    def get_attributes(self):
        return {'relative_x': self.relative_x}
