import multiprocessing
import os.path
import re
from multiprocessing.pool import ThreadPool
from random import Random
import time

import cachetools as cachetools
import inspyred
from inspyred.ec.analysis import fitness_statistics


class Solution(object):
    def __init__(self, trope_list, fitness):
        self.trope_list = trope_list
        self.fitness = fitness


class AssociativeRule(object):
    def __init__(self, antecedents, consequents, confidence):
        self.antecedents = antecedents
        self.consequents = consequents
        self.confidence = confidence


class Optimizer(object):
    DEFAULT_APRIORI_FILE = "../../scripts/data/apriori_rules_0.005_0.05.txt"

    ITEM_PATTERN = re.compile("^item: \(([^\\\\]*)\)")
    RULE_PATTERN = re.compile("^Rule: \((.*)\) ==> \((.*)\) , ([0-9\.]*)$")
    NUMBER_OF_CPUS = 8

    def __init__(self, list_of_current_tropes=[], seed=None, number_of_tropes=43, path_to_rules=None,
                 max_evaluations=30000, multi_process=False, multi_thread=False, mutation_probability=0.0232,
                 crossover_probability=1, population_size=100, details_file_name=None, summary_file_name=None,
                 execution_name="execution"):

        self.list_of_tropes = list_of_current_tropes
        self.random = Random(seed) if seed is not None else Random(time())
        self.number_of_tropes = number_of_tropes
        self.path_to_rules = path_to_rules if path_to_rules is not None else self._build_default_path_to_rules()
        self.max_evaluations = max_evaluations
        self.multi_process = multi_process
        self.multi_thread = multi_thread
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.population_size = population_size

        self.details_file_name = details_file_name
        self.summary_file_name = summary_file_name
        self.execution_name = execution_name

        self.tropes = []
        self.tropes_indexes = []
        self.rules_by_trope = {}
        self.rules_by_antecedent_and_consequent = {}

        self._retrieve_info_from_file()
        self.cache = cachetools.LRUCache(5000, missing=None, getsizeof=None)

    def calculate_solution(self):
        start = time.time()

        ea = inspyred.ec.GA(self.random)
        pool = None

        ea.selector = inspyred.ec.selectors.tournament_selection
        ea.terminator = inspyred.ec.terminators.evaluation_termination
        ea.variator = [self.build_mutator(), inspyred.ec.variators.crossover(self.build_crossover())]
        ea.observer = self.build_observer()

        ea.evaluator = self.build_evaluator()
        if self.multi_thread:
            print("Multi thread")
            pool = ThreadPool()
        if self.multi_process:
            print("Multi process")
            pool = multiprocessing.Pool()
        if self.multi_thread or self.multi_process:
            ea.evaluator = self.build_multiprocess_evaluator(pool)

        final_pop = ea.evolve(generator=self.build_generator(), evaluator=ea.evaluator,
                              max_evaluations=self.max_evaluations, pop_size=self.population_size)
        best_candidate = max(final_pop)

        if self.multi_thread or self.multi_process:
            pool.join()
            pool.close()

        trope_list = sorted([self.tropes[index] for index in best_candidate.candidate])

        seconds = time.time() - start

        summary = ", ".join(
            [self.execution_name, str(best_candidate.fitness), str(int(seconds))] + trope_list)
        self.log_summary_line(summary)

        return Solution(trope_list, best_candidate.fitness)

    def build_generator(self):
        def generator(random, args):
            return random.sample(self.tropes_indexes, self.number_of_tropes)

        return generator

    def build_evaluator(self):
        def evaluator(candidates, args):
            fitnesses = []
            for candidate in candidates:
                fitness = self._calculate_fitness(candidate)
                fitnesses.append(fitness)
            return fitnesses

        return evaluator

    def build_multiprocess_evaluator(self, pool):
        def evaluator(candidates, args):
            return pool.map(self._calculate_fitness, candidates)

        return evaluator

    def build_mutator(self):
        def mutator(random, candidates, args):
            mutants = []
            for candidate in candidates:

                mutant = candidate.copy()
                unused_tropes = set(set(self.tropes_indexes) - set(candidate))

                for index in range(0, len(candidate)):
                    if self.should_mutate(random):
                        new_trope = random.choice(list(unused_tropes))

                        unused_tropes.remove(new_trope)
                        unused_tropes.add(mutant[index])

                        mutant[index] = new_trope
                mutants.append(mutant)
            return mutants

        return mutator

    def build_crossover(self):
        def crossover(random, mom, dad, args):
            if self.should_crossover(random):
                block_init = random.randint(0, self.number_of_tropes)
                block_end = random.randint(0, self.number_of_tropes)

                if block_end < block_init:
                    block_end += self.number_of_tropes

                first_child = list(mom)
                second_child = list(dad)

                for index in range(block_init, block_end):
                    real_index = index % self.number_of_tropes
                    first_child[real_index] = dad[real_index]
                    second_child[real_index] = mom[real_index]

                first_child_set = set(first_child)
                second_child_set = set(second_child)

                candidate_elements = list(mom)
                random.shuffle((candidate_elements))
                while len(first_child_set) < self.number_of_tropes:
                    first_child_set.add(candidate_elements[0])
                    del candidate_elements[0]

                candidate_elements = list(dad)
                random.shuffle((candidate_elements))
                while len(second_child_set) < self.number_of_tropes:
                    second_child_set.add(candidate_elements[0])
                    del candidate_elements[0]

                return [list(first_child_set), list(second_child_set)]
            else:
                return [mom, dad]

        return crossover

    def build_observer(self):
        def observer(population, num_generations, num_evaluations, args):
            stats = fitness_statistics(population)
            best_individual = max(population, key=lambda x: x.fitness)

            log = [num_generations, stats['best'], stats['worst'], stats['mean'], stats['median'], stats['std']]
            log += sorted(best_individual.candidate)
            log = [str(round(value, 3)) for value in log]
            log.insert(0, self.execution_name)
            self.log_detail_line(", ".join(log))

            # print ("Geneneration={!s}. Best fitness={!s}".format(num_generations, best_individual.fitness))

        return observer

    def _retrieve_info_from_file(self):
        tropes_set = set()
        self.rules_by_trope = {}
        with open(self.path_to_rules) as file:
            for line in file:
                tropes_in_line = self._get_tropes_in_line(line)
                for trope in tropes_in_line:
                    tropes_set.add(trope)
                rule = self._get_rule_in_line(line)

                if rule is not None:
                    for antecedent in rule.antecedents:
                        if antecedent not in self.rules_by_trope:
                            self.rules_by_trope[antecedent] = []

                        self.rules_by_trope[antecedent].append(rule)

                        if antecedent not in self.rules_by_antecedent_and_consequent:
                            self.rules_by_antecedent_and_consequent[antecedent] = {}

                        for consequent in rule.consequents:
                            if consequent not in self.rules_by_antecedent_and_consequent[antecedent]:
                                self.rules_by_antecedent_and_consequent[antecedent][consequent] = []

                            self.rules_by_antecedent_and_consequent[antecedent][consequent].append(rule)

        self.tropes = sorted(tropes_set)
        if '' in self.tropes:
            self.tropes.remove('')
        self.tropes_indexes = list(range(0, len(self.tropes)))

    def _get_tropes_in_line(self, line):
        matches = self.ITEM_PATTERN.match(line)
        if not matches:
            return []

        elements = matches.group(1)
        items = elements.split(",")
        return [item.strip().replace("'", "") for item in items]

    def _get_rule_in_line(self, line):
        matches = self.RULE_PATTERN.match(line)
        if not matches:
            return None

        antecedents = self._get_set_from_group(matches.group(1))
        consequents = self._get_set_from_group(matches.group(2))
        confidence = float(matches.group(3))

        return AssociativeRule(antecedents, consequents, confidence)

    def _get_set_from_group(self, group):
        return frozenset(group.strip()[:-1].replace("'", "").split(","))

    def _build_default_path_to_rules(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(my_path, self.DEFAULT_APRIORI_FILE)

    def _get_max_tropes(self):
        return len(self.tropes_indexes)

    def _calculate_fitness(self, candidate):
        cache_key, cached_fitness = self.try_get_cached_fitness(candidate)
        if cached_fitness is not None:
            return cached_fitness

        fitness = 0
        tropes = self.get_tropes_as_short_names(candidate)

        for selected_trope in tropes:
            max_confidence = self.get_maximum_confidence_from_the_rest_to_the_trope(selected_trope, tropes)
            fitness += max_confidence

        self.cache.__setitem__(cache_key, fitness)
        return fitness

    def get_maximum_confidence_from_the_rest_to_the_trope(self, selected_trope, tropes):
        max_confidence = 0
        other_tropes = set([trope for trope in tropes if trope != selected_trope])
        rules = self.get_rules_based_in_antecedents_and_consequent_two_dicts(other_tropes, selected_trope)
        for rule in rules:
            max_confidence = max(max_confidence, rule.confidence)
        return max_confidence

    def add_rules_based_in_antecedents_and_consequent_one_dict(self, antecedents_superset, consequent, rules):
        for trope in antecedents_superset:
            if trope in self.rules_by_trope:
                for rule in self.rules_by_trope[trope]:
                    if rule not in rules and rule.antecedents.issubset(
                            antecedents_superset) and consequent in rule.consequents:
                        rules.add(rule)

    def get_rules_based_in_antecedents_and_consequent_two_dicts(self, antecedents_superset, consequent):
        rules = set()
        for trope in antecedents_superset:
            if trope in self.rules_by_antecedent_and_consequent:
                dictionary_of_consequents = self.rules_by_antecedent_and_consequent[trope]
                if consequent in dictionary_of_consequents:
                    for rule in dictionary_of_consequents[consequent]:
                        if rule not in rules and rule.antecedents.issubset(antecedents_superset):
                            rules.add(rule)
                        if rule.confidence == 1:
                            return rules
        return rules

    def get_tropes_as_short_names(self, candidate):
        tropes = list(map(lambda x: self.tropes[x], candidate))
        return tropes

    def try_get_cached_fitness(self, candidate):
        cache_key = ",".join([str(element) for element in sorted(candidate)])
        cached_fitness = self.cache.get(cache_key, None)
        return cache_key, cached_fitness

    def should_mutate(self, random):
        return random.random() <= self.mutation_probability

    def should_crossover(self, random):
        return random.random() <= self.crossover_probability

    def log_detail_line(self, content):
        self.log_line(content, self.details_file_name)

    def log_summary_line(self, content):
        self.log_line(content, self.summary_file_name)

    def log_line(self, content, file_name):
        if file_name is None:
            print(content)
        else:
            with open(file_name, "a") as file:
                file.write(content + "\n")
