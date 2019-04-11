"""
Introduction to Python

Lecture 3: Functions and Comprehensions

Task1: write your function to color nodes according to the number of neighbors the node has
Task2: write your own function to calculate number of connected components
"""

import matplotlib.pylab as plt
import numpy as np
import networkx as nx


def create_random_graph(nodes=30, delta=0.02):
    A = np.zeros(shape=(nodes, nodes), dtype=np.int)
    for i in range(nodes):
        for j in range(i):
            if np.random.random() < delta:
                A[i, j] = A[j, i] = 1

    return nx.from_numpy_matrix(A)


if __name__ == '__main__':
    G = create_random_graph(nodes=40, delta=0.06)
    print(type(G))
    colors = np.array(['b', 'g', 'r', 'c', 'm', 'y'], dtype=np.object)
    color_index = np.arange(len(G)) % len(colors)
    nx.draw(G, node_color=colors[color_index], with_labels=True)
    print('Edges:', G.edges)
    print('Nodes:', G.nodes)
    print('Number of connected components', nx.number_connected_components(G))

    plt.show()
