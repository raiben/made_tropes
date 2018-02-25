from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface
from plot_builder.interfaces.trope_definitions_aggregator_interface import TropeDefinitionsAggregatorInterface
from plot_builder.implementations.tropes.archetypes import *


class TropeDefinitionsAggregatorAllTropes(TropeDefinitionsAggregatorInterface):
    def __init__(self):
        self.list_of_tropes = []
        trope_definition_classes = TropeDefinitionInterface.__subclasses__()
        for trope_definition_class in trope_definition_classes:
            self.list_of_tropes.append(trope_definition_class())
        self.list_of_tropes.sort(key=lambda definition: definition.__class__.__name__)

    def get_all_tropes_as_sorted_array(self):
        return self.list_of_tropes
