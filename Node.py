class Node(object):
    def __init__(self, ID, x_position, y_position, direction):
        self.ID = ID
        self.x_position = x_position
        self.y_position = y_position
        self.direction = direction

    def __eq__(self, other):
        return self.ID == other.ID

    def get_ID(self):
        return self.ID

    def get_attributes(self):
        return {'ID': ID, 
                'x_position': self.x_position, 
                'y_position': self.y_position}
