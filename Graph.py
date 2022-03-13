# Defines what a graph is for both implementations

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    # Check if the node is in the graph
    def contains(self, name):
        for node in self.nodes:
            if node.name == name:
                return True
        return False

    # Return the node given the node name (A, B, C, etc.)
    def find(self, name):
        if (self.contains(name)):
            for node in self.nodes:
                if node.name == name:
                    return node
        else: # if not found, create a new node
            node_new = Node(name=name)
            self.add_node(node_new)
            return node_new

    # Adds an edge (both parent and child) between 2 nodes
    def add_edge(self, parent, child):
        parent_node = self.find(parent.name)
        child_node = self.find(child.name)

        parent_node.add_child(child_node)
        child_node.add_parent(parent_node)

    # We need to normalize the pagerank after running it
    # Otherwise, we'd have an unstadard measurement
    def normalize_pagerank(self):
        pagerank_sum = sum(node.pagerank for node in self.nodes)

        for node in self.nodes:
            node.pagerank /= pagerank_sum
