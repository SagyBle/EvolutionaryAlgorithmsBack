from random import randrange, uniform


def init_random_colors(num_of_vertices: int, num_of_colors: int):
    colors = [None] * num_of_vertices
    for i in range(0, num_of_vertices):
        colors[i] = randrange(num_of_colors)
    return colors


# change an colors entry in probability of 0/3(= p) * ((num_of_colors-1)/num_of_colors)
# returns new colors array
def mutate(old_colors: [int], num_of_colors):
    new_colors = old_colors
    num_of_vertices = len(old_colors)
    # initialize new random colors array
    possible_colors = init_random_colors(num_of_vertices, num_of_colors)

    # in probability p we'll take the new color from possible_colors array
    for i in range(0, num_of_vertices):
        if uniform(0, 1) <= 0.3:
            new_colors[i] = possible_colors[i]
    return new_colors

# arrays are passed by reference, and function change them!
def crossover(colors0: [int], colors1: [int]):
    len_of_colors = len(colors0)
    start_index = 0
    end_index = randrange(1, len_of_colors)

    colors0[start_index:end_index], colors1[start_index:end_index] = colors1[start_index:end_index], \
        colors0[start_index:end_index]
    return colors0, colors1

# if __name__ == '__main__':
#     NUM_OF_COLORS = 3
    # colors0 = init_random_colors(5, NUM_OF_COLORS)
    # colors1 = init_random_colors(5, NUM_OF_COLORS)

    # print(colors0)
    # mutate(colors0, num_of_colors=NUM_OF_COLORS)
    # print(colors0)
    #
    # print(f'colors0: {colors0}')
    # print(f'colors1: {colors1}')
    # print("after crossover:")
    # crossover(colors0, colors1)
    # print(f'colors0: {colors0}')
    # print(f'colors1: {colors1}')
    #
    #
    #
    # colors0 = [0,0,0,0,0]
    # colors1 = [1,1,1,1,1]
    # print("before crossover:")
    # print(colors0)
    # print(colors1)
    # crossover(colors0,colors1)
    # print("after crossover:")
    # print(colors0)
    # print(colors1)
    # print(mutate(colors0, 3))


