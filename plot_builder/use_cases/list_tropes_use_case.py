from plot_builder.interfaces.trope_definitions_aggregator_interface import TropeDefinitionsAggregatorFactory
from plot_builder.interfaces.tropes_presenter_interface import TropesPresenterFactory
from plot_builder.use_cases.base_use_case import BaseUseCase


class ListTropesUseCase(BaseUseCase):
    def __init__(self):
        self.trope_definition_aggregator = TropeDefinitionsAggregatorFactory.get_instance()
        self.all_tropes = self.trope_definition_aggregator.get_all_tropes_as_sorted_array()

    def run(self):
        self.build_tropes_presenter()
        return self.tropes_presenter.present()

    def build_tropes_presenter(self):
        self.tropes_presenter = TropesPresenterFactory.get_instance(self.all_tropes)

    def get_random_number_of_events(self):
        return self.random_generator.new_random_integer(0, self.MAXIMUM_NUMBER_OF_EVENTS - 1)

    def get_random_trope_id(self):
        return self.random_generator.new_random_integer(0, len(self.all_tropes) - 1)

    def get_random_existent_id(self):
        return self.random_generator.new_random_integer(0, self.MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE - 1)
