class Node(object):
  def __init__(self, ID, x_position, y_position, direction):
    self.ID = ID
    self.x_position = x_position
    self.y_position = y_position
    self.direction = direction

  def get_ID(self):
    return self.ID
  