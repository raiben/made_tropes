from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class TheSpeechlessTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "TheSpeechless"

    def get_long_name(self):
        return "The Speechless"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/TheSpeechless"

    def get_rdf_element(self):
        return "TheSpeechless/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Katya from Die Hard with a Vengeance is mute from an assassination attempt that left "
                "prominent scarring on her throat. However, in her final scene, she does scream angrily "
                "(and incoherently) while firing on John McClane and Zeus Carver."}

    def get_categories(self):
        return ['CharactersAsDevice']

    def get_general_description(self):
        return "Someone who does not speak onscreen because he cannot speak at all.\nHe is intelligent; he " \
            "does show signs of sentience to us, the viewers\u2014just not to the other characters. He " \
            "may be able to vocalize onscreen, but it won't be in a known language\u2014probably just " \
            "the occasional sigh, gasp, or other such non-speech sounds\u2014and none of the characters " \
            "will be able to interpret what he says. He will be able to gesture, but this may or may " \
            "not convey any meaning to the other characters; they may play charades with him to figure " \
            "out what he has to say. In extremis, may lapse into Talking with Signs\u2014but only we " \
            "the viewers get to see the signs.\nOften surprisingly competent, and tends to understand " \
            "what's going on better than voiced characters, while being hilariously unable to " \
            "communicate that understanding.\nOne popular use of this character is the Silent Snarker: " \
            "while they never have any lines, they are highly facially expressive and used for many a " \
            "Reaction Shot, Facepalm or visual This Is Gonna Suck.\nOne form of He Who Must Not Be " \
            "Heard. The opposite is The Unintelligible, whom the characters understand, but we don't. " \
            "Contrast also The Voiceless, who can talk, but just doesn't whenever we're watching. See " \
            "also Heroic Mime and Cute Mute. May utilize a Voice for the Voiceless or Mouth of " \
            "Sauron.\nCompare Pantomime Animal."

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
