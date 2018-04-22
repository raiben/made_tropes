from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class StrappedToABombTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "StrappedToABomb"

    def get_long_name(self):
        return "Strapped to a Bomb"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/StrappedToABomb"

    def get_rdf_element(self):
        return "StrappedToABomb/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Happens to MacClane and Zeus in Die Hard with a Vengeance after they are captured by the "
                "Big Bad."}

    def get_categories(self):
        return ['WeaponsAndWieldingTropes']

    def get_general_description(self):
        return "A favorite execution method of Dastardly Whiplash types, this trope involves the villain " \
            "tying a captured character to an armed explosive device. Cue frantic searches for the " \
            "Conveniently-Placed Sharp Thing and attempts to disarm the device while still tied up (for " \
            "example, a memorable scene in a Scooby-Doo, Where Are You! episode where Shaggy and Scooby " \
            "attempt to put out a bomb fuse with their butts). Generally, though, disaster gets averted " \
            "by the Big Damn Heroes showing up to get their pal out of Dodge before he/she gets blasted " \
            "to a pile of thin gruel. Bonus points if the rescue team cuts it so close that they and " \
            "their rescuee wind up Outrunning the Fireball afterward.\nIt operates on a similar " \
            "principle to Chained to a Railway, in that it's essentially a timed Death Trap. However, " \
            "the myriad ways to trigger a bomb means that villains can have lots of fun with this... " \
            "for instance, rigging the bomb to go off when somebody tries to rescue the victim (this is " \
            "sure to mess with the victim's psyche a lot, and can also subvert a Big Damn Heroes moment " \
            "by turning it into a Senseless Sacrifice.)\nSee also Death Trap and Bound and Gagged, as " \
            "this is a Sub-Trope of both, and Explosive Leash and Why Am I Ticking?, which are Sister " \
            "Tropes. Riding the Bomb is also closely related."

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
