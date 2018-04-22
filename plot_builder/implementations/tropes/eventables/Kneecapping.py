from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class KneecappingTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "Kneecapping"

    def get_long_name(self):
        return "Knee-capping"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/Kneecapping"

    def get_rdf_element(self):
        return "Kneecapping/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: \"Have to take the safety catch off.\" Dakka\n In the next "
                "film, the Big Bad again does this to the sidekick."}

    def get_categories(self):
        return ['ATorturedIndex']

    def get_general_description(self):
        return "The act of deliberately damaging someone's knees to incapacitate them or limit their " \
            "mobility. This can be performed by shooting the victim's kneecaps, or by striking them " \
            "with kicks, melee weapons, or other up close and personal means.\nSince this is an " \
            "extremely painful type of injury, knee-capping can be used as a brutal form of Mutilation " \
            "Interrogation. This can kill two birds with one stone for the savvy torturer, as the " \
            "permanently debilitating nature of the injury makes it much more difficult for the victim " \
            "to escape. Tearing up all that muscle, those sinews and those complicated bones with a " \
            "bullet would in Real Life probably leave you crippled for life, if you weren't killed by " \
            "blood loss or shock.\nKnee-capping can also be used as a tactic in combat to drastically " \
            "hamper the mobility of an opponent. Needless to say, this type of fighting is a bit too " \
            "dirty for most upstanding protagonists, so it is often reserved for villains, Anti Heroes, " \
            "and Combat Pragmatists.\nIn real life, it is often not the kneecap itself that is the " \
            "target of these attacks, as opposed to the joint and tissue beneath it. A piece of Common " \
            "Knowledge is that kneecaps don't repair when broken/shattered. They do when treated " \
            "properly, it just takes a very long time. Additionally, unlike in film and television, you " \
            "would never actually aim to shoot out someone's kneecap or leg to disable a target in such " \
            "a manner (see the Real Life section below).\nA sub-trope of Trying to Catch Me Fighting " \
            "Dirty. Compare Agony of the Feet for other mobility hampering injuries, and An Arm and a " \
            "Leg for occasions when the legs are lost completely."

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
