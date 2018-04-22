from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class InterruptedIntimacyTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "InterruptedIntimacy"

    def get_long_name(self):
        return "Interrupted Intimacy"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/InterruptedIntimacy"

    def get_rdf_element(self):
        return "InterruptedIntimacy/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "The end of Die Hard with a Vengeance involves the hero, John McClane, interrupting Simon, "
                "the villain, as he's about to get intimate with his wife. The normally stoic woman "
                "suddenly gets very angry at McClane."}

    def get_categories(self):
        return ['ComedyTropes']

    def get_general_description(self):
        return "A couple is about to have sex, or are in the midst of the act, but another person " \
            "interrupts somehow. They have to stop to deal with the interruption. This trope can be " \
            "played for comedy, drama or both. Can often lead to a Relationship Reveal. If they choose " \
            "to keep going, it's Coitus Uninterruptus. If they try and keep things secret (if there is " \
            "a knock on the door), it could lead to a Closet Shuffle. A subtrope of Moment " \
            "Killer.\nOften followed by a \"Don't you people know how to knock?\", because no one ever " \
            "locks their door when they're getting intimate.\nCompare to Caught with Your Pants Down " \
            "for the solo version of the trope. A supertrope of Primal Scene and Parents Walk In at the " \
            "Worst Time. Sister Trope to Sorry to Interrupt.\n\nExamples"

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
