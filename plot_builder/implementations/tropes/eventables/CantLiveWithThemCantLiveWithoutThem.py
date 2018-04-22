from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class CantLiveWithThemCantLiveWithoutThemTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "CantLiveWithThemCantLiveWithoutThem"

    def get_long_name(self):
        return "Can't Live With Them, Can't Live Without Them"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/CantLiveWithThemCantLiveWithoutThem"

    def get_rdf_element(self):
        return "CantLiveWithThemCantLiveWithoutThem/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Taken very literally in Die Hard with a Vengeance, wherein John McClane finds his new "
                "sidekick obnoxious, Zeus (said sidekick) despises him in return, but quite literally "
                "cannot live without him as the evil mastermind has set traps that he demands they solve "
                "together."}

    def get_categories(self):
        return ['FrenemyTropes']

    def get_general_description(self):
        return "A development often used in buddy films and romantic comedy. One person, often a loner- " \
            "type, is paired off with someone else against his/her will.\nHe can't stand the " \
            "person/situation and wishes for his old routine. When he gets his old routine back, he " \
            "suddenly realizes he misses that person a lot and does everything in his power to get her " \
            "back. Usually, happens when a bickering pair become Vitriolic Best Buds, or generate an " \
            "Aww, Look! They Really Do Love Each Other situation, whether it's a fraternal sort of love " \
            "among buddies, or romantic love.\nSometimes subverted to \"Can't live with 'em, can't kill " \
            "'em\".\nSee also Odd Couple.\nCompare We Want Our Jerk Back (when the resident Deadpan " \
            "Snarker's presence is sorely missed), Belligerent Sexual Tension.\n\nExamples"

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
