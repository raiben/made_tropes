from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class RevengeOfTheSequelTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "RevengeOfTheSequel"

    def get_long_name(self):
        return "Revenge of the Sequel"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/RevengeOfTheSequel"

    def get_rdf_element(self):
        return "RevengeOfTheSequel/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance"}

    def get_categories(self):
        return ['DiscreditedTrope']

    def get_general_description(self):
        return "In many sequel names, particularly in schlock horror, the title, or sub-title, describes " \
            "some kind of return, revenge, reaction, counter-force, backlash, etc. that usually implies " \
            "it's a direct consequence of one of the previous installments. The movie's tagline might " \
            "even be something like \"And this time, It's Personal.\"\nAlso expect \"Son of _____\" and " \
            "\"Bride of _____\".\nCompare There's No \"B\" in Movie. Subtrope of Stock Subtitle."

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
