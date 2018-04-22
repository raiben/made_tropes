from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class TheDragAlongTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "TheDragAlong"

    def get_long_name(self):
        return "The Drag-Along"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/TheDragAlong"

    def get_rdf_element(self):
        return "TheDragAlong/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance has Zeus, who got roped into John McClane's bomb-diffusing "
                "adventure after trying to protect McClane from a street gang without realizing what was "
                "happening. They become friends by the end."}

    def get_categories(self):
        return ['Starwars']

    def get_general_description(self):
        return "Most of the hero team is eager and ready to go on another adventure, face peril, and " \
            "explore new regions. Not this guy. This guy would rather stay home, where it's safe. Maybe " \
            "he doesn't really think the trip is worth it, maybe he doesn't care, or maybe he just has " \
            "an aversion to painful, dangerous situations. Yet the team wants him to come, so, kicking " \
            "and screaming if necessary, he comes along anyway.\nNone too happy about constantly being " \
            "dragged along on adventures, you can usually find this one complaining and making " \
            "sarcastic remarks, but, when push comes to shove, you can bet that he'll show his heroic " \
            "traits in the clutch.\nContrast the Sour Supporter, who doesn't believe it will work but " \
            "will contribute anyway (although with sardonic comments), and The Load or The Millstone, " \
            "who may or may not be supportive but whose actions and/or very existence work against the " \
            "heroes' purposes.\nA variation on The Complainer Is Always Wrong and I Do Not Like Green " \
            "Eggs and Ham. Most Drag Alongs are also Butt Monkeys or Chew Toys, which may justify their " \
            "reluctance.\nCompare Refusal of the Call, Cowardly Sidekick, Cowardly Lion, Grumpy Bear, I " \
            "Just Want to Be Normal, Dragged by the Collar.\nContrast The Team Wannabe but do not " \
            "confuse with the Tagalong Kid. Also not to be confused with Dragged into Drag."

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
