"""
Creating a standard graph and displaying it along with the its matrix
"""

import matplotlib.pylab as plt
import networkx as nx
import matplotlib.cm


if __name__ == '__main__':
    G = nx.barabasi_albert_graph(30, 5)
    plt.figure('Graph')
    nx.draw_circular(G, node_color=range(len(G)), cmap=matplotlib.cm.jet, with_labels=True)
    plt.figure('Graph Matrix')
    plt.imshow(nx.to_numpy_matrix(G))

    plt.show()
