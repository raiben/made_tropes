from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class AskAStupidQuestionTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "AskAStupidQuestion"

    def get_long_name(self):
        return "Ask a Stupid Question..."

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/AskAStupidQuestion"

    def get_rdf_element(self):
        return "AskAStupidQuestion/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane stops a truck."}

    def get_categories(self):
        return ['Dialogue']

    def get_general_description(self):
        return "... and you'll Get a Stupid Answer.\nYou know how obnoxious Captain Obvious can be. You " \
            "just want to yell at them and say, \"Any blind idiot can tell what's going on!\" But then " \
            "there are those Captains Obvious who can not only tell what is going on, but ask a stupid " \
            "question just to verify.\nThis is not only when that question is asked, but to the " \
            "frustrated individual this is their chance to strike back with a non-sequitur, either in a " \
            "Deadpan Snarker retort or full on Mind Screw confusion. A specific variation of Sarcasm " \
            "Mode.\nWhile examples on this page are of In-Universe instances of this type of exchange, " \
            "this is certainly a staple of MSTing by pointing out where people are being oblivious to " \
            "their dialogue (or being repetitive in them). For example: \"This is a map to " \
            "Hammunaptra.\" \"The Hammunaptra?\" \"No, the one in Jersey.\"\nBill Engvall's \"Here's " \
            "Your Sign\" routine was dedicated to these exchanges. MAD also had a section called " \
            "\"Snappy Answers To Stupid Questions\" written by Al Jaffee.\nOf course, if you decide to " \
            "avert the inevitable sarcastic retort by not seeking explicit confirmation that your " \
            "friend with the house full of boxes is actually moving, nine times out of ten it will turn " \
            "out (after a generous helping of Poor Communication Kills) that he is just having the " \
            "house fumigated.\nAn attempt to maneuver someone into asking a stupid question for the " \
            "purpose of delivering a snappy answer is What's a Henway? When the stupid answer is, in " \
            "fact, correct, it's Don't Be Ridiculous. See Stupid Question Bait for a similar concept."

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
