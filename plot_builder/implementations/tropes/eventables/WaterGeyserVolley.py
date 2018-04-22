from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class WaterGeyserVolleyTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "WaterGeyserVolley"

    def get_long_name(self):
        return "Water Geyser Volley"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/WaterGeyserVolley"

    def get_rdf_element(self):
        return "WaterGeyserVolley/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "John McClane is shot out of a sewer pipe 10 feet into the air in Die Hard with a "
                "Vengeance."}

    def get_categories(self):
        return ['ComedyTropes']

    def get_general_description(self):
        return "This is a Comedy trope that can be seen very often in Western Animation. A character comes " \
            "across a geyser and becomes innately curious about it as he looks directly into it, when " \
            "the geyser suddenly erupts in a torrent of water that thrusts the character up into the " \
            "air. This sometimes results in the victim bouncing around on the top of the spray.\nThis " \
            "is not Truth in Television, because a person will just get thrown back a few feet from " \
            "such high water pressure. And be cooked by the superheated water.\nThis is often a " \
            "mechanic in video games (usually of the Platformer genre), and the geysers end up being " \
            "moving and/or slippery platforms.\nCan go hand-in-hand with: Making a Splash\n\nExamples"

    def get_sorted_role_characters_array(self):
        return []
        # TODO: please, return the role names as a list

    def get_sorted_role_objects_array(self):
        return []
        # TODO: please, return the object names as a list

    def get_sorted_role_places_array(self):
        return []
        # TODO: please, return the place names as a list

    def get_number_of_events(self):
        return 0
        # TODO: how many events will this trope consist on

    def get_events_from_coded_plot_entity(self, coded_plot_entity):
        return []
        # TODO: please, build a list of EventEntity

    def get_description_with_replaced_existents(
            self, list_of_characters, list_of_places, list_of_objects):
        return ""
        # TODO: Please, give a description of the trope with the real provided
        # actors
