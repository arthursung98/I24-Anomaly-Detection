from Node import Node
from Edge import Edge
import numpy as np

class Graph:
    # nodes is a list of node objects in the graph 
    # edges is a list of edge objects in the graph
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def get_nodes(self, with_attributes = False):
        if (not with_attributes):
            return self.nodes
        else:
            # returns a list of (node, attributes) pairs 
            # for visualization purpose
            # i.e. [(node1, node1.get_attributes()), ...]
            def pair(node):
                return (node, node.get_attributes())
            return list(map(pair, self.nodes))

    def get_edges(self, with_attributes = False):
        if (not with_attributes):
            return self.edges
        else:
            # returns a list of (car1, car2, attributes) triples 
            # for visualization purpose
            # i.e. [(car1, car2, edge.get_attributes()), ...]
            def triples(edge):
                return (edge.car1, edge.car2, edge.get_attributes())
            return list(map(triples, self.edges))

    def get_nodes_pos(self):
        # returns a dictionary of nodes paired with np.array(x_pos, y_pos)
        return {node: np.array([node.x_position, node.y_position]) for node in self.nodes}

    def add_node(self, node):
        if not node.ID in [node.ID for node in self.nodes]:
            self.nodes.append(node)
    
    def add_edge(self, edge):
        car1 = edge.get_car1()
        car2 = edge.get_car2()
        
        if ((car1 in self.nodes and car2 in self.nodes) and (not car1 == car2)):
            self.edges.append(edge)
