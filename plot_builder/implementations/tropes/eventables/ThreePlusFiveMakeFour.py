from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ThreePlusFiveMakeFourTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ThreePlusFiveMakeFour"

    def get_long_name(self):
        return "Three Plus Five Make Four"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ThreePlusFiveMakeFour"

    def get_rdf_element(self):
        return "ThreePlusFiveMakeFour/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In the movie Die Hard with a Vengeance, the two main characters must solve this type of "
                "puzzle in order to disarm a bomb near a public fountain. In the original script, the bomb "
                "was a Chekhov's Gun, as the movie would end with McClane planting the bomb on the bad "
                "guy's helicopter, and upon discovery one of them asks if anyone has a four gallon jug (in "
                "the final script the bomb was used for something else entirely without the puzzle being "
                "brought up again)."}

    def get_categories(self):
        return []

    def get_general_description(self):
        return "You have two containers, one that holds 3 liters and one that holds 5 liters, and access " \
            "to a water source. Place exactly 4 liters of water into a third container (one that holds " \
            "at least 5 liters, so that you can't simply fill the container to the brim and be done " \
            "with it).\nThis puzzle dates back at least as far as the 1920s, and quite possibly earlier " \
            "still.\nThe solution is as follows:\nFirst, fill the 3-liter container to the brim.\nPour " \
            "the 3 liters of water into the 5-liter container.\nFill the 3-liter container again.\nPour " \
            "water from the 3-liter container into the 5-liter container until it is filled to the " \
            "brim. This should leave you with 1 liter of water in the 3-liter container.\nEmpty out the " \
            "5-liter container, then pour the 1 liter of water into it from the 3-liter " \
            "container.\nFill the 3-liter container once more, then pour the water from both containers " \
            "into the third container.\nAn alternate solution with fewer fills:\n Fill the 5-liter " \
            "container.\n Fill the 3-liter container from the 5-liter container, leaving 2 liters.\n " \
            "Empty the 3-liter container. Then, pour the remaining 2 liters from the 5- to the 3-liter " \
            "container.\n Refill the 5-liter, then fill the 3-liter from the 5-liter container. Leaving " \
            "4 liters in the 5-liter container.\nAnother alternate solution, though this one requires " \
            "several assumptions: The containers must have at least one line of symmetry when looking " \
            "at them from the top, and they must have a constant width. (Cylinders or rectangular " \
            "prisms meet this requirement.)\n Fill the 5-liter container, then place one part of the " \
            "bottom down, and tilt it until the water level makes a straight line from the upper edge " \
            "of the bottom to the bottom edge of the lip.\n Do the same thing with the 3-liter " \
            "container, and pour it into the 5-liter container.\n 2.5 + 1.5 = 4\nIt bears noting that " \
            "this puzzle, like many other stock puzzles, is usually difficult only because the solver " \
            "is overthinking it. In practice, if you actually have the two jugs, and you just start " \
            "filling one jug and pouring it into the other, the solution presents itself very quickly. " \
            "(This is incorporated in some tellings of the riddle, which demand that you come up with " \
            "the answer in less than a minute, as an Aesop about the value of trying things out rather " \
            "than just sitting there thinking.)\nMaths nerd bit: You're looking for the smallest x and " \
            "y that satisfy 3x\u22125y=4; then fill the 3-liter x times, pouring it into the 5-liter " \
            "when full, and emptying the 5-liter when it's full (which you'll do y times). The solution " \
            "is x=3 and y=1. The alternate solution up there is the dual formulation, 5x\u22123y=4 " \
            "(x=2, y=2). From here, two details present themselves: one, that it's easily adaptable to " \
            "other values other than 3 and 5, and two, that a solution exists only if the target value " \
            "is either a factor or a multiple of the highest common factor of the container sizes (e.g. " \
            "you can't get 4 liters from 6- and 3-liter containers)."

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
