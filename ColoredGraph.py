from random import randrange
import pandas as pd
from eckity.individual import Individual
from eckity.fitness.simple_fitness import SimpleFitness
from Graph import Graph
from Data import Data
from ManipultateColors import init_random_colors

class ColoredGraph(Individual):
    def __init__(self, graph, num_of_vertices, num_of_colors, colors):
        super().__init__(SimpleFitness())
        self.graph = graph
        # self.num_of_vertices = num_of_vertices
        self.num_of_colors = num_of_colors
        self.colors = colors

    def get_graph(self):
        return self.graph

    def get_num_of_colors(self):
        return self.num_of_colors

    def get_colors(self):
        return self.colors

    def set_all_vertices_to_legal(self):
        self.graph.set_all_vertices_to_legal()

    def paint_graph_vertices(self, colors):
        self.colors = colors
        self.graph.load_vertices_colors(colors)
        self.graph.reset_fitness()

    def evaluate_fitness(self):
        return self.graph.evaluate_fitness()



    # override - Individual interface
    def show(self):
        colors = self.get_colors()
        self.graph.print_adjacency_list()

        Data.colors = colors
        Data.fitness = self.graph.get_fitness()
        Data.END_CALC = True

        print(f'colors: {colors}\nfitness: {self.graph.get_fitness()}')


# if __name__ == '__main__':
#     graph = Graph(Data.NUM_OF_VERTICES)
#     graph.load_adjacency_list(Data.EDJES_LIST)
#     colors = [0, 1, 1]
#     cg = ColoredGraph(graph, Data.NUM_OF_VERTICES, Data.NUM_OF_COLORS, colors)
#     cg.paint_graph_vertices([0, 0, 0])
#     cg.evaluate_fitness()
#     print("end1")
#     NUM_OF_VERTICES = 5
#     NUM_OF_COLORS = 3
#     graph = Graph(NUM_OF_VERTICES)
#     graph.load_adjacency_list(Data.edges_list5)
#     graph.load_vertices_colors(init_random_colors(NUM_OF_VERTICES, NUM_OF_COLORS))
#     graph.print_adjacency_list()
#     cg = ColoredGraph(graph, NUM_OF_VERTICES, NUM_OF_COLORS)
#     print("22")
