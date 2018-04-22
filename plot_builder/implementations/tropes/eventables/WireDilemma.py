from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class WireDilemmaTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "WireDilemma"

    def get_long_name(self):
        return "Wire Dilemma"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/WireDilemma"

    def get_rdf_element(self):
        return "WireDilemma/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Subverted in Die Hard with a Vengeance, where the bomb squad guy is cutting wires left, "
                "right, and center, but nothing happens at all... he stays to the end. When the timer hits "
                "0, he finds it's a fake."}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "In fiction-land, disarming just about any bomb is a matter of cutting the right wires in " \
            "the right order \u2014 usually each wire will be given a distinctive color, and an " \
            "assistant will read from a manual: \"Clip the red wire, then the blue wire, then the " \
            "yellow wire...\" The implication is generally that if the wrong wire is cut, the bomb will " \
            "explode instantly, killing the person disarming it and everyone else in the blast radius. " \
            "Combines Race Against the Clock with the need to make absolutely sure you're making the " \
            "right decision for dramatic tension. Of course it's never as easy as just following the " \
            "manual \u2014 generally some kind of subversion is used to heighten tension.\nKnown " \
            "permutations:\n The red wire isn't there.\n All the wires are the same color.\n Cutting " \
            "any wire at all is a bad play.\n The hero is colorblind, or the lighting makes him " \
            "effectively colorblind.\n The guy reading from the manual changes his mind between maybe " \
            "red, maybe blue ... are any of 'em green?\n The guy with the manual says \"red\", the hero " \
            "says \"Frack it!\" and yanks out the whole snarled-up mess of wires, or cuts the blue one " \
            "and... there is a big explosion.\n The guy with the manual tells the hero to cut the red " \
            "wire. He goes on to do so, but just as he's about to cut it (sweat in his eyes and all) " \
            "\u2014 or already has \u2014 the guy says \"NO!! STOP!! It's not that one!\". Even if " \
            "there's no manual guy, the hero will usually change his mind about which wire to cut at " \
            "the last second.\n The color is one the cutter doesn't know: taupe, ochre, turquoise, " \
            "umber, etc.\n The guy reading from the manual says something like \"It says to cut the " \
            "blue wire..\" * snip* \".. after cutting the red one..\"\n The hero just throws the bomb " \
            "out the window.\n An expert arrives and simply flips the OFF switch on the bomb to " \
            "deactivate it.\n The hero/expert futilely tries to defuse the bomb. The other person " \
            "watching (usually another member of the team if the hero is trying to defuse the bomb, or " \
            "if the expert is defusing the bomb, then the hero is watching) gets frustrated and shoves " \
            "the hero/expert out of the way and punches the control panel. This may result in two " \
            "different endings. One is that the bomb shuts down to the hero/expert's surprise, or two, " \
            "the bomb skips the timer and just detonates, Hilarity usually ensues.\n The bomb " \
            "explodes... harmlessly (with a shower of confetti or powder, maybe a large \"BANG\" sign), " \
            "and we're shown it was all a test that the hero just failed.\n There is more than one " \
            "bomb. If the bomb goes off, the next guy knows to cut a different wire.\n There ARE no " \
            "wires.\nAt no point is there a plausible explanation as to why a homemade bomb should " \
            "conform to any color-code standard at all, especially since the designer obviously never " \
            "intended for it to be disarmed in the first place. The Fridge Logic as to why he would be " \
            "using multiple-colored wires also never comes up, even though in a home-made bomb, all the " \
            "wire should have come from the same single-colored spool.\nNaturally, a bomb intended for " \
            "air-dropping (or a missile warhead) really shouldn't have any trick wires to start with. " \
            "Still, it makes you wish there were an Override Command.\nExample of a Dead Horse Trope, " \
            "partly since in real life the electronics of a bomb are both simpler and more fragile than " \
            "Hollywood would have you believe. The Wire Dilemma has a minor Sub-Trope in the Wrong " \
            "Wire. See also Bomb Disposal and Cut the Fuse.\n\nExamples"

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
