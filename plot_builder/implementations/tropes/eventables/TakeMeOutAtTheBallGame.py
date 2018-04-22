from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class TakeMeOutAtTheBallGameTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "TakeMeOutAtTheBallGame"

    def get_long_name(self):
        return "Take Me Out at the Ball Game"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/TakeMeOutAtTheBallGame"

    def get_rdf_element(self):
        return "TakeMeOutAtTheBallGame/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, the terrorists claim they want John McClane to go to Yankee "
                "Stadium to collect a clue to stop the bomb that will blow up a school. In truth, there is "
                "a sniper at the stadium who will shoot him if he shows up. (Zeus appears at the stadium, "
                "but given the orders were to kill both, he lives)"}

    def get_categories(self):
        return ['JustForPun']

    def get_general_description(self):
        return "A person getting murdered at a sporting event. Creates a situation where there might be " \
            "hundreds of witnesses, thousands of suspects, but isn't necessarily easier for the " \
            "detectives.\nTitle is a reference to the unofficial anthem of baseball. The quote is " \
            "Silent Hunter's re-write of the lyrics of the chorus."

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
