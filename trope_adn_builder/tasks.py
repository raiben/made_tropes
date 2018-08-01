from random import Random

from invoke import task

from genetic_algorithm.optimizer import Optimizer


@task
def calculate_tropes_combination(list_of_current_tropes=[], seed=None):
    optimizer = Optimizer(list_of_current_tropes, seed)
    solution = optimizer.calculate_solution()


@task
def run_experiment(seed):
    mutation_probabilities = [0.0116, 0.0232, 0.0464]
    crossover_probabilities = [0.5, 0.75, 1]
    population_sizes = [50, 100, 200]

    random = Random(seed)

    for mutation_probability in mutation_probabilities:
        for crossover_probability in crossover_probabilities:
            for population_size in population_sizes:
                for run_index in range(0, 10):
                    print("Mut={}, Cross={}, Pop={}, Run={}".format(mutation_probability, crossover_probability,
                                                                    population_size, run_index))
                    optimizer = Optimizer(seed=random.randint(0, 100000), max_evaluations=30000,
                                          mutation_probability=0.0232,
                                          crossover_probability=1, population_size=100)
                    solution = optimizer.calculate_solution()
