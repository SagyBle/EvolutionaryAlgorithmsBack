from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

from ColoredGraph import ColoredGraph

from ColoredGraphCreator import ColoredGraphCreator


class ColoredGraphEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

    def _evaluate_individual(self, colored_graph: ColoredGraph):
        colored_graph.set_all_vertices_to_legal()
        collisions = 0
        for vertice in colored_graph.get_graph().get_adjacency_list():
            for neighbour in vertice.get_neighbours():
                if vertice.get_color() == neighbour.get_color():
                    if vertice.get_is_legal():
                        collisions += 1
                        vertice.set_is_legal(False)
                    if neighbour.get_is_legal():
                        collisions += 1
                        neighbour.set_is_legal(False)
        colored_graph.get_graph().sett_fitness(collisions)
        return_val = colored_graph.get_graph().get_fitness()
        # if return_val == 0:
            # print("from ColoredGraphEvaluator found return_val==0")
        return return_val

# if __name__ == '__main__':
#     print("compiled")
#     cge = ColoredGraphEvaluator()
#     cgc = ColoredGraphCreator()
#     individulas = cgc.create_individuals(10, higher_is_better=False)
#     cg_individual = individulas[0]
#     return_val = cge._evaluate_individual(cg_individual)
#     print(return_val)
#     print("OK finished!")

