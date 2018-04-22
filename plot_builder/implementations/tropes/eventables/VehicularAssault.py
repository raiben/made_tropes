from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class VehicularAssaultTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "VehicularAssault"

    def get_long_name(self):
        return "Vehicular Assault"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/VehicularAssault"

    def get_rdf_element(self):
        return "VehicularAssault/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "The end of Die Hard with a Vengeance: McClane kills the Big Bad's helicopter, and thus the "
                "Big Bad.\n In Live Free or Die Hard, he kills a helicopter. With a car."}

    def get_categories(self):
        return ['BossBattle']

    def get_general_description(self):
        return "The someone or something has run up against an enemy. It's time to do battle, just the " \
            "heroes, and... a vehicle?\nThis is when someone has to go up against what essentially " \
            "amounts to a vehicular foe. Maybe the Big Bad is too weak to just attack on foot, and does " \
            "it from the protection of his vehicle. Maybe it's just a bunch of Mooks in a helicopter. " \
            "Worst yet, the vehicle itself is the villain, either through malevolent AI or spiritual " \
            "possession. In any case, the battle isn't between individuals or groups so much as between " \
            "people.\nThe end result is that the heroes have an opponent that's faster, more durable, " \
            "and deadlier than just an ordinary, squishy human. Furthermore, the villain(s) can usually " \
            "take shots at the heroes, either by shooting at the heroes from the safety of their " \
            "vehicle or by using weapons mounted on the vehicle itself. Failing that, there's always " \
            "the old standby of Car Fu. Helicopters in this situation are rather liable to become " \
            "makeshift blenders, whether or not the helicopter or its occupants have a better way of " \
            "dispatching the heroes.\nWhen this appears, there's usually three ways it'll play out:\n " \
            "The hero takes out the vehicle directly, either by hitting a weak point, manipulating it " \
            "into a trap, or just using a very big gun.\n The hero takes out the driver, thereby " \
            "causing the vehicle to crash, or at least stop moving and attacking.\n The hero can't take " \
            "it out, and is forced to run away.\nNote that just a character killing a vehicle does not " \
            "qualify it for this trope, nor does two vehicles duking it out with each other. The " \
            "attacker must be fighting the victim from or with the vehicle for it to qualify. It can " \
            "qualify for this trope if the victim does have a vehicle, but one which is at a severe " \
            "disadvantage against the attacker's vehicle and can't fight off the attacker (jetpack " \
            "versus spaceship, motorcycle versus helicopter, car versus helicopter, etc.). As a general " \
            "rule, things like jetpacks and skateboards do not qualify as a vehicle.\nHelicopters tend " \
            "to be a particular favorite for this trope, but anything from a motorcycle to a spaceship " \
            "can qualify. Also, while this trope is not limited to villains, it's considerably rarer to " \
            "see heroic examples since it's one of the dirtier techniques in the book.\nPops up " \
            "frequently in Video Games, though not uncommon in other media. Also Truth in Television; " \
            "see pretty much any vehicle designed for combat purposes, or any crime where the weapon " \
            "was a car or other vehicle.\nCompare Vehicular Combat, where the emphasis is on the " \
            "vehicles fighting each other, and Vehicular Sabotage, when a character's vehicle is " \
            "maliciously tampered with before they drive it. Not to be confused with Car Fu, which is " \
            "when the vehicle is turned into a makeshift weapon. However, the two are likely to " \
            "overlap."

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
