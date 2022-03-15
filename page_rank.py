# Created by Teagan Johnson, Michael Dreger, Sydney Bell, Conor Babcock O'Neill
import numpy as np
import math
from Graph import Graph
from Node import Node
from initialization import initialize_graph

# Input: a graph object defined in Graph.py, an integer damper effect
# Output: a numpy array and an integer
def run_matrix_page_rank(graph, d):
    # Find total number of nodes in graph (used later)
    num_nodes = len(graph.nodes)
    # Create A, the transition matrix of the graph
    A = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        deg = len(graph.nodes[i].children)
        for j in range(num_nodes):
            if graph.nodes[i].contains_child(graph.nodes[j].name):
                A[j][i] = (1 / deg)

    # Create v, the rank vector (keeps track of page ranks)
    v = np.zeros(num_nodes)
    prop = (1 / num_nodes)
    for i in range(v.size): # initialize values of v to 1/number of nodes
        v[i] = prop

    # Define B, the probability that a node randomly jumps to another node
    B = (1/num_nodes) * (np.ones(num_nodes)) # initialize values to 1/num nodes

    diff = math.inf # Difference value used for while loop consideration
    iter = 0 # Keeps track of number of iterations of page rank
    previous_pageranks = v # initialize to v, keeps track of previous page ranks
    while diff > .01:

        # Create M. This is the variable that holds the new matrix values
        # including the damper effect d
        M = ((1-d)*A) + d*B
        # Update v to the value of M*v
        v = np.matmul(M, v)

        # keep track of differences from previous rank to current rank for each
        # node
        diff_matrix = abs(np.subtract(previous_pageranks, v))
        diff = np.sum(diff_matrix) # total difference from previous to current
        previous_pageranks = v # update previous page rank values
        iter += 1

    # Total sum of page ranks. Used to normalize rank vector
    total_sum = sum(v)

    # Normalize each rank so v adds up to 1
    for x in range(num_nodes):
        v[x] = v[x] / total_sum

    return np.round(v, 4), iter


def main():
    small_graph = initialize_graph('small_graph.txt')
    med_graph = initialize_graph('med_graph.txt')
    big_graph = initialize_graph('big_graph.txt')

    small_v, small_iter = run_matrix_page_rank(small_graph, .15)
    med_v, med_iter = run_matrix_page_rank(med_graph, .15)
    big_v, big_iter = run_matrix_page_rank(big_graph, .15)

    print("Matrix: ", small_v, "Iterations: ", small_iter)
    print("Matrix: ", med_v, "Iterations: ", med_iter)
    print("Matrix: ", big_v, "Iterations: ", big_iter)

main()
