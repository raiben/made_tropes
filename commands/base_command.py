from abc import abstractmethod

from collections import defaultdict


class BaseCommand():
    class __metaclass__(type):
        __inheritors__ = defaultdict(list)

        def __new__(meta, name, bases, dct):
            klass = type.__new__(meta, name, bases, dct)
            for base in klass.mro()[1:-1]:
                meta.__inheritors__[base].append(klass)
            return klass

    def __init__(self, arguments):
        self.arguments = arguments

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    @abstractmethod
    def get_description():
        pass
