from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class RazorFlossTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "RazorFloss"

    def get_long_name(self):
        return "Razor Floss"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/RazorFloss"

    def get_rdf_element(self):
        return "RazorFloss/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Mentioned and seen in Die Hard with a Vengeance. As the two heroes are attempting to get "
                "from a bridge to a ship passing under it, Zeus says they should jump to the attached "
                "crane. John Mc Clane says the cables would cut them in half. Then when they use the winch "
                "on an SUV to climb down, the ship pulls the car off the bridge, leaving the hook and cable "
                "attached to the crane. As it swings, it hits a henchman. Zeus and John are then seen "
                "dragging him by his arms and legs. About eight feet apart..."}

    def get_categories(self):
        return ['WeaponsAndWieldingTropes']

    def get_general_description(self):
        return "Razor floss is when any long, thin material \u2014 string, thread, fine wire, etc \u2014 " \
            "is used as a weapon with Absurd Cutting Power. Odd as it may sound, strings can become " \
            "deadly weapons in the right hands. Besides restraining enemies and even controlling other " \
            "people's bodies against their will, or triggering traps, they can be pretty handy for " \
            "cutting. In many works of fiction, one skilled enough, can use strings to cut opponents or " \
            "even boulders, without hurting themselves. Naturally, monsters of the humanoid arachnid " \
            "variety can usually be counted on to be using this trope.\nFantasy settings generally have " \
            "this type of string made of human hair, while in more modern ones it's probably " \
            "monomolecular wire. In series less reliant on the Rule of Cool, the wire usually manifests " \
            "as garrotes or tripwires, with varyingly messy outcomes.\nWhat the audience sees usually " \
            "amounts to Sword Lines sans the sword. Can be counted on to inflict an absurdly Clean Cut " \
            "on its victims.\nIn reality, cables and metal wires can be used to inflict not so clean " \
            "but still pretty nasty wounds, provided they are of the right material and/or sufficient " \
            "force is applied. Cheese slicers frequently use thin metal wires stretched in a metal " \
            "frame to accomplish this trope, for instance. The monomolecular form is an eternal dream " \
            "of materials engineering: any material with enough tensile strength to be used as razor " \
            "floss could be woven into cables of the sort needed to build a Space Elevator. " \
            "note\u00A0Carbon nanotubes could fit the bill if some hitches can be solved: production " \
            "defects involving single atoms out of place can cut their strength by up to 85%\nA rarely " \
            "addressed aspect of the trope occurs when the razor floss breaks or is cut. In such " \
            "situations it may snap back at the user like a rubber band.\nCompare Whip Sword and Killer " \
            "Yoyo. Subtrope of Absurd Cutting Power."

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
