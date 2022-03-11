class Node(object):
    def __init__(self, ID, x_position, y_position, direction):
        self.ID = ID
        self.x_position = x_position
        self.y_position = y_position
        self.direction = direction

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.ID == other.ID)
        else:
            return False

    def get_ID(self):
        return self.ID

    def get_attributes(self):
        return {'ID': self.ID, 
                'x_position': self.x_position, 
                'y_position': self.y_position}
