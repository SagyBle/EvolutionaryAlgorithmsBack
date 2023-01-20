import ManipultateColors
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange
from ColoredGraph import ColoredGraph
from ManipultateColors import crossover

from ColoredGraphCreator import ColoredGraphCreator


class ColoredCrossover(GeneticOperator):
    def __init__(self, probability=1, arity=2, events=None):
        super().__init__(probability, arity, events)

    def apply(self, individuals: [ColoredGraph]):
        # get individuals
        cg0: ColoredGraph = individuals[0]
        cg1: ColoredGraph = individuals[1]
        # get cg's colors arrays
        colors_cg0 = cg0.get_colors()
        colors_cg1 = cg1.get_colors()
        # commit the crossover
        crossovered_colors_cg0, crossovered_colors_cg1 = crossover(
            colors_cg0, colors_cg1)
        # set the new colors array, and paint the cg's vertices.
        cg0.paint_graph_vertices(crossovered_colors_cg0)
        cg1.paint_graph_vertices(crossovered_colors_cg1)

        self.applied_individuals = individuals
        return individuals

# if __name__ == '__main__':
#     print("compiled")
#     cgc = ColoredGraphCreator()
#     individuals = cgc.create_individuals(10, higher_is_better=False)
#     cco = ColoredCrossover()
#     cg0 = individuals[0]
#     cg1 = individuals[1]
#     cco.apply(individuals)
#     cg0 = individuals[0]
#     cg1 = individuals[1]
