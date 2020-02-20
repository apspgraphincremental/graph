from graph.Graph import Graph
from server.Services import Services


class GraphServices(Services):
    def __init__(self):
        Services.__init__(self)

    def create_graph(self, num_nodes, probability_edges, directed):
        print("Generate. Nodes[" + str(num_nodes) + "] Edges[" + str(probability_edges) + "] Direc[" + str(directed)+ "]")
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)

        return self.export(graph)

    def dynamic_incremental_random_edge(self, values):
        graph = Graph.import_values(values)
        graph.dynamic_incremental_random_edge()

        return self.export(graph)
