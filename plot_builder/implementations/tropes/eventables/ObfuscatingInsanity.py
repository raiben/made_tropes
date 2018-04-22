from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ObfuscatingInsanityTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ObfuscatingInsanity"

    def get_long_name(self):
        return "Obfuscating Insanity"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ObfuscatingInsanity"

    def get_rdf_element(self):
        return "ObfuscatingInsanity/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "John McClane has to fake this in Die Hard with a Vengeance, when a madman makes him wear a "
                "billboard insulting Afro-Americans while in his underwear. His future partner in "
                "adventures saves him by claiming his insanity, and he runs with it. And in general, "
                "McClane has his moments where he appears \"unhinged\". He does this for various reasons, "
                "either to fool and confuse his enemies, or to cope with the crap he has to go through."}

    def get_categories(self):
        return ['InfauxmationDesk']

    def get_general_description(self):
        return "It's pretty much a given that no-one takes crazy people seriously. It's also a given that " \
            "a lot of people give crazy people a wide berth lest they flip out on them. A lot of people " \
            "are aware of this and choose to take advantage of it, although their reasons for doing so " \
            "vary from one character to the next. Sometimes the apparent nutcase is actually perfectly " \
            "sane, other times they actually are a little on the Cloudcuckoolander side (or maybe more " \
            "than a little) but deliberately play it up to the Nth degree so that they appear to be far " \
            "crazier than they actually are. If they are not the point-of-view character, the question " \
            "may be left open.\nNot to be confused with Insanity Defense. Compare Obfuscating " \
            "Stupidity, where people pretend to be dimwitted instead of crazy.\n\nExamples"

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
