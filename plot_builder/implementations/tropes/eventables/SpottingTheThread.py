from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SpottingTheThreadTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SpottingTheThread"

    def get_long_name(self):
        return "Spotting the Thread"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SpottingTheThread"

    def get_rdf_element(self):
        return "SpottingTheThread/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane gets in an elevator with several terrorists "
                "disguised as cops and security. He notices they're using terminology incorrectly, "
                "referring to the elevator as a \"lift\" (a European/British term) and a weather report as "
                "raining \"dogs and cats\" (the wrong order). McClane is visibly suspicious, but what "
                "confirms it is when he spots \"Detective Otto\" is wearing a police badge that belongs to "
                "a friend of his. McClane being McClane, things inevitably get violent."}

    def get_categories(self):
        return ['DisguiseTropes']

    def get_general_description(self):
        return "This is when an impersonator has an almost perfect disguise, only to ruin it with a " \
            "seemingly inconspicuous mistake. Perhaps the imposter blurted out something out-of- " \
            "character (or a personal catchphrase), or accidentally revealed that they're left-handed. " \
            "\nThis can more easily occur during a round of Bluff the Impostor, and can be a sub-trope " \
            "of Spot the Impostor except that their target generally has no advance knowledge that " \
            "there is an imposter in the first place.\nRelated to Pull the Thread as this is often what " \
            "leads to it. Compare Saying Too Much, a more incriminating version. See also Conviction by " \
            "Counterfactual Clue, when this gets even more unrealistic. Often overlaps with Imposter " \
            "Forgot One Detail. Compare For Want of a Nail.\nWhen applied to a dream test, it's A " \
            "Glitch in the Matrix."

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
