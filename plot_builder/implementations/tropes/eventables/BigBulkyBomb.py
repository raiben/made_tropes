from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class BigBulkyBombTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "BigBulkyBomb"

    def get_long_name(self):
        return "Big Bulky Bomb"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/BigBulkyBomb"

    def get_rdf_element(self):
        return "BigBulkyBomb/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance has both a Red Herring bomb the size of a vending machine (the "
                "explosive liquids are actually maple syrup), and the actual bomb that takes a major part "
                "of a ship's basement and leads to an impressive blast."}

    def get_categories(self):
        return ['WeaponsAndWieldingTropes']

    def get_general_description(self):
        return "Any bomb that is at least as big as a car (either as one explosive or a cluster), is truly " \
            "made to make a huge blast.\nThe reason is that when you have Stuff Blowing Up, it's often " \
            "good to have bigger explosions. But that doesn't necessarily mean the actual bomb has to " \
            "be large, especially these days with high yield explosives. Before then, huge bombs were " \
            "the easiest way to make it clear the blast would be huge (in fiction and Real Life). With " \
            "high yield in a large amount, the blast goes Up to Eleven.\nMay overlap with the " \
            "Incredibly Obvious Bomb, because it's going to be hard to hide something this " \
            "big.\nCompare BFG, BFS, More Dakka, Wave Motion Gun, Kill Sat, Macross Missile Massacre, " \
            "There Is No Kill Like Overkill, Awesomeness Is Volatile, Outrun the Fireball.\nNot to be " \
            "confused with a work that flops horribly.\nThis is about the size of the bomb. The actual " \
            "explosion, its effects, or even the materials of the bomb, are irrelevant to whether an " \
            "example counts."

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
