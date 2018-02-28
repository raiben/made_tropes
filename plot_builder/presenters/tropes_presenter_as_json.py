import json
from collections import OrderedDict

from plot_builder.interfaces.tropes_presenter_interface import TropesPresenterInterface


class TropesPresenterAsJSON(TropesPresenterInterface):
    def __init__(self, trope_definitions):
        self.trope_definitions = trope_definitions

    def present(self):
        tropes_dictionary = OrderedDict()
        for trope_definition in self.trope_definitions:
            tropes_dictionary[trope_definition.__class__.__name__] = {
                "type": trope_definition.get_type(),
                "role_characters": trope_definition.get_sorted_role_characters_array(),
                "role_places": trope_definition.get_sorted_role_places_array(),
                "role_objects": trope_definition.get_sorted_role_objects_array(),
                "info": trope_definition.get_info(),
                "description": trope_definition.get_description_with_replaced_existents(
                    ["<{}>".format(name) for name in trope_definition.get_sorted_role_characters_array()],
                    ["<{}>".format(name) for name in trope_definition.get_sorted_role_places_array()],
                    ["<{}>".format(name) for name in trope_definition.get_sorted_role_objects_array()]
                )
            }

        print(json.dumps(tropes_dictionary, indent=2))
