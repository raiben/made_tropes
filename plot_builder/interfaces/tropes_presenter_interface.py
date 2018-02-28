from abc import abstractmethod

from utilities.base_factory import BaseFactory


class TropesPresenterInterface():
    @abstractmethod
    def __init__(self, trope_definitions):
        pass

    @abstractmethod
    def present(self):
        pass


class TropesPresenterFactory(BaseFactory):
    @classmethod
    def get_default_class(cls):
        from plot_builder.presenters.tropes_presenter_as_json import TropesPresenterAsJSON
        return TropesPresenterAsJSON
