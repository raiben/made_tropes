import json
from collections import OrderedDict

from plot_builder.interfaces.plot_presenter_interface import PlotPresenterInterface


class PlotPresenterWithBasicSubstitution(PlotPresenterInterface):
    def __init__(self, coded_plot, trope_definitions, space):
        self.coded_plot = coded_plot
        self.trope_definitions = trope_definitions
        self.space = space

    def present(self):
        list_of_dictionaries = [self.build_dictionary_from_event(index, event)
                                for index, event in enumerate(self.coded_plot.list_of_events)]
        printable_events = json.dumps(list_of_dictionaries, indent=2)
        print(printable_events)

    def build_dictionary_from_event(self, index, event):
        dictionary = OrderedDict()
        trope_definition = self.trope_definitions[event.trope_id]

        dictionary["Event id"] = index

        characters = [self.space.list_of_characters[character_id] for character_id in event.list_of_character_ids]
        places = [self.space.list_of_places[place_id] for place_id in event.list_of_place_ids]
        objects = [self.space.list_of_objects[object_id] for object_id in event.list_of_object_ids]
        dictionary["Basic description"] = self.trope_definitions[
            event.trope_id].get_description_with_replaced_existents(characters, places, objects)

        dictionary["Trope name"] = trope_definition.__class__.__name__
        dictionary["Trope information"] = trope_definition.get_info()
        dictionary["Existents"] = OrderedDict()
        for role, character in zip(trope_definition.get_sorted_role_characters_array(), characters):
            dictionary["Existents"][character] = role
        for role, object in zip(trope_definition.get_sorted_role_objects_array(), objects):
            dictionary["Existents"][object] = role
        for role, place in zip(trope_definition.get_sorted_role_places_array(), places):
            dictionary["Existents"][place] = role

        return dictionary
