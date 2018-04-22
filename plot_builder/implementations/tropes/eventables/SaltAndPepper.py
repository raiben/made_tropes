from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SaltAndPepperTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SaltAndPepper"

    def get_long_name(self):
        return "Salt and Pepper"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SaltAndPepper"

    def get_rdf_element(self):
        return "SaltAndPepper/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "John McClane and Zeus Carver in Die Hard with a Vengeance. Subverted in that neither one "
                "of them have much of a respect for authority."}

    def get_categories(self):
        return ['DuoTropes']

    def get_general_description(self):
        return "A variation on the Odd Couple, involving a white person and a black person. Usually, the " \
            "white person is a strait-laced by-the-book type, while the black person is a funky, urban " \
            "type who doesn't have much respect for authority. Most commonly, they're cops, assigned as " \
            "partners after their old partners die/get disgusted and walk away. Generally, the two make " \
            "a fairly good team if they can work out the personality clashes, with the strengths of one " \
            "covering for the weaknesses of the other.\nSalt And Pepper seems to be becoming subverted " \
            "more often today due to increased racial awareness, so that it's the white person who's a " \
            "rebellious hothead, and the black person is smart and savvy. Another common subversion is " \
            "for the black guy to be uptight and the white guy to be relaxed. An alternate version is a " \
            "pairing of a white character with a Hispanic character called a Cafe con Leche. Please " \
            "note, however, that being two different races isn't enough for this trope. There must be " \
            "some kind of contrast in their personalities for it to work.\nFor American media, this may " \
            "be more common in the movies (Lethal Weapon, Die Hard 1 2 and 3) than on TV as television " \
            "shows often seem more segregated.\nSee also Black Best Friend. Irishman And A Jew is an " \
            "older variation of this trope. If they're not different races, the trope is All Work vs. " \
            "All Play."

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
