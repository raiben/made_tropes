from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class EvenEvilHasLovedOnesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "EvenEvilHasLovedOnes"

    def get_long_name(self):
        return "Even Evil Has Loved Ones"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/EvenEvilHasLovedOnes"

    def get_rdf_element(self):
        return "EvenEvilHasLovedOnes/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Used again the Die Hard with a Vengeance when Simon reveals that McClane killed his "
                "brother, Hans, despite Simon revealing that he hated his brother."}

    def get_categories(self):
        return ['EvilTropes']

    def get_general_description(self):
        return "Being evil doesn't always mean hatred and negativity 24/7. Even evil characters (and real " \
            "people) can find someone to love. Often, that love is twisted, a cause for villainy, or an " \
            "act but sometimes a work can show an evil character's love is genuine and deep. This " \
            "serves to humanize the character, to give the hero doubts about fighting him/her, or to " \
            "provide a weakness for the hero to exploit. At an extreme end, can provoke Mama Bear or " \
            "Papa Wolf reactions if they are threatened, or prompt the loved ones to Avenging the " \
            "Villain.\nEven Bad Men Love Their Mamas and Unholy Matrimony are subtropes.\nCompare Even " \
            "Evil Has Standards, Morality Pet, Mad Scientist's Beautiful Daughter, Daddy's Little " \
            "Villain, Villainous Friendship. If the evil character in question is a mook, and said love " \
            "brings them in conflict with their own boss, that's Even Mooks Have Loved Ones. Can often " \
            "overlap with Moral Myopia when the villain sees no problem with their own methods, until " \
            "those methods are turned on the ones THEY love."

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
