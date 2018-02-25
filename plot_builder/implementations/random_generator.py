import random

from plot_builder.interfaces.random_generator_interface import RandomGeneratorInterface


class RandomGenerator(RandomGeneratorInterface):
    @staticmethod
    def set_seed(new_seed_as_integer):
        return random.seed(new_seed_as_integer)

    @staticmethod
    def new_random_integer(minimum, maximum):
        return random.randint(minimum, maximum)
