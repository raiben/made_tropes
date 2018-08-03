import os
from random import Random

from invoke import task

from trope_dna_builder.genetic_algorithm.optimizer import Optimizer


@task
def calculate_tropes_combination(list_of_current_tropes=[], seed=None):
    optimizer = Optimizer(list_of_current_tropes, seed)
    solution = optimizer.calculate_solution()


@task
def run_ga_experiment_1(context, seed=None):
    mutation_probabilities = [0.0116, 0.0232, 0.0464]
    crossover_probabilities = [0.5, 0.75, 1]
    population_sizes = [50, 100, 200]
    max_evaluations = 30000

    random = Random(int(seed))

    directory = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(directory):
        os.makedirs(directory)

    summary_file_name = os.path.join(directory, "genetic_tropes_execution_summary.log")

    for mutation_probability in mutation_probabilities:
        for crossover_probability in crossover_probabilities:
            for population_size in population_sizes:
                for run_index in range(0, 10):
                    print("Mut={}, Cross={}, Pop={}, Run={}".format(mutation_probability, crossover_probability,
                                                                    population_size, run_index))
                    seed = random.randint(0, 100000)
                    execution_components = [str(mutation_probability), str(crossover_probability), str(population_size),
                                            str(max_evaluations), str(run_index), str(seed)]

                    execution_name = ", ".join(execution_components)
                    details_file_name = os.path.join(directory, "_".join(execution_components) + ".log")
                    optimizer = Optimizer(seed=seed, max_evaluations=max_evaluations,
                                          mutation_probability=mutation_probability,
                                          crossover_probability=crossover_probability,
                                          population_size=population_size,
                                          details_file_name=details_file_name, summary_file_name=summary_file_name,
                                          execution_name=execution_name)
                    solution = optimizer.calculate_solution()
