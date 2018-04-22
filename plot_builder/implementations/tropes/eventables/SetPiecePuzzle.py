from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SetPiecePuzzleTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SetPiecePuzzle"

    def get_long_name(self):
        return "Set Piece Puzzle"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SetPiecePuzzle"

    def get_rdf_element(self):
        return "SetPiecePuzzle/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "They also did that three-unit container + five-unit container with a need to get four "
                "units. You know, the one from Die Hard with a Vengeance. Easy When You Know How."}

    def get_categories(self):
        return []

    def get_general_description(self):
        return "Puzzles in Adventure Games and Adventure-hybrids tend to fall into one of two categories: " \
            "the Lock and Key Puzzle, wherein the player must collect and use objects from around the " \
            "model world to effect changes to the state of the game, and the Set Piece Puzzle, which " \
            "consists of a single object to be manipulated.\nA Set Piece Puzzle is typically some sort " \
            "of device, usually a complicated machine, whose controls must be operated in a particular " \
            "way to solve the puzzle. Most often, interacting with the puzzle will bring up a new user " \
            "interface, distinct from the one used for playing most of the game.\nThere are many " \
            "possible sorts of set piece puzzles, often based on traditional non-computer puzzle toys. " \
            "For many years, the most popular of these was the Fifteen Puzzle or sliding-tile puzzle. " \
            "The Towers of Hanoi (with a small number of disks) is another favorite. A single round of " \
            "a Puzzle Game can often be found built into the mechanism.\nAdventure games have long used " \
            "a combination of the two types of puzzle, though the Set Piece Puzzle became " \
            "overwhelmingly popular to the point of excluding all others during the dominance of Myst- " \
            "clones. These puzzles were popular with designers because, isolated as they were from the " \
            "rest of the model world, they were technically easier to design and avoided the problem of " \
            "Combinatorial Explosion. A game consisting of only this sort of puzzle need not, for " \
            "example, provide a player inventory at all.\nTo the player, a mix of both puzzle types " \
            "adds variety, though overuse of the Set Piece Puzzle makes the puzzles feel disconnected " \
            "from the narrative, and can lead him to feel that he's dealing with a Solve the Soup Cans " \
            "puzzle.\nOn occasion, the player may be faced with a broken Set Piece Puzzle, and would " \
            "have to find an item that repairs the puzzle before it can be played. Examples of this are " \
            "sporadic, but games that feature both Set-Piece and Lock-And-Key will usually have at " \
            "least one.\nThe Set Piece Puzzle usually features Puzzle Reset."

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
