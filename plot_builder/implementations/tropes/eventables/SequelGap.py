from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SequelGapTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SequelGap"

    def get_long_name(self):
        return "This entry is trivia, which is cool and all, but not a trope. On a work, it goes on the " \
            "Trivia " \
            "tab.\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\n\t\t\n\t\tSequel " \
            "Gap"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SequelGap"

    def get_rdf_element(self):
        return "SequelGap/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance (1995) and Live Free or Die Hard (2007) \u2014 12 years."}

    def get_categories(self):
        return ['Trivia']

    def get_general_description(self):
        return "A film or other literary work where a sequel is released long, long after the original " \
            "work. May sometimes be a Trilogy Creep, very often related to Development Hell. Does not " \
            "apply to Sequels In Name Only, Sequel Series, or Franchise Reboots. This Trope is for " \
            "honest-to-goodness sequels. See also Capcom Sequel Stagnation, and a related Webcomic " \
            "trope, Schedule Slip.\n\nExamples"

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
