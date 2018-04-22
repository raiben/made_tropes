from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class StereotypeReactionGagTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "StereotypeReactionGag"

    def get_long_name(self):
        return "Stereotype Reaction Gag"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/StereotypeReactionGag"

    def get_rdf_element(self):
        return "StereotypeReactionGag/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Happens a lot between John McClane and his partner-of-circumstance Zeus in Die Hard with a "
                "Vengeance. McClane asks, for instance, \"can you pick this lock?\" Zeus calls him a racist "
                "(\"Oh, all black dudes know how to pick locks, right?\"), then when McClane calls him out "
                "on it, says that, yes, yes he can.\n Earlier in the movie, when McClane asks if Zeus can "
                "hotwire a car, Zeus says:\n But as it turns out, Zeus doesn't know how to use a gun."}

    def get_categories(self):
        return ['CharacterReactionIndex']

    def get_general_description(self):
        return "One character assumes another has a certain item, skill, or relationship based on a " \
            "stereotype, be it racial, gender, or orientation-based.\nFor instance, someone asks a gay " \
            "character if he can design clothes, or a latino character if he has any relatives who work " \
            "on cars, or a black character if he knows where to buy weed.\nThe character being asked is " \
            "incensed, and outraged that his friend would believe such outlandish and bigoted " \
            "assumptions.\nThen, of course, it turns out he does, in fact, have the skill or item in " \
            "question readily at hand, and calmly gives up the info with a calm \"yeah, okay.\" This " \
            "allows writers to indulge ethnic and gender assumptions with built in Lampshade Hanging. " \
            "The best way of putting it is \"but he didn't know that.\"\nCompare I Resemble That " \
            "Remark. Contrast with Stop Being Stereotypical, Mistaken for Racist, Discriminate and " \
            "Switch. Also see Hypocritical Humor.\n\nExamples"

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
