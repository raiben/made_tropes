from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ScrewTheMoneyIHaveRulesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ScrewTheMoneyIHaveRules"

    def get_long_name(self):
        return "Screw the Money, I Have Rules!"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ScrewTheMoneyIHaveRules"

    def get_rdf_element(self):
        return "ScrewTheMoneyIHaveRules/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "John McClane in Die Hard with a Vengeance won't take money from criminals, even when it's "
                "a hell of a lot easier than getting the shit kicked out of him by them."}

    def get_categories(self):
        return ['CharactersAsDevice']

    def get_general_description(self):
        return "For some people, money isn't an issue. Maybe a hero's morals and convictions are so strong " \
            "that he can never be bought out, not even for all the money and riches in the world. Maybe " \
            "someone is so committed to a goal he'll spend all the money he has to in order to reach " \
            "it. Or perhaps there are some people who just don't need the money; the warm fuzzy feeling " \
            "after doing a good deed is reward enough. Whatever the reason, wealth comes second to " \
            "personal values. Even a chance at matrimony may not be enough.\nNote that this does not " \
            "necessarily mean \"wealth comes second to good personal values.\" This is a very common " \
            "trope for Knight Templar types, and outright Chaotic Evil villains can enact it too, as " \
            "can people who prioritize amusement over personal gain.\nOf course, it's not unknown for " \
            "it to be a Secret Test of Character with a Sweet and Sour Grapes\nCompare Money Is Not " \
            "Power, Keep the Reward, Honor Before Reason, What You Are in the Dark, Doing It for the " \
            "Art. The Last DJ is a specific character type who is likely to do this, although he may " \
            "pay for it, especially in missed opportunities. If the character's refusal includes making " \
            "the situation even worse for the offerer, that's a Bribe Backfire.\nContrast Screw the " \
            "Rules, I Have Money! (the obvious inversion of this trope), Only in It for the Money, and " \
            "Every Man Has His Price.\n\nExamples"

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
