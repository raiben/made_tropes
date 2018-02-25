from plot_builder.entities.coded_plot_entities import CodedPlotEntity, CodedPlotEventEntity
from plot_builder.entities.space_entity import SpaceEntity
from plot_builder.interfaces.plot_presenter_interface import PlotPresenterFactory
from plot_builder.interfaces.random_generator_interface import RandomGeneratorFactory
from plot_builder.interfaces.trope_definitions_aggregator_interface import TropeDefinitionsAggregatorFactory
from plot_builder.use_cases.base_use_case import BaseUseCase


class BuildRandomPlotUseCase(BaseUseCase):
    MAXIMUM_NUMBER_OF_EVENTS = 1000
    MAXIMUM_NUMBER_OF_EXISTENTS = 3000
    MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE = int(MAXIMUM_NUMBER_OF_EXISTENTS / 3)

    def __init__(self):
        self.random_generator = RandomGeneratorFactory.get_instance()
        self.space = SpaceEntity()
        self.trope_definition_aggregator = TropeDefinitionsAggregatorFactory.get_instance()
        self.all_tropes = self.trope_definition_aggregator.get_all_tropes_as_sorted_array()

    def run(self):
        self.build_space()
        self.build_random_coded_plot()
        self.build_plot_presenter()

        return self.plot_presenter.present()

    def build_random_coded_plot(self):
        self.coded_plot = CodedPlotEntity()
        number_of_events = self.get_random_number_of_events()
        for index in range(0, number_of_events):
            event = self.build_random_event()
            self.coded_plot.list_of_events.append(event)

    def build_random_event(self):
        coded_plot_event = CodedPlotEventEntity()
        coded_plot_event.trope_id = self.get_random_trope_id()

        trope_definition = self.all_tropes[coded_plot_event.trope_id]
        for index in range(0, len(trope_definition.get_sorted_role_characters_array())):
            existent_id = self.get_random_existent_id()
            coded_plot_event.list_of_character_ids.append(existent_id)
        for index in range(0, len(trope_definition.get_sorted_role_places_array())):
            existent_id = self.get_random_existent_id()
            coded_plot_event.list_of_place_ids.append(existent_id)
        for index in range(0, len(trope_definition.get_sorted_role_objects_array())):
            existent_id = self.get_random_existent_id()
            coded_plot_event.list_of_object_ids.append(existent_id)

        return coded_plot_event

    def build_space(self):
        self.space.list_of_characters = ["C{}".format(index)
                                         for index in range(0, self.MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE)]
        self.space.list_of_objects = ["O{}".format(index)
                                      for index in range(0, self.MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE)]
        self.space.list_of_places = ["P{}".format(index)
                                     for index in range(0, self.MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE)]

    def build_plot_presenter(self):
        self.plot_presenter = PlotPresenterFactory.get_instance(self.coded_plot, self.all_tropes, self.space)

    def get_random_number_of_events(self):
        return self.random_generator.new_random_integer(0, self.MAXIMUM_NUMBER_OF_EVENTS - 1)

    def get_random_trope_id(self):
        return self.random_generator.new_random_integer(0, len(self.all_tropes) - 1)

    def get_random_existent_id(self):
        return self.random_generator.new_random_integer(0, self.MAXIMUM_NUMBER_OF_EXISTENTS_BY_TYPE - 1)
