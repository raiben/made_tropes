from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class NotSoStoicTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "NotSoStoic"

    def get_long_name(self):
        return "Not So Stoic"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/NotSoStoic"

    def get_rdf_element(self):
        return "NotSoStoic/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance has two female examples:\n Action Girl Connie Kowalski is pretty "
                "hard-boiled - as are almost all of the NYPD cops - but during the evacuation of the "
                "elementary school (when it's believed that a bomb has been planted there) she confesses "
                "that she might \"pee [her] pants.\"\n Katya, Simon Gruber's Dark Action Girl, never "
                "smiles, never speaks, never even makes a sound throughout all her scenes...until the "
                "film's climax, when she and Simon are interrupted by John McClane and Zeus Carver at a "
                "very inopportune moment - and she completely loses her cool, firing off a machine gun and "
                "screaming in rage."}

    def get_categories(self):
        return ['EmotionTropes']

    def get_general_description(self):
        return "Not So Stoic is what happens when a Stoic is pushed to the edge, and falls off. This is " \
            "when The Stoic loses his/her fa\u00E7ade and shows the world (or just their True " \
            "Companions) that they aren't an emotionless automaton. They may be good at hiding it but " \
            "they feel just as much as the rest of us. Likely to be very heartwrenching or extremely " \
            "terrifying or both.\nIn order to qualify, the show of emotion must be a significant one, " \
            "not just a small smile or subtle frown. This emotion need not be a \"negative\" one: Manly " \
            "Tears over the death of a teammate are certainly un-stoic, but so is unfettered joy over " \
            "their return.\nThese outpourings of emotion usually happen only a few times throughout the " \
            "series \u2014 if the stoic is showing emotion every other episode in every season, then " \
            "they aren't much of a stoic. However, these moments can also be used to illustrate a " \
            "character's growth towards becoming more open to others, in which case displays of emotion " \
            "\u2014 overt and subtle \u2014 would become more frequent over time.\nCompare with Not So " \
            "Above It All, OOC Is Serious Business and Sugar and Ice Personality. Contrast with Bad " \
            "Dreams (where The Stoic can keep it buttoned up \u2014 while awake), Rage Breaking " \
            "Point.\nWhen Played for Laughs or poorly written, it's an Out-of-Character " \
            "Moment.\nWARNING: Many Spoilers Ahead!\n\nExamples"

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
