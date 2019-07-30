class Graph:
    def __init__(self, num_of_nodes):
        self.V = num_of_nodes
        self.graph = []

    def add_edge(self, v, u, weight):
        self.graph.append([u, v, weight])

    def __repr__(self):
        print(" V|U|Weight")
        for row in self.graph:
            print("[%d|%d|%lf]" % (row[0], row[1], row[2]))
        return ""


# Test
raw_list = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
G = Graph(len(raw_list))
for row in raw_list:
    G.add_edge(row[0], row[1], row[2])

print(G)
