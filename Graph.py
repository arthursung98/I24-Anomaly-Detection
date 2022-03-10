class Graph:
  # nodes is a list of the nodes in the graph
  # edges is a dict mapping each node to a list of its children
  def __init__(self):
    self.nodes = []
    self.edges = {}

  def add_node(self, node):
    if node in self.nodes:
      raise ValueError('Duplicate Node')
    else:
      self.nodes.append(node)
      self.edges[node] = []
  
  def add_edge(self, edge):
    car1 = edge.get_car1()
    car2 = edge.get_car2()
    if not (car1 in self.nodes and car2 in self.nodes):
        raise ValueError('Node not in graph')
    self.edges[car1].append(car2)
    self.edges[car2].append(car1)

  