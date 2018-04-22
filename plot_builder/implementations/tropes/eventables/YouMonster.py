from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class YouMonsterTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "YouMonster"

    def get_long_name(self):
        return "You Monster!"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/YouMonster"

    def get_rdf_element(self):
        return "YouMonster/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, Simon actively attempts to avoid this trope when he reveals "
                "he lied about planting a bomb in a school."}

    def get_categories(self):
        return ['StockPhrases']

    def get_general_description(self):
        return "A Stock Phrase often directed towards a Big Bad or other particularly evil character. If a " \
            "character is saying this, it's a good indication that whoever the statement is directed " \
            "towards has either crossed the Moral Event Horizon in the character's eyes or just so " \
            "happened to press their Berserk Button. Variations exist (such as \"You're a monster\" or " \
            "\"You're rotten to the core!\").\nSee You're Insane! for when a character is calling " \
            "another crazy rather than evil. This can also lead to an Insult Backfire if a particularly " \
            "wicked villain takes pride in this label.\nThis trope can also be used to point out how " \
            "powerful the character is. Characters who possess that much power are considered monsters " \
            "by others because of their immense power. Similarly, it can be used in a show of amazement " \
            "when somebody does something that incredible.\nIn dramatic situations, this carries the " \
            "same weight as the Japanese This Is Unforgivable!. Unrelated to You Bastard, but there may " \
            "be overlap if the work's being fairly Anvilicious. May be the cause or effect (but mostly " \
            "cause) of a Villainous Breakdown.\nThis often shows up in What Measure Is a Non-Human? " \
            "scenarios, often targeted at a character who either is or is trying to be human.\nCompare " \
            "Complete Monster, in which the audience feels that the character is irredeemable. Contrast " \
            "with You Rebel Scum!, where the general populace in-story has been convinced that the " \
            "protagonists are evil. See also I Am a Monster when they consider themselves to be evil or " \
            "inhuman."

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
