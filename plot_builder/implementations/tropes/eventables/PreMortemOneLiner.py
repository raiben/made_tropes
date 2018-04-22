from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PreMortemOneLinerTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "PreMortemOneLiner"

    def get_long_name(self):
        return "Pre-Mortem One-Liner"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PreMortemOneLiner"

    def get_rdf_element(self):
        return "PreMortemOneLiner/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: \"Say 'Hello' to your brother.\" (\"Yippee-ki-yay\" is uttered "
                "after the kill)."}

    def get_categories(self):
        return []

    def get_general_description(self):
        return "What's better than killing your most hated enemy? Sending them into the afterlife with " \
            "your voice in their ears and the knowledge of your badassery in their head, that's " \
            "what.\nAnother common staple of the Action Hero, this finishing quote need not be a One- " \
            "Liner, but the longer your little speech goes, the more likely the bad guy will find some " \
            "way to evade your intended killing blow or worse, make you Talk to the Fist. Consequently, " \
            "Genre Savvy heroes are advised to just Kill Him Already and save the pithy quotes for " \
            "immediately afterwards. Of course, sometimes (as in the Heroes and Matrix examples) it " \
            "seems that a Pre-Mortem One-Liner somehow paralyzes your enemy while you deliver it, or " \
            "maybe they're just courteous.\nThe monstrous equivalent is less articulate. Not to be " \
            "confused with a Pre Ass Kicking One Liner, which is used at the beginning of a fight; " \
            "these quotes are used to end the fight. Also related but different is a one-liner " \
            "delivered when escaping from battle.\nGive My Regards in the Next World and See You in " \
            "Hell are subtropes. Compare Bond One-Liner (aka Post-Mortem One-Liner) which is a humorous " \
            "aside for the audience. If the victim is the one speaking, it's Defiant to the End."

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
