import networkx as nx # for visualization
import matplotlib.pyplot as plt # for plotting
from Graph import Graph
from Node import Node
from Edge import Edge
import random

'''
Plots a Graph object using networkx library

@param    graphObject - an object of type Graph
'''
def plot_graph(graphObject):
    # initialize nx graph to visualize
    G = nx.Graph()
    # add nodes from graph object
    G.add_nodes_from(graphObject.get_nodes(True))
    # iterate through dictionary and add to G
    G.add_edges_from(graphObject.get_edges(True))

    fig, ax = plt.subplots()
    # pos holds the position of where all individual nodes will be plotted
    pos = nx.spring_layout(G)
    nodes = nx.draw_networkx_nodes(G, pos=pos, ax=ax)
    edges = nx.draw_networkx_edges(G, pos=pos, ax=ax)

    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                      bbox=dict(boxstyle="round", fc="w"),
                      arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    
    # updates the annotation for the hovered item ind
    def update_annot(ind, isNode):
        if isNode: 
            # updates the annotation for a node
            node = list(G.nodes)[ind["ind"][0]]
            xy = pos[node]
            annot.xy = xy
            node_attr = {'node': node}
            node_attr.update(G.nodes[node])
            text = 'Node'
            for k, v in node_attr.items():
                if not type(v) is Node:
                    text += '\n' + f'{k}: {v}'
            annot.set_text(text)
        else:
            # updates the annotation for an edge
            edge = list(G.edges)[ind["ind"][0]]
            # since pos only holds the locations of the nodes, we find
            # the avg of the location of nodes to find the edge's midpoint
            xy = (pos[edge[0]] + pos[edge[1]]) / 2
            annot.xy = xy
            edge_attr = {'edge': edge}
            edge_attr.update(G.edges[edge])
            text = 'Edge'
            for k, v in edge_attr.items():
                # if attribute is the (Node, Node) tuple, add the
                # car IDs instead
                if type(v) is tuple:
                    text += '\n' + f'car1_ID: {v[0].ID}'
                    text += '\n' + f'car2_ID: {v[1].ID}'
                else:
                    text += '\n' + f'{k}: {v}'
            annot.set_text(text)
        
    # detects if user hovers a node or an edge
    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            # check if nodes/edges contain mouse event
            cont, ind = nodes.contains(event)
            cont2, ind2 = edges.contains(event)
            # ind is the item containing the event
            if cont or cont2:
                # update the annotation for the item
                if cont:
                    update_annot(ind, True)
                elif cont2:
                    update_annot(ind2, False)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()
  
    fig.canvas.mpl_connect("motion_notify_event", hover)
    
    plt.show()

def generate_random_graph(num_of_nodes=5, verbose=False):
    graph = Graph()
    
    # randomly generate X nodes
    list_of_nodes = []
    for i in range(num_of_nodes):
        random_x = random.random() * 200
        random_y = random.random() * 200
        node = Node(i, random_x, random_y, 0)
        list_of_nodes.append(node)
        graph.add_node(node)
        if verbose:
            print('Added node: {nodeID} {attribute}'.format(nodeID = node.get_ID(), attribute = node.get_attributes()))

    # randomly pick two nodes and form an edge (do this X times)
    for i in range(20):
        two_random_nodes = random.sample(list_of_nodes, 2)
        edge = Edge(two_random_nodes[0], two_random_nodes[1])
        graph.add_edge(edge)
        if verbose:
            print('Added edge: {car1ID} {car2ID} {attribute}'.format(car1ID = edge.get_car1().ID, car2ID = edge.get_car2().ID, attribute = edge.get_attributes()))

    return graph

def test_run_zi():
    G = generate_random_graph(10)
    plot_graph(G)
    