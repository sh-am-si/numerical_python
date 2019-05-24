"""
Introduction to Python

Lecture 3: Functions and Comprehensions

Task1: write your function to color nodes according to the number of neighbors the node has
Task2: write your own function to calculate number of connected components
"""

import matplotlib.pylab as plt
import networkx as nx
import numpy as np


def create_random_graph(nodes=30, delta=0.02):
    A = np.zeros(shape=(nodes, nodes), dtype=np.int)
    for i in range(nodes):
        for j in range(i):
            if np.random.random() < delta:
                A[i, j] = A[j, i] = 1

    return nx.from_numpy_matrix(A)


def get_cc_num(graph):
    '''
    algorithm suggested by Sebastian and Grzegorz
    :param graph:
    :return:
    '''
    cc = np.arange(len(graph))
    for edge in graph.edges:
        n, m = cc[edge[0]], cc[edge[1]]
        cc[cc == m] = n
    return len(np.unique(cc))


if __name__ == '__main__':
    G = create_random_graph(nodes=20, delta=0.06)
    print(type(G))
    colors = np.array(['b', 'g', 'r', 'c', 'm', 'y'], dtype=np.object)
    color_index = np.arange(len(G)) % len(colors)
    nx.draw(G, node_color=colors[color_index], with_labels=True)
    print('Edges:', G.edges)
    print('Nodes:', G.nodes)
    print('Number of connected components', nx.number_connected_components(G))
    print('My number of connected components', get_cc_num(G))

    flag = True
    for nodes in range(20, 120):
        for delta in np.linspace(0.01, 0.09, 100):
            G = create_random_graph(nodes=nodes, delta=delta)
            if nx.number_connected_components(G) != get_cc_num(G):
                print(f'wrong for {nodes} nodes and {delta} delta')
                flag = False
                break
    print('Test passed' if flag else 'Test failed')

    plt.show()
