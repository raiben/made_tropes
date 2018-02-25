from abc import abstractmethod

from utilities.base_factory import BaseFactory


class TropeDefinitionsAggregatorInterface():
    @abstractmethod
    def get_all_tropes_as_sorted_array(cls):
        pass


class TropeDefinitionsAggregatorFactory(BaseFactory):
    @classmethod
    def get_default_class(cls):
        from plot_builder.implementations.trope_definitions_aggregator_all_tropes import \
            TropeDefinitionsAggregatorAllTropes
        return TropeDefinitionsAggregatorAllTropes
