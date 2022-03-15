import numpy as np
from Graph import Graph
from Node import Node
from initialization import initialize_graph

# This implementation implements the "surfer" idea of page rank
# Every iteration of the

# Defines one iteration of page rank
def one_iter(graph, damp):
    nodes = graph.nodes
    for node in nodes:
        node.update_page_rank(damp, len(graph.nodes)) # look in node file

# Runs page rank x amount of times
def run_page_rank(graph, damp):
    for x in range(1000):
        one_iter(graph, damp)
    graph.normalize_pagerank() # Normalizes page rank values


def main():
    graph = Graph()
    initialize_graph(graph, 'med_graph.txt')

    run_page_rank(graph, 0.15) # change damper to whatever you want (0,1)

    for node in graph.nodes:
        print("Node's name: ", node.name)
        print("Page rank: ", node.pagerank)

main()
