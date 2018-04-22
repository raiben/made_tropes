from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class OutOfCharacterAlertTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "OutOfCharacterAlert"

    def get_long_name(self):
        return "Out-of-Character Alert"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/OutOfCharacterAlert"

    def get_rdf_element(self):
        return "OutOfCharacterAlert/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, a bunch of German mercenaries impersonate cops. Although the "
                "leader speaks English with a flawless American accent, he slips up on a few word choices, "
                "such as calling an elevator a \"lift\" and saying that it's raining \"dogs and cats\", "
                "instead of the usual \"cats and dogs\". When McClane recognizes that one of them is "
                "wearing a friend's badge, and mentions the lottery to figure out if anyone on the elevator "
                "is real. None of the fake cops know last night's numbers, though in the beginning it's "
                "established that every NYPD cop plays the lottery with their badge number."}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "The inversion of Something Only They Would Say: When a character is pretending to be " \
            "someone else, they may unwittingly reveal this by saying something that would be out-of- " \
            "character for who they're impersonating. Variations include not responding to a well-known " \
            "Berserk Button, doing things they're normally afraid of (or have a similar excuse for " \
            "never doing), insisting to be called by a nickname they hate, or otherwise invokes OOC Is " \
            "Serious Business.\nOften Invoked in kidnapping and I Have Your Wife scenarios, to let the " \
            "heroes know that something is amiss. If the Big Bad is demanding a ransom, this is to " \
            "alert them to the fact that it's a trap; if he wants the kidnapped to \"assure\" The Hero " \
            "that the kidnapped is \"in fact\" okay, this is to secretly convey that they're not. " \
            "Sometimes serves as a Quiet Cry for Help. If they've pre-arranged such an alert, this is a " \
            "Covert Distress Code.\nReal-life military personnel sometimes use hand signals when being " \
            "taped to communicate in another way with their 'home base'. There are a few documented " \
            "cases of soldiers giving hand signals (and one case of them just flipping the bird to the " \
            "camera) to alert the people receiving it that no, they weren't being treated very politely " \
            "at all. And some have done it just for fun, giving the sign for coercion when forced to " \
            "shake a politician's hand, for instance.\nCompare with Lying Finger Cross (a common " \
            "gesture used in this trope), Not Himself, Ooh, Me Accent's Slipping, and Trust Password (a " \
            "pre-arranged alert to confirm one's identity and freedom of action). Contrast with " \
            "Something Only They Would Say (in which a character is identified by a characteristic) and " \
            "Bluff the Impostor. Sister Trope to You Called Me X, It Must Be Serious."

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
