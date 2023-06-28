def cycle_crossover(parent1, parent2):

    cycle = [-1 for i in range(len(parent1))]
    cycle_index = 1

    for i in range(len(parent1)):
        if cycle[i] == -1:
            aux_index = parent1.index(parent2[i])
            while cycle[aux_index] == -1:
                cycle[aux_index] = cycle_index
                aux_index = parent1.index(parent2[aux_index])
            cycle_index += 1

    solution = [parent2[i] if n % 2 == 0 else parent1[i] for i, n in enumerate(cycle)]

    return solution
