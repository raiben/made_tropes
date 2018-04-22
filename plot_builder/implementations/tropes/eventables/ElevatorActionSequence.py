from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ElevatorActionSequenceTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ElevatorActionSequence"

    def get_long_name(self):
        return "Elevator Action Sequence"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ElevatorActionSequence"

    def get_rdf_element(self):
        return "ElevatorActionSequence/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, the hero unwittingly enters an elevator with no less than "
                "five mooks disguised as law enforcement. The mooks make a number of gaffes, betraying that "
                "they are neither Americans nor cops, before McClane notices that one of them is wearing a "
                "familiar badge. An elevator gunfight ensues."}

    def get_categories(self):
        return ['VideogameSettings']

    def get_general_description(self):
        return "Some places are just designed for epic fight sequences. The lush scenery, the rippling " \
            "wind in the Badass Longcoat, the Greek choir blaring triumphantly in creepy tone...\nAnd " \
            "then there's the Elevator Action Sequence.\nThere are advantages to the Elevator Action " \
            "Sequence which make it so common in fiction. The main one is that it forces an arbitrary " \
            "restriction on the heroes: in a game or movie with many wide-open spaces, elevators (even " \
            "large, moving ones) tend to be static areas from which it is impossible to escape. The " \
            "situation forces characters into a fight whether they like it or not, and also moves " \
            "everyone automatically, so that we can pay more attention to the battle than where they're " \
            "going. That people on an elevator must be going somewhere is naturally a foregone " \
            "conclusion.\nSimilar to the elevator is the funicular, which is like an elevator that " \
            "moves along a diagonal plane instead of straight up and down. The funicular is also known " \
            "to attract its fair share of action.\nThis tropes is most common in early nineties Beat " \
            "'em Up games, which often used a moving platform rather than an enclosed elevator, " \
            "allowing the player to throw enemies off the side. Although those games are out of vogue " \
            "these days, examples can still be found occasionally in platformers, Action games and " \
            "RPGs.\nOften parodied by having two combatants fight their way onto the elevator, then " \
            "calmly wait for the elevator to arrive to resume fighting.\nLift of Doom is a specific " \
            "variant, usually found in Platform Games.\nThis trope is not to be confused with Elevator " \
            "Going Down. Its polar opposite is the lack of action in an Uncomfortable Elevator " \
            "Moment.\nCompare Elevator Snare, where the action comes from the villain or monster " \
            "reaching through the closing elevator doors. See also Evil Elevator. Sister trope of " \
            "Cable-Car Action Sequence. Has nothing to do with the Elevator Action series of video " \
            "games, which has you fighting people pretty much everywhere except the " \
            "elevators.\n\nExamples"

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
