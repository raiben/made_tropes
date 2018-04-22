from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ICanSeeYouTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ICanSeeYou"

    def get_long_name(self):
        return "I Can See You"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ICanSeeYou"

    def get_rdf_element(self):
        return "ICanSeeYou/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, Simon makes a phone call to the FBI car after the Wall "
                "Street subway station bombing. Despite Cobb making a stern order to the others to not tell "
                "Simon where they are, when Simon talks and gives them his bomb threat, he asks them who is "
                "in the van with them, and comments about Andy Cross and Phil Jarvis, the two federal "
                "agents in the van, and Jarvis's habit of fidgeting with his glasses. Once we see the "
                "emergency vehicles move out, we see that Simon is standing on the rooftop right nearby, "
                "watching them.\n Also when he demands to know why McClane didn't answer a certain payphone "
                "when he was supposed to. McClane tells him off, only to have Gruber say \"All you had do "
                "was say that there was a fat woman on the phone and that you couldn't get her to hang "
                "up\", thus revealing that he's watching them, as that is in fact exactly what had "
                "happened."}

    def get_categories(self):
        return ['HorrorTropes']

    def get_general_description(self):
        return "This is the creepy counterpart to Short-Distance Phone Call. It's when someone calls " \
            "another person from a cell phone. At first the person being called believes the caller to " \
            "be far away, but then the caller makes a comment like \"nice outfit\" or whatever, and the " \
            "person being called realizes he or she is within line of sight of the caller.\nNeedless to " \
            "say, it was even creepier before cell phones came around.\nAlso related to The Calls Are " \
            "Coming from Inside the House. See also Harassing Phone Call. Not to be confused with You " \
            "Can See Me?."

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
