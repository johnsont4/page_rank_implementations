from Graph import Graph
from Node import Node

# This creates a graph using the Graph and Node classes above
def initialize_graph(graph, new_file):
    # Open the text file
    with open(new_file) as file:
        nodes = file.readlines()

    # Iterate through nodes, adding nodes to graph
    for x in nodes:
        if not graph.contains(x[0]): # if the first node is not in the graph
            graph.add_node(Node(name=x[0]))
        if not graph.contains(x[1]): # if the second node is not in the graph
            graph.add_node(Node(name=x[1]))

    for connection in nodes: # Calls graph's add_edge function
        graph.add_edge(Node(name=connection[0]), Node(name=connection[1]))
