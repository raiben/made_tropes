from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class LastRequestTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "LastRequest"

    def get_long_name(self):
        return "Last Request"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/LastRequest"

    def get_rdf_element(self):
        return "LastRequest/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane asks Gruber if he has any aspirin. This doesn't help "
                "McClane escape his predicament, but it does give them a lead on where to find Gruber "
                "later."}

    def get_categories(self):
        return ['Dialogue']

    def get_general_description(self):
        return "Something you request right before you die. The opportunity may be offered to you by your " \
            "executioner out of personal kindness or cultural tradition."

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
