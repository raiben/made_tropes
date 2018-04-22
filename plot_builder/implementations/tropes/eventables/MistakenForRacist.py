from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MistakenForRacistTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MistakenForRacist"

    def get_long_name(self):
        return "Mistaken for Racist"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MistakenForRacist"

    def get_rdf_element(self):
        return "MistakenForRacist/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance , the Big Bad of the film, portrayed by Jeremy Irons, "
                "blackmails John McClane into standing on a street corner in the middle of Harlem wearing a "
                "sandwich board that reads \"I Hate Niggers\". He very nearly gets killed by a gang of "
                "local street thugs but is saved by Zeus. Note that when they were filming the scene, Bruce "
                "Willis wore a sign saying \"I Hate Everyone\", because they were genuinely worried that "
                "he'd get killed. They photoshopped it after.\n In order to avoid racism the TV edit keeps "
                "the \"I Hate Everyone\" sign. Of course this means the black people in the neighbourhood "
                "appear to attack McClane for no real reason leading to some Unfortunate Implications."}

    def get_categories(self):
        return ['RaceTropes']

    def get_general_description(self):
        return "A character says or accidentally does something that is interpreted by everyone else as " \
            "being racist, and they proceed to chew him out for it or start shunning him for it. If it " \
            "is not the main plot for the story, it can be quickly cleared up, but otherwise, any " \
            "attempt to prove that he's not really racist ends up backfiring and making him look even " \
            "more racist. Appearing to look xenophobic in front of foreigners is a common variant.\nIf " \
            "the people who believe this person prejudiced are themselves prejudiced, they'll be proud " \
            "of him, leading to Your Approval Fills Me with Shame. The character may also try " \
            "(unconvincingly) to deny it by saying \"Some of My Best Friends Are X.\"\nCompare " \
            "Discriminate and Switch, Stereotype Reaction Gag, Calling Me a Logarithm.\n\nExamples"

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
