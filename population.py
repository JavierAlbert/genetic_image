import numpy as np
import individual

# The class population is mainly a set of individuals
# It is initialized with new individuals that have new genes

# It has 2 methods:
# - selection_pool: Checks the fitness of all the contained individuals and
#                   selects the 4 individuals with the highest fitness
# - evolve: Given the 4 pre-selected individuals it creates a new generation of
#           individuals. Each new individual is created by randomly choosing 2
#           past individuals from the pool that are crossed and allow to mutate.

class population():

    def __init__(self):

        # Create fresh and new individuals

        self.pop = []
        for i in range(POPULATION_SIZE):
            self.pop.append(individual())

    def selection_pool(self):

        # Choose the best 4 individuals based on fitness

        sorted_individuals = sorted(self.pop, key=lambda x: x.fitness, reverse=True)
        pool = sorted_individuals[:4]
        return pool

    def evolve(self):

        # Random select 2 parents, cross them and mutate them to create new individuals

        pool = self.selection_pool()
        self.pop = []
        for i in range(POPULATION_SIZE):
            chosen = np.random.choice(pool, 2, replace=False)
            self.pop.append(individual(chosen[0], chosen[1]))