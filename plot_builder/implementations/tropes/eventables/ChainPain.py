from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ChainPainTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ChainPain"

    def get_long_name(self):
        return "Chain Pain"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ChainPain"

    def get_rdf_element(self):
        return "ChainPain/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "John McClane does this on Targo in Die Hard with a Vengeance."}

    def get_categories(self):
        return ['WeaponsAndWieldingTropes']

    def get_general_description(self):
        return "Related to Whip It Good and Epic Flail, sometimes the chain link is all you need, without " \
            "the weight at the end. In less realistic works, skilled users can make Instant Knots with " \
            "it.\nA Badass Biker will often do this in a rumble. Also very common in 80s movies with " \
            "street gangs and among fictional Japanese delinquents. See also Fighting with Chucks, " \
            "Variable-Length Chain, Chained by Fashion and Whip It Good. Sub-Trope of Improvised " \
            "Weapon."

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
