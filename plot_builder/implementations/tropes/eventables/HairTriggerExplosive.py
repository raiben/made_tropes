from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HairTriggerExplosiveTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HairTriggerExplosive"

    def get_long_name(self):
        return "Hair-Trigger Explosive"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HairTriggerExplosive"

    def get_rdf_element(self):
        return "HairTriggerExplosive/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Played straight and later subverted in Die Hard with a Vengeance. The liquid/gelled binary "
                "explosive used in the movie, PLX, actually exists but neither looks like it does in the "
                "movie nor does it explode on impact (instead requiring at least a blasting cap). It's also "
                "certainly not energetic enough that the amount collected on the tip of a paper clip would "
                "be enough to flip a chair. Seen later on, the actual bombs made with it feature more "
                "realistic amounts of priming explosives."}

    def get_categories(self):
        return ['TropesThatGoBoom']

    def get_general_description(self):
        return "There are powerful explosives, and can blow up almost everything. But Hollywood gives it a " \
            "nasty drawback: anything can make it explode. And I do mean anything. You have to be " \
            "super-careful or it will blow up. Or maybe it blows without any apparent reason.\nSome " \
            "Real Life explosives really have a hair trigger, some...don't. Note that most explosives " \
            "in fiction are not depicted this way. Usually in fiction, a plunger or a similar device " \
            "(e.g. with a blasting cap, fuse, Plunger Detonator, etc.) is used to safely blow up " \
            "explosives. But also in fiction, they get the volatility of explosives wrong, especially " \
            "TNT and dynamite.\nSubtrope of Stuff Blowing Up and The Last Straw. Supertrope of Nitro " \
            "Express. Also see Explosive Stupidity when someone doesn't know this. This applied to a " \
            "car intentionally is Molotov Truck, and unintentionally is Every Car Is a Pinto. " \
            "Compare/contrast Made of Explodium, in which something that should not be explosive " \
            "explodes anyway. If a nuclear weapon is treated like this, it's Artistic License \u2013 " \
            "Nuclear Physics."

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
