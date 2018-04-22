from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class LetsDanceTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "LetsDance"

    def get_long_name(self):
        return "Let's Dance"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/LetsDance"

    def get_rdf_element(self):
        return "LetsDance/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance, bomb squad technician Charlie Veiss says this to a bomb he's "
                "attempting to defuse:"}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "A Stock Phrase most often heard right before an action scene and used as a Pre Ass Kicking " \
            "One Liner. The Hero comes across a random Big Bad, or one of his mooks. When the Hero " \
            "announces his intention to fight/kill said Bad Guy, he might laugh a little sadistically " \
            "before a reply of \"Let's Dance\". Sometimes this is accompanied by a cracking of " \
            "knuckles, or even of the victim's neck.\nCompare Bring It. Dance Battler also takes this " \
            "literally."

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
