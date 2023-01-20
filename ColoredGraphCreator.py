from eckity.creators.creator import Creator
from Graph import Graph
from ColoredGraph import ColoredGraph
from Data import Data
from ManipultateColors import init_random_colors
# import EssentialClasses


class ColoredGraphCreator(Creator):
    def __init__(self, events=None):
        super().__init__(events)

    def create_individuals(self, n_individuals, higher_is_better=False):
        individuals = []
        for i in range(n_individuals):
            graph = Graph(Data.NUM_OF_VERTICES)
            graph.load_adjacency_list(Data.EDJES_LIST)
            # create random colors array graph
            random_colors = init_random_colors(Data.NUM_OF_VERTICES, Data.NUM_OF_COLORS)
            # load graph colors array
            graph.load_vertices_colors(random_colors)
            graph.reset_fitness()
            # in colored_graph, update the colors field with the same colors array
            colored_graph = ColoredGraph(graph, Data.NUM_OF_VERTICES, Data.NUM_OF_COLORS, random_colors)
            individuals.append(colored_graph)

        return individuals

    # NUM_OF_VERTICES = 5
    # NUM_OF_COLORS = 3
    # graph = Graph(NUM_OF_VERTICES)
    # graph.load_adjacency_list(Data.edges_list0)
    # graph.load_vertices_colors(init_random_colors(NUM_OF_VERTICES, NUM_OF_COLORS))
    # graph.print_adjacency_list()
    # cg = ColoredGraph(graph, NUM_OF_VERTICES, NUM_OF_COLORS)
    # print("22")

# if __name__ == '__main__':
#     cg = ColoredGraphCreator(events=None)
#     individuals = cg.create_individuals(10, higher_is_better=True)
#     print("yes mother fucker")
