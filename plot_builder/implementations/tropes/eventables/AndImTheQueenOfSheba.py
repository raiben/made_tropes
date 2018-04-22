from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class AndImTheQueenOfShebaTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "AndImTheQueenOfSheba"

    def get_long_name(self):
        return "And I'm the Queen of Sheba"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/AndImTheQueenOfSheba"

    def get_rdf_element(self):
        return "AndImTheQueenOfSheba/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance:"}

    def get_categories(self):
        return ['IAmAnIndex']

    def get_general_description(self):
        return "A form of sarcastic rejoinder, responding to an improbable statement with an even more " \
            "impossible statement.\nPopular forms include \"I'm the Queen of Sheba\" and \"I'm a " \
            "monkey's uncle\".\nCan lead to interesting results if Bob takes Alice at her word, which " \
            "may be because he's constitutionally deaf to sarcasm, doesn't expect her to disbelieve " \
            "him, or doesn't recognize the improbability of her statement. Or Bob may sarcastically " \
            "reference Alice's statement when his improbable statement is proved true; see Cue the " \
            "Flying Pigs.\nSee also Or My Name Isn't...."

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
