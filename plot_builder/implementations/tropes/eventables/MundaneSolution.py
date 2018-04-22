from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MundaneSolutionTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MundaneSolution"

    def get_long_name(self):
        return "Mundane Solution"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MundaneSolution"

    def get_rdf_element(self):
        return "MundaneSolution/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, like the Terminator example above, Zeus could hotwire the "
                "car since as an electrician he knows how - or just stick his pocketknife in the ignition "
                "and turn."}

    def get_categories(self):
        return ['NarrativeDevices']

    def get_general_description(self):
        return "A very exotic device or problem, against which all manner of intricate, powerful devices " \
            "or strategies fail, is counteracted by something incredibly simple and mundane. It can't " \
            "be solved by their conventional solutions of More Dakka, Attack! Attack! Attack!, " \
            "diplomacy, or other Rule of Cool applications. Applied Phlebotinum, it seems, often turns " \
            "out to have a weakness to some household product.\nSupernatural beings in both Eastern and " \
            "Western mythology have a tendency for strange weaknesses, like a demon's obsessive- " \
            "compulsive need to count dropped grains of rice or a vampire's vulnerability to garlic and " \
            "sunlight.\nCan be preceded by someone Stating the Simple Solution, followed by a Face Palm " \
            "and/or a Glad I Thoughtof It moment.\nCompare Cutting the Knot. Contrast with Mundane " \
            "Utility, where something exotic is used to solve something mundane, and Weaksauce " \
            "Weakness, where a no less powerful individual gets strange weaknesses or power. Related to " \
            "Muggles Do It Better."

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
