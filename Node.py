# Defines what a node is for both implementations

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.pagerank = 1.0 # Initialize pagerank to 1

    # Adds a node to the nodes children list
    def add_child(self, new_child):
        if new_child not in self.children:
            self.children.append(new_child)
    # Adds a node to the node's parent list
    def add_parent(self, new_parent):
        if new_parent not in self.parents:
            self.parents.append(new_parent)

    # Update pagerank for one node
    def update_page_rank(self, damper, num_nodes):
        in_nodes = self.parents
        PR_summation = sum(node.pagerank / len(node.children) for node in in_nodes)
        random_jump = damper / num_nodes
        self.pagerank = random_jump + (1-damper) * PR_summation

    # Check if the node is in the graph
    def contains_child(self, name):
        for node in self.children:
            if node.name == name:
                return True
        return False
