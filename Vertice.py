class Vertice:
    def __init__(self, index: int, color):
        self.index = index
        self.color = color
        self.is_legal = True
        self.neighbours = list()

    def print_vertice(self):
        print(f'({self.index}, {self.color}, {self.is_legal})')

    def print_vertice_extended(self):
        print(f'index: {self.index} \ncolor: {self.color}\nlegal: {self.is_legal}')

    def get_index(self):
        return self.index

    def get_color(self):
        return self.color

    def set_color(self, colorr: int):
        self.color = colorr

    def get_is_legal(self):
        return self.is_legal

    def set_is_legal(self, is_legal):
        self.is_legal = is_legal

    def add_neighbour(self, vertice_to_add):
        self.neighbours.append(vertice_to_add) if vertice_to_add not in self.neighbours else self.neighbours

    def get_neighbours(self):
        return self.neighbours


# if __name__ == '__main__':
#     v0 = Vertice(0, 2)
#     v0.print_vertice_extended()
#     v0.set_color(11)
#     v0.print_vertice_extended()
