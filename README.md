# Final Project: PageRank README #
### Teagan, Sydney, Conor and Michael ###
## Overview ##
	This code implements a variation of page rank. The file page_rank.py contains the code with child files Graph.py and Node.py. It takes in a text file representing a graph (graph.txt) and outputs the page rank vector and the number of iterations the algorithm took.

## Usage ##
Install numpy, a Python package that allows you to easily work with matrices, using pip (if you need help installing pip, see here)
In your terminal, run the command “pip install numpy”
To run page_rank on different graphs other than the example, either:
Edit the current graph.txt file. Each row is one edge, with the parent node (first) pointing to the child node (second). Or…
Create a new graph file. Follow the same format as the current graph.txt file, but put in your own edges and nodes. In the page_rank.py file, change the file that’s being read to “__your_graph_name__.txt”.
Time to run the program! In your terminal (make sure you’re in the same directory as page_rank.py is located in), run the command “python3 page_rank.py”. 
In your terminal, you’ll see a printed statement including the page rank vector and the number of iterations it took.

## Matrix Usage Explanation ##
	To implement page rank, we use matrices to represent each of the nodes and their respective ranks. Matrices allow us to easily manipulate the ranks of pages from one iteration to another. Numpy, the Python library, is an extremely powerful tool for working with matrices. It allows us to easily store matrices as data structures in Python, much like how we store arrays.
