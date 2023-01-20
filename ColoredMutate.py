from eckity.genetic_operators.genetic_operator import GeneticOperator
from ManipultateColors import mutate

from ColoredGraph import ColoredGraph


class ColoredMutate(GeneticOperator):
    def __init__(self, probability=1, arity=1, events=None):
        super().__init__(probability, 1, events)

    # artiy is 1, so individulas len is 1.
    def apply(self, individuals):
        cg: ColoredGraph = individuals[0]
        cg_colors = cg.get_colors()
        new_colors = mutate(cg_colors, cg.num_of_colors)
        cg.paint_graph_vertices(new_colors)

        self.applied_individuals = individuals
        return individuals


#
# if __name__ == '__main__':
#     print("compiled")
#     cgc = ColoredGraphCreator()
#     individuals = cgc.create_individuals(10, higher_is_better=False)
#     cm = ColoredMutate()
#     cm.apply(individuals)
#     # cg_individual_is_modified = individulas[0]
#     print("OK finished!")
