from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MotivationalLieTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MotivationalLie"

    def get_long_name(self):
        return "Motivational Lie"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MotivationalLie"

    def get_rdf_element(self):
        return "MotivationalLie/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, John McClane only gets Zeus Carver to help him investigate a "
                "spate of bombings by telling him that one bomb was discovered in a black neighborhood. "
                "Towards the end of the movie he admits that it wasn't anyplace close to where he'd claimed "
                "it was found."}

    def get_categories(self):
        return ['TruthAndLies']

    def get_general_description(self):
        return "Sometimes, the good guys get into a real jam where nothing seems like it's going to save " \
            "them. Maybe The Hero is getting his butt kicked by The Rival or the Big Bad. Maybe there's " \
            "some kind of impassable barrier between the hero and his objective, or some kind of mind " \
            "bending riddle has bogged them down. Whatever the case may be, it doesn't look good.\nThen " \
            "someone Genre Savvy like a friend who's a Guile Hero, the Cynical Mentor or The Lancer " \
            "comes along, and tells the hero a lie that gets them fired up with a fresh batch of Heroic " \
            "Resolve. Maybe he tells the hero that the Big Bad killed the hero's parents, despite the " \
            "fact the bad guy wasn't even in the country that night. (Or pushes a Berserk Button, for " \
            "example telling The Napoleon that his opponent called him a shrimp.) Maybe you say that " \
            "the Femme Fatale is waiting naked on the other side of the obstacle if the hero can just " \
            "get through it, or that the world's greatest chef will make the hero's Trademark Favorite " \
            "Food if he figures out the puzzle.\nWouldn't you know it, the hero suddenly manages to " \
            "turn the tide and start kicking ass.\nAlthough the person telling the lie usually isn't " \
            "thinking beyond the short term goal of overcoming an immediate problem, sometimes " \
            "(especially in the hands of a prophet) this is done with a long term goal in mind, such as " \
            "forcing Character Development or some other change in behavior or nature. In these cases " \
            "the lie may even become a form of Prophecy Twist.\nA Motivational Lie can also be a deadly " \
            "weapon in the hands of a cunning villain, who can use it to either manipulate the heroes " \
            "or turn others against them, such as in a Let's You and Him Fight scenario. As such it can " \
            "be a favorite weapon of the Manipulative Bastard, Magnificent Bastard, and The " \
            "Chessmaster.\nCompare and contrast with tropes such as Batman Gambit, Magic Feather, " \
            "Blatant Lies, Wounded Gazelle Gambit, Unreliable Expositor, Metaphorically True, False " \
            "Reassurance, and Let Them Die Happy. Closely related to the Placebo Effect."

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
