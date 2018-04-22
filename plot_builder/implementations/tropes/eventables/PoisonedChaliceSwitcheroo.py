from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PoisonedChaliceSwitcherooTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "PoisonedChaliceSwitcheroo"

    def get_long_name(self):
        return "Poisoned Chalice Switcheroo"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PoisonedChaliceSwitcheroo"

    def get_rdf_element(self):
        return "PoisonedChaliceSwitcheroo/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Although not involving poison, the alternate ending to Die Hard with a Vengeance plays "
                "with this trope. John McClane faces off with Simon Gruber, a rocket launcher with the "
                "sights removed on the table between them. They play the Simon Says game, with the rocket "
                "being turned each time Simon Gruber answers a question correctly. Eventually he gets a "
                "question wrong, so John tells him to pull the trigger. However Simon turns the rocket "
                "launcher one more time before doing so, convinced the muzzle will then be facing towards "
                "John. He's wrong."}

    def get_categories(self):
        return ['NarrativeDevices']

    def get_general_description(self):
        return "Two enemies are sharing a drink and one of the glasses contains poison. At least one of " \
            "them will attempt to poison the other by switching glasses while the other's back is " \
            "turned. Common joke is either that someone poisons a chalice, then they get switched over, " \
            "or someone knows he's got a poisoned drink, and tries to find a chance to dispose of it " \
            "without being obvious, or pretending to swap the glasses, waiting for the enemy to really " \
            "swap them and drink. A common trick (most famously seen in The Princess Bride) is to " \
            "poison both drinks.\nA less lethal variation is to shake up a bottle or can of soda or " \
            "beer.\nA Discredited Trope, more often parodied (or made fun of) than played straight " \
            "these days. When switched and switched back, this is Two Rights Make a Wrong."

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
