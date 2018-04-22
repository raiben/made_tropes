from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class CriminalMindGamesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "CriminalMindGames"

    def get_long_name(self):
        return "Criminal Mind Games"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/CriminalMindGames"

    def get_rdf_element(self):
        return "CriminalMindGames/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Subverted in Die Hard with a Vengeance with \"Simon\" playing a Simon-Says type game with "
                "the main character through the first half of the movie in order to prevent a bomb from "
                "being detonated. Subverted in that  it's shown to simply be a way to get McClane (and the "
                "entire NYPD) out of the way while Simon pulls off a heist of the federal reserve."}

    def get_categories(self):
        return ['Plots']

    def get_general_description(self):
        return "The detectives are on the heels of a very unbalanced criminal who has left them a trail of " \
            "clues to follow \u2014 these clues aren't meant to cover the criminal's tracks, but, for " \
            "the criminal's (and the audience's) entertainment, are usually intended to be a test of " \
            "their intellect, or their investigatory skills, as though the criminal wants to see if the " \
            "detectives are worthy of catching him.\nNot only do the detectives oblige the nutter and " \
            "follow his breadcrumb trail, they tend to give up all conventional routes of " \
            "investigation. Usually they are the minutest step behind their quarry right until the end. " \
            "Sometimes the criminal wishes to distract or trap the detectives, sometimes they want them " \
            "to uncover some other truth along the way, but usually they're just being a real smartass. " \
            "Sometimes the clues are hidden in the Serial Killer's Calling Card or in its gruesome " \
            "souvenirs. There is often a Breaking Speech (or \"The Reason You Suck\" Speech) and a Kirk " \
            "Summation (or \"World of Cardboard\" Speech) exchange between The Protagonist and " \
            "antagonist some time before the climax.\nThe criminal will often warn the investigators " \
            "that there will be consequence for cheating on the game.\nCan overlap with Absurdly High- " \
            "Stakes Game.\nThese people often enjoy wordplay. Anagrams abound, as well as sentences " \
            "with a carefully designed second meaning, and proper nouns which are conveniently also " \
            "real words (\"wait a minute, does he mean Jim Trashcompacter?\").\nSee also Linked List " \
            "Clue Methodology for a number of non-(or at least less) criminal scavenger hunts. Compare " \
            "The Walrus Was Paul.\n\nExamples"

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
