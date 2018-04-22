from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class RedHerringTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "RedHerring"

    def get_long_name(self):
        return "Red Herring"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/RedHerring"

    def get_rdf_element(self):
        return "RedHerring/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance the main villain is presented as a mad bomber with a personal "
                "grudge against John McClane  for killing his brother who was the Big Bad of the first "
                "film. Turns out that was all a distraction to keep John and his unwitting civilian partner "
                "busy finding bombs, while he and his crew of professional mercenaries rob Fork Knox of its "
                "gold. It's later revealed that the villain  didn't even like his brother, and John dying "
                "from one of the bombs going off was just a bonus while doing the robbery, not a personal "
                "priority."}

    def get_categories(self):
        return ['InfauxmationDesk']

    def get_general_description(self):
        return "A clue that leads in the wrong direction.\nA red herring is a good red herring when it " \
            "interweaves itself into the story's events. For example, the murder victim may have been a " \
            "philanderer. His wife has no alibi. Aha! It was the wife!\nThe wife's lack of an alibi is " \
            "a red herring. It turns out the wife was shtupping somebody else at the time and didn't " \
            "want to provide that information. However, the deceased husband's philandering is what got " \
            "him killed, as it turns out, by his girlfriend's jealous husband. Philandering as a motive " \
            "is introduced for good cause, not just to set up suspicions about the wife's lack of an " \
            "alibi.\nThe supertrope to Red Herring Shirt, Red Herring Mole and Red Herring " \
            "Twist.\nCompare: Mistaken for Evidence, where the same result is caused by a mix-up " \
            "instead of intentional misdirection. The Untwist is when a plot twist is confused for a " \
            "Red Herring because it's too obvious, but turns out to have been genuine all along. See " \
            "also Chewbacca Defense, when a red herring is used to baffle your opponents, and Non " \
            "Sequitur, when an event does not make sense in context. See also Big Secret. Has nothing " \
            "to do with With This Herring. If a major star is used to sucker the audience rather than " \
            "the actual characters, you've just been served Dead Star Walking, or at least an aversion " \
            "of Narrowed It Down to the Guy I Recognize. Subject to being Spoiled by the Format: if " \
            "they've just found a plausible suspect, but there's 180 more pages to go, " \
            "well\u2026\nWarning: Due to the nature of this trope, unmarked spoilers ahead!"

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
