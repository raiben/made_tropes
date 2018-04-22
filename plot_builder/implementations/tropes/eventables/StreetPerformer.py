from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class StreetPerformerTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "StreetPerformer"

    def get_long_name(self):
        return "Street Performer"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/StreetPerformer"

    def get_rdf_element(self):
        return "StreetPerformer/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, when they're tearing through Central Park in a stolen Taxi, "
                "barely missing several picnickers, Samuel L. Jackson asks Bruce Willis \"Are you AIMING "
                "for those people?\" \"No, no... well, maybe that mime.\""}

    def get_categories(self):
        return ['CharactersAsDevice']

    def get_general_description(self):
        return "People performing stunts on streets (say, a One-Man Band) in order to get money from " \
            "spectators, often seen at any renaissance fair. Also known as \"buskers\" in Ireland (a " \
            "word ultimately of Celtic and Iberian origin).\nOne common element is having a hat (or " \
            "some other container) out in front in which passersby can toss money into.\nCommonly an " \
            "Acceptable Target in the mass media, likely to be stigmatized either as New-Age Retro " \
            "Hippie or \"wannabe performer with no talent\". However, quite a few of these artists have " \
            "become successful and even world-famous.\nStreet Musician and Organ Grinder are Sub " \
            "Tropes."

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
