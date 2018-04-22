from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class GiveMyRegardsInTheNextWorldTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "GiveMyRegardsInTheNextWorld"

    def get_long_name(self):
        return "Give My Regards in the Next World"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/GiveMyRegardsInTheNextWorld"

    def get_rdf_element(self):
        return "GiveMyRegardsInTheNextWorld/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Heroic example in Die Hard with a Vengeance, McClane says \"Say hello to your brother\" "
                "just before he kills Simon Gruber, referring to Hans Gruber who McClane killed in the "
                "first film."}

    def get_categories(self):
        return ['StockPhrases']

    def get_general_description(self):
        return "A stock Pre-Mortem One-Liner which usually comes in two flavours:\nFrom the killer to the " \
            "victim. Often told from the villain to the Disposable Woman or anyone close to The Hero " \
            "that they're about to kill. When it's The Hero saying this, it's usually to Mooks " \
            "attempting to avenge their boss or to an enemy upon the issue of a Duel to the " \
            "Death.\nFrom the victim to their friends or sometimes the killer themselves. The Tear " \
            "Jerker variant which is usually found among the True Companions when one of them is dying " \
            "in the arms of one of his comrades, usually along the lines of \"Meet you on the other " \
            "side\".\nThis One-Liner is sometimes used in the context of a Mercy Kill but it's " \
            "rarer.\nRelated to See You in Hell and We Will Meet Again.\nAs this accompanies a " \
            "character's death, beware of spoilers on this page."

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
