from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class StockScreamTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "StockScream"

    def get_long_name(self):
        return "Stock Scream"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/StockScream"

    def get_rdf_element(self):
        return "StockScream/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "While John McClaine is driving through a park in Die Hard with a Vengeance, he's asked if "
                "he's aiming for people. \"No...\" (Wilhelm scream) \"Except for maybe that mime.\""}

    def get_categories(self):
        return ['SoundFXTropes']

    def get_general_description(self):
        return "Overused Stock Sound Effects can screw with a TV viewer's attention span \u2014 repeated " \
            "use makes them instantly recognizable to those in the know. One of the worst offenders is " \
            "the Stock Scream \u2014 one of several vocal effects used when a character has to scream " \
            "and the sound the actor recorded isn't loud or piercing enough. From the popularity of " \
            "some stock \"scream\" effects, you would think they were the only ones in existence. " \
            "Currently there are about 15 commonly used stock screams, most of which have yet to be " \
            "named.\nLooking for an Instant Wilhelm Scream? Look no further."

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
