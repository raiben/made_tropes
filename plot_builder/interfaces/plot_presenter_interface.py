from abc import abstractmethod

from utilities.base_factory import BaseFactory


class PlotPresenterInterface():
    @abstractmethod
    def __init__(self, coded_plot, trope_definitions, space):
        pass

    @abstractmethod
    def present(self):
        pass


class PlotPresenterFactory(BaseFactory):
    @classmethod
    def get_default_class(cls):
        from plot_builder.presenters.plot_presenter_with_basic_substitutions import PlotPresenterWithBasicSubstitution
        return PlotPresenterWithBasicSubstitution
