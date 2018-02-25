from abc import abstractmethod

from utilities.base_factory import BaseFactory


class RandomGeneratorInterface():
    @abstractmethod
    def set_seed(self, new_seed_as_integer):
        pass

    @abstractmethod
    def new_random_integer(self, minimum, maximum):
        pass


class RandomGeneratorFactory(BaseFactory):
    @classmethod
    def get_default_class(cls):
        from plot_builder.implementations.random_generator import RandomGenerator
        return RandomGenerator
