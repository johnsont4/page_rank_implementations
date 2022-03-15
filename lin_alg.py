# Motivation from https://en.wikipedia.org/wiki/PageRank

import numpy as np
from Graph import Graph
from Node import Node
from initialization import initialize_graph

def pagerank(M, num_iterations, damp):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = ((1-damp) * M + (damp) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v

def main():
    graph = Graph()
    initialize_graph(graph, 'big_graph.txt')

    num_nodes = len(graph.nodes)
    A = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        deg = len(graph.nodes[i].children)
        for j in range(num_nodes):
            if graph.nodes[i].contains_child(graph.nodes[j].name):
                A[j][i] = (1 / deg)

    v = pagerank(A, 100, 0.15)
    print(v)

main()
