from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ContemplativeBossTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ContemplativeBoss"

    def get_long_name(self):
        return "Contemplative Boss"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ContemplativeBoss"

    def get_rdf_element(self):
        return "ContemplativeBoss/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: Simon walks like this when entering the Federal Reserve Bank "
                "vault he's about to rob."}

    def get_categories(self):
        return ['StockPoses']

    def get_general_description(self):
        return "He's the Big Boss, the Evil Overlord, or some other higher-up either good or bad. When he " \
            "receives people in his office, instead of looking at them directly, he talks with his back " \
            "to them while looking out the window, probably with his arms folded behind him.\nUsually " \
            "intended to convey that the character is so badass he can't be bothered to look at his " \
            "audience, this is sometimes used to indicate an internal conflict of some sort (depending " \
            "on his facial expression). Also has the bonus of keeping his identity a secret, up until " \
            "the Chair Reveal or Shadow Reveal\nIf the other character is a trusted lieutenant or " \
            "confidant, the senior figure may ask them to look out the window and \"Tell me what you " \
            "see\" in order to segue into making a point.\nThis may be part of The " \
            "Faceless.\n\nExamples"

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
