import random


class Data:

    edges_list0 = [(0, 1), (1, 2), (3, 4), (0, 4)]
    edges_list1 = [(0, 2), (1, 3), (0, 3)]
    edges_list2 = [(0, 2), (0, 3), (0, 4), (2, 4)]
    edges_list3 = [(1, 3), (1, 2), (3, 4), (0, 2)]
    edges_list4 = [(0, 4), (1, 3), (3, 4), (0, 3)]
    edges_lists = [edges_list0, edges_list1, edges_list2, edges_list3, edges_list4]
    edges_list5 = [
        (0, 1), (0, 2),
        (1, 8), (1, 9),
        (2, 3), (2, 5), (2, 6), (2, 7),
        (3, 4), (3, 10), (3, 11),
        (4, 5), (4, 11), (4, 14),
        (5, 13),  (5, 14),
        (6, 7), (6, 16),
        (7, 15), (7, 16),
        (8, 15),
        (9, 13),
        (10, 11),
        (11, 12),
        (12, 17),
        (13, 16), (13, 17),
        (14, 17),
        (15, 16)
    ]
    edges_list10 = [(0, 1), (1, 2), (2, 0)]
    EDJES_LIST = []
    NUM_OF_VERTICES = 18
    NUM_OF_COLORS = 3
    fitness = None

    END_CALC = False

    def get_edgelist(self):
        return self.edges_lists[random.randrange(0, len(self.edges_lists))]

    colors = []
    # ReturnedData = {
    #     'Colors': [],
    #     'final_fitness': None,
    #     'num_og_generations': None
    # }

