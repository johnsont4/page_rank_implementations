import numpy as np
import math
from Graph import Graph
from Node import Node
from initialization import initialize_graph

def run_matrix_page_rank(graph):
    # Create A
    num_nodes = len(graph.nodes)
    A = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        deg = len(graph.nodes[i].children)
        for j in range(num_nodes):
            if graph.nodes[i].contains_child(graph.nodes[j].name):
                A[j][i] = (1 / deg)

    # Create v
    v = np.zeros(num_nodes)
    prop = (1 / num_nodes)
    for i in range(v.size):
        v[i] = prop

    diff = math.inf
    iter = 0
    old_matrix = v
    while diff > .001:
        #print(diff)
        v = np.matmul(A, v)
        #print(v)

        diff_matrix = abs(np.subtract(old_matrix, v))
        diff = np.sum(diff_matrix)
        old_matrix = v
        iter += 1

    return np.round(v, 3), iter


def main():
    small_graph = Graph()
    med_graph = Graph()
    big_graph = Graph()
    initialize_graph(small_graph, 'small_graph.txt')
    initialize_graph(med_graph, 'med_graph.txt')
    initialize_graph(big_graph, 'big_graph.txt')

    small_v, small_iter = run_matrix_page_rank(small_graph)
    med_v, med_iter = run_matrix_page_rank(med_graph)
    big_v, big_iter = run_matrix_page_rank(big_graph)

    print("Matrix: ", small_v, "Iterations: ", small_iter)
    print("Matrix: ", med_v, "Iterations: ", med_iter)
    print("Matrix: ", big_v, "Iterations: ", big_iter)

main()
