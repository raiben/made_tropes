from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class BondVillainStupidityTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "BondVillainStupidity"

    def get_long_name(self):
        return "Bond Villain Stupidity"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/BondVillainStupidity"

    def get_rdf_element(self):
        return "BondVillainStupidity/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Simon in Die Hard with a Vengeance handcuffs John McClane and Zeus to a bomb on a ship and "
                "leaves them to die, instead of shooting them and blowing up the ship after."}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "Bond Villain Stupidity is a form of Genre Blindness commonly exhibited by villains. It " \
            "occurs when a villain fails to kill the hero when he has him cornered, incapacitated, or " \
            "otherwise defenseless, thus giving the hero a chance to escape and later come back to " \
            "defeat the villain. It is so named because it occurs frequently in James Bond movies. A " \
            "common form of Bond Villain Stupidity is to place the hero in an elaborate Death Trap from " \
            "which he can escape (slow dipping mechanisms over pits of sharks, alligators, or lava are " \
            "perennial favorites). If you ever asked why the villains don't just shoot him then use " \
            "their pets/lava to dispose of the body, then congratulations, you are smarter than the " \
            "average megalomaniac. Also common is the inability to resist a Just Between You and Me " \
            "moment before putting the hero in said death trap. Several variants of this one made the " \
            "Evil Overlord List.\nOften includes Monologuing, accompanied by stock quotes such as \"You " \
            "Have No Chance to Survive! I don't think we'll meet again... Goodbye!\"\nIf they actually " \
            "expect the hero to die before their eyes, it's Prepare to Die.\nObjective logic aside, a " \
            "big part of the reason for this trope is because \"mundane\" kills do indeed seem to annoy " \
            "audiences; see Dropped a Bridge on Him.\nThis is so common that the Hypercompetent " \
            "Sidekick pointing out the inherent flaws in this trope and suggesting a more pragmatic " \
            "solution has become a trope on its own: Stating the Simple Solution. For more generalized " \
            "villainous incompetence, see Villain Ball. For those villains that avert this trope, see " \
            "Dangerously Genre Savvy."

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
