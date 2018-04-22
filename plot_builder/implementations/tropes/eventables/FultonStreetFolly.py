from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class FultonStreetFollyTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "FultonStreetFolly"

    def get_long_name(self):
        return "Fulton Street Folly"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/FultonStreetFolly"

    def get_rdf_element(self):
        return "FultonStreetFolly/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance features a Wall Street subway bombing. (And subverts it by using "
                "the explosion to break into the Federal Reserve.)"}

    def get_categories(self):
        return ['JustForPun']

    def get_general_description(self):
        return "Even though there are 4.85 other boroughs in New York City (if you count Staten Island), " \
            "Lower Manhattan is used disproportionately often in many films and shows because it's " \
            "easier to film in; the Financial District empties out like a Ghost City on the weekends. " \
            "Many of the streets are already blocked off, and there are few residents to complain if an " \
            "entire neighborhood is overrun by camera crews and catering trucks.\nAs a result, anything " \
            "which is nominally set (or could be set) in other parts of the city will still have scenes " \
            "filmed downtown even if there's no compelling reason for the characters or action to be " \
            "there. A story about stock brokers makes sense, but for everything else, it's because it's " \
            "an easy shooting location.\nThe corner of Wall and Broad Streets is a popular spot because " \
            "it's been closed to traffic for years. It's also the location of Federal Hall, which " \
            "easily doubles for any other columned government building. Hardly a weekend goes by " \
            "without something being filmed there.\nThe trope name comes from Robert Fulton, whose 1807 " \
            "steamboat the Clermont was contemporaneously ridiculed as \"Fulton's " \
            "folly\"note\u00A0Previous steamboats had been woefully underpowered, leading the Unwashed " \
            "Masses\u2122 to believe the technology was completely infeasible, and who has a prominent " \
            "local street named for him and is buried at nearby Trinity Church.\nA subtrope of Big " \
            "Applesauce, where things happen in New York even though they could be reasonably set in " \
            "any other city, state or country.\nNot to be confused with Fulton Street Foley, the sound " \
            "of urban combat and mobilized emergency vehicles as Lower Manhattan falls under lockdown."

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
