from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MalcolmXeroxTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MalcolmXerox"

    def get_long_name(self):
        return "Malcolm Xerox"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MalcolmXerox"

    def get_rdf_element(self):
        return "MalcolmXerox/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Zeus from Die Hard with a Vengeance definitely qualifies. In fact, Samuel L. Jackson "
                "researched the role to look and act exactly like Malcolm X himself."}

    def get_categories(self):
        return ['JustForPun']

    def get_general_description(self):
        return "A form of Straw Character, this trope is specific to black characters.\nThese characters " \
            "are often very far to the left of the political spectrum, and usually militant. These " \
            "black radicals or activists are depicted as a bunch of hypocritical, irrational, paranoid, " \
            "unreasonable, lazy, bigoted, race-card-playing, conspiratorial raving loons. Even within " \
            "black TV shows and movies, they're very rarely depicted as respectable or intelligent " \
            "people whose opinion is of any real merit. When it comes to black TV and films, this could " \
            "be an attempt by some black writers to subvert the stereotype of black people agreeing " \
            "with these particular views. In the process, they ended up creating a Straw Character. " \
            "Needless to say these characters can easily veer into Unfortunate Implications territory. " \
            "Some even see these characters as tactics to discredit the image of conscious black people " \
            "in mainstream media.\nThe Trope Namer is Malcolm X, who achieved fame during the American " \
            "civil rights movement for his aggressive and hard-line views on race; however, he was " \
            "actually a subversion in that after going on his pilgrimage to Mecca he started to promote " \
            "racial equality and unfortunately got killed for it by hard-line black " \
            "nationalists.note\u00A0Unless you believe the conspiracy theories that say " \
            "otherwise\nCompare with Straw Feminist, Angry Black Man."

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
