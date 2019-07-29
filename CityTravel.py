import networkx as nx
from matplotlib import pylab

raw_list = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
G = nx.Graph()


def build_graph(raw_list):
    for row in raw_list:
        if row[0] not in list(G.nodes):
            G.add_node(row[0])
        if row[1] not in list(G.nodes):
            G.add_node(row[1])
        G.add_edge(row[0], row[1], weight=row[2])


def print_graph(G):
    pos = nx.spring_layout(G)
    pylab.figure(2)
    nx.draw(G, pos, with_labels=True)
    # specifiy edge labels explicitly
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # show graphs
    pylab.show()


build_graph(raw_list)
print_graph(G)
