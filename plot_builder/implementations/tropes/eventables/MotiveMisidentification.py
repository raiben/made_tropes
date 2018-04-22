from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MotiveMisidentificationTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MotiveMisidentification"

    def get_long_name(self):
        return "Motive Misidentification"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MotiveMisidentification"

    def get_rdf_element(self):
        return "MotiveMisidentification/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "This is repeated with Hans' brother in Die Hard with a Vengeance where he first "
                "authorities to believe that he's a terrorist who wants revenge on McClane, but is actually "
                "using the confusion to set up a huge robbery. The fact that he would also get revenge on "
                "the cop who killed his brother was just icing on the cake. He then almost convinces the "
                "world that he carried out the robbery in order to destroy the gold rather than keep it, "
                "which as a mercenary he has actually been paid to do."}

    def get_categories(self):
        return ['Dialogue']

    def get_general_description(self):
        return "Disgusted by the Big Bad's squirrel-stealing antics, Steven Ulysses Perhero finally " \
            "corners the dastardly villain in the Abandoned Warehouse, where the following dialog takes " \
            "place:\nWhat a shocking twist! The hero... and naturally we the audience... assumed the " \
            "villain was up to something. And we were correct. He was. Unfortunately, the hero... and " \
            "naturally we the audience... were utterly incorrect about precisely what the villain was " \
            "up to.\nThis happens a lot when your hero is either too eager... or simply an " \
            "idiot.\nBasically, this trope is when a character comes to an erroneous conclusion about a " \
            "villain's motives based on his actions. While the Big Bad is certainly still a horrible " \
            "person, how he truly intends to go about it or why he's going about it in the first place " \
            "turns out to be something for which everyone else's suspicions were way off the mark. And " \
            "sometimes, the evil scheme isn't actually an evil scheme at all. In either case, the Big " \
            "Bad didn't try to fool the hero, or leave a false trail, or otherwise trick him in any " \
            "way. No, with this trope, the hero was fooling himself all along.\nSometimes the result of " \
            "paying attention to the Red Herring. Compare Hidden Agenda Villain (the villain is " \
            "concealing his true intentions) and Civilian Villain (the villain tricks the hero into " \
            "mistaking legitimate activites for nefarious ones in order to make the hero look bad and " \
            "make himself look like an innocent victim). Contrast Evil Plan for a more obvious motive " \
            "though this trope still might occur. See also Not Me This Time.\nThis is an Ending Trope, " \
            "so expect UNMARKED SPOILERS.\n\nExamples"

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
