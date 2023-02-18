import networkx as nx
import matplotlib.pyplot as plt

def to_graph(edges: list[tuple[int]]):
    g = nx.Graph()
    coord_dict = {}
    for i,edge in enumerate(edges):
        coord_dict[i] = (i // 2, (i % 2) * 2)
        g.add_edge(edge[0], edge[1])
    nx.draw(g, coord_dict, node_size=1000)
    return g

