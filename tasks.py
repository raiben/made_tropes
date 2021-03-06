import os
from random import Random

from invoke import task
from pathos import multiprocessing

from trope_dna_builder.genetic_algorithm.optimizer import Optimizer


@task
def calculate_tropes_combination(list_of_current_tropes=[], seed=None):
    optimizer = Optimizer(list_of_current_tropes, seed)
    solution = optimizer.calculate_solution()


@task
def run_ga_experiment_1(context, seed=None):
    crossover_type = Optimizer.CROSSOVER_FROM_PARTS
    mutation_probabilities = [0.0116, 0.0232, 0.0464]
    crossover_probabilities = [0.5, 0.75, 1]
    population_sizes = [50, 100, 200]
    max_evaluations = 30000
    max_executions = 30
    no_better_results_during_evaluations = 0

    random = Random(int(seed))

    directory = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(directory):
        os.makedirs(directory)

    summary_file_name = os.path.join(directory, "genetic_tropes_execution_summary.log")

    pool = multiprocessing.Pool()

    map_parameters = []

    for mutation_probability in mutation_probabilities:
        for crossover_probability in crossover_probabilities:
            for population_size in population_sizes:
                for run_index in range(0, max_executions):
                    print("Mut={}, Cross={}, Pop={}, Run={}".format(mutation_probability, crossover_probability,
                                                                    population_size, run_index))
                    seed = random.randint(0, 100000)
                    execution_components = [str(mutation_probability), str(crossover_probability), str(population_size),
                                            str(max_evaluations), str(run_index), str(seed)]

                    execution_name = ", ".join(execution_components)
                    details_file_name = os.path.join(directory, "_".join(execution_components) + ".log")

                    parameters = (crossover_probability, details_file_name, execution_name, max_evaluations,
                                  mutation_probability, population_size, seed, summary_file_name, crossover_type,
                                  no_better_results_during_evaluations)
                    map_parameters.append(parameters)

    print("{!s} combinations".format(len(map_parameters)))
    pool.starmap(run_optomizer, map_parameters)
    pool.close()
    pool.join()


@task
def run_ga_experiment_2(context, seed=None):
    mutation_probabilities = [0.0116, 0.0232, 0.0464]
    crossover_probabilities = [0.5, 0.75, 1]
    crossover_types = [Optimizer.CROSSOVER_SUBSET]
    population_sizes = [50, 100, 200]
    max_evaluations = 30000
    max_executions = 30
    no_better_results_during_evaluations = 0

    random = Random(int(seed))

    directory = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(directory):
        os.makedirs(directory)

    summary_file_name = os.path.join(directory, "genetic_tropes_execution_summary_crossover_subset.log")

    pool = multiprocessing.Pool()

    map_parameters = []

    for mutation_probability in mutation_probabilities:
        for crossover_probability in crossover_probabilities:
            for crossover_type in crossover_types:
                for population_size in population_sizes:
                    for run_index in range(0, max_executions):
                        print("Mut={}, Cross={}, Pop={}, Run={}".format(mutation_probability, crossover_probability,
                                                                        population_size, run_index))
                        seed = random.randint(0, 100000)
                        execution_components = [str(mutation_probability), str(crossover_probability),
                                                str(crossover_type), str(population_size), str(max_evaluations),
                                                str(run_index), str(seed)]

                        execution_name = ",".join(execution_components)
                        details_file_name = os.path.join(directory, "_".join(execution_components) + ".log")

                        parameters = (crossover_probability, details_file_name, execution_name, max_evaluations,
                                      mutation_probability, population_size, seed, summary_file_name, crossover_type,
                                      no_better_results_during_evaluations)
                        map_parameters.append(parameters)

    print("{!s} combinations".format(len(map_parameters)))
    pool.starmap(run_optomizer, map_parameters)
    pool.close()
    pool.join()


@task
def run_ga_experiment_good_solution(context, seed=None):
    mutation_probability = 0.0116
    crossover_probability = 0.5
    crossover_type = Optimizer.CROSSOVER_FROM_PARTS
    population_size = 50
    max_evaluations = 30000
    no_better_results_during_evaluations = 30000
    max_executions = 30

    random = Random(int(seed))

    directory = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(directory):
        os.makedirs(directory)

    summary_file_name = os.path.join(directory, "genetic_tropes_execution_summary_good_solution.log")

    pool = multiprocessing.Pool()

    map_parameters = []
    for run_index in range(0, max_executions):
        print("Mut={}, Cross={}, Pop={}, Run={}".format(mutation_probability, crossover_probability,
                                                        population_size, run_index))
        seed = random.randint(0, 100000)
        execution_components = [str(mutation_probability), str(crossover_probability),
                                str(crossover_type), str(population_size), str(max_evaluations),
                                str(run_index), str(seed)]

        execution_name = ",".join(execution_components)
        details_file_name = os.path.join(directory, "_".join(execution_components) + ".log")

        parameters = (crossover_probability, details_file_name, execution_name, max_evaluations,
                      mutation_probability, population_size, seed, summary_file_name, crossover_type,
                      no_better_results_during_evaluations)
        map_parameters.append(parameters)

    print("{!s} combinations".format(len(map_parameters)))
    pool.starmap(run_optomizer, map_parameters)
    pool.close()
    pool.join()


def run_optomizer(crossover_probability, details_file_name, execution_name, max_evaluations,
                  mutation_probability, population_size, seed, summary_file_name, crossover_type,
                  no_better_results_during_evaluations):
    print("Running process...")
    optimizer = Optimizer(seed=seed, max_evaluations=max_evaluations,
                          mutation_probability=mutation_probability,
                          crossover_probability=crossover_probability,
                          population_size=population_size,
                          details_file_name=details_file_name, summary_file_name=summary_file_name,
                          execution_name=execution_name, crossover=crossover_type,
                          no_better_results_during_evaluations=no_better_results_during_evaluations)
    return optimizer.calculate_solution()
