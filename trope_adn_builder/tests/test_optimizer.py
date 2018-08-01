from unittest import TestCase

from trope_adn_builder.genetic_algorithm.optimizer import Optimizer


class TestOptimizer(TestCase):
    def test_when_no_list_provided_then_solution_has_43_tropes(self):
        optimizer = Optimizer(seed=123, mutation_probability=0.005, crossover_probability=1,
                              population_size=100)
        solution = optimizer.calculate_solution()
        self.assertEqual(len(solution.trope_list), 43, "Should've returned a solution of 43 tropes")

    def test_when_no_list_provided_and_multi_process_then_solution_has_43_tropes(self):
        optimizer = Optimizer(seed=123, max_generations=5, multi_process=True)
        solution = optimizer.calculate_solution()
        self.assertEqual(len(solution.trope_list), 43, "Should've returned a solution of 43 tropes")

    def test_when_no_list_provided_and_multi_threaded_then_solution_has_43_tropes(self):
        optimizer = Optimizer(seed=123, max_generations=5, multi_thread=True)
        solution = optimizer.calculate_solution()
        self.assertEqual(len(solution.trope_list), 43, "Should've returned a solution of 43 tropes")
