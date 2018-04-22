from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ShortLivedAerialEscapeTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ShortLivedAerialEscape"

    def get_long_name(self):
        return "Short Lived Aerial Escape"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ShortLivedAerialEscape"

    def get_rdf_element(self):
        return "ShortLivedAerialEscape/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance had a helicopter get destroyed, as well as one escape with "
                "moderate damage."}

    def get_categories(self):
        return ['Spectacle']

    def get_general_description(self):
        return "Oh no! The Bad Guys had the foresight to prepare an aerial getaway (usually in the form of " \
            "a helicopter).\nDoes the hero take it lying down because Gravity Is a Harsh Mistress? Of " \
            "course not. Especially not if he is a Hollywood action hero! He will destroy the vehicle " \
            "in a spectacularly explosive manner (because Everything Is Better With Explosions), but " \
            "usually not before he leaps into the flying vehicle in question to have one final, mano-a- " \
            "mano, brutal fistfight with the Big Bad in question."

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
