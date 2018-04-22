from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class NotableNonSequiturTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "NotableNonSequitur"

    def get_long_name(self):
        return "Notable Non Sequitur"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/NotableNonSequitur"

    def get_rdf_element(self):
        return "NotableNonSequitur/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, there is an offhand reports about thirteen dump trucks being "
                "stolen the night before. Later in the film, it is revealed that these trucks are being "
                "used by the villains to cart off the gold they have stolen."}

    def get_categories(self):
        return ['NarrativeDevices']

    def get_general_description(self):
        return "In a Detective Drama, any time a piece of dialogue comes along which is off-the-cuff, not " \
            "followed up and unrelated to everything, you can tell it's going to be very important. If " \
            "a suspect turns up late and says \"Sorry I'm late, my car was stolen yesterday\", the " \
            "alleged car theft will be significant. If the detective remarks that the suspect has a " \
            "nice keychain and the suspect says \"Yeah, it's from my old fraternity\", the insignia on " \
            "the keychain will turn up later to reveal that the suspect and victim were in college " \
            "together. Basically this happens whenever the writer can't find a neat way of dropping an " \
            "important clue into an existing conversation.\nSee also Chekhov's Gun.\nRelated to the Law " \
            "of Conservation of Detail"

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
