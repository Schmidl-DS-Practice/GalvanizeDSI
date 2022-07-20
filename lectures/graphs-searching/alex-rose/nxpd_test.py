# A test file for nxpd. When run from terminal ($ python nxpd_test.py), this should output a simple graph.
import numpy as np
import networkx as nx
import nxpd

g_matrix = np.array([
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0]
])
G = nx.from_numpy_matrix(g_matrix)
G.graph['rankdir'] = 'LR'
nxpd.draw(G)