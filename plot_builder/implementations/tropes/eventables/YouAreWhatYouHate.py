from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class YouAreWhatYouHateTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "YouAreWhatYouHate"

    def get_long_name(self):
        return "You Are What You Hate"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/YouAreWhatYouHate"

    def get_rdf_element(self):
        return "YouAreWhatYouHate/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, the character of Zeus is a black man with serious problems "
                "with white people, most especially white racists. Eventually McClane calls him out on the "
                "fact that he's acting like a racist himself."}

    def get_categories(self):
        return ['IndexOfExactTropeTitles']

    def get_general_description(self):
        return "This is the implication that a character who dislikes a particular thing is secretly a " \
            "practitioner of that thing.\nThis especially comes into play when ethnicity or " \
            "homosexuality is involved. Such a character is likely to believe in negative stereotypes " \
            "about his own group (no matter how irrational), and hate himself for it, or live by those " \
            "stereotypes so they become self-fulfilling prophecies. If Fantastic Racism is in play, " \
            "such as with Differently Powered Individuals, the person may try to suppress the trait " \
            "that makes them part of the hated group, or use said power as a weapon against them.\nIn " \
            "older shows this sometimes comes up with racist characters who are exposed as being light- " \
            "skinned African-Americans who are 'passing'. Depending on the time frame of the media, the " \
            "result may be either to show that the character should love himself or, in very old media " \
            "from before 1940 or so, to show that the character is a sneaky liar who wasn't ethical " \
            "enough to accept his \"natural\" place in the order of things.\nThis sort of implication " \
            "is \"non-falsifiable\": If even denial is taken as proof, there's no way to prove " \
            "innocence. Characters who don't actually fall under this trope, but are accused of it by " \
            "other characters, may get increasingly angry (or despondent) about no one believing " \
            "them.\nThis trope comes in several flavors.\n The hater genuinely does not know he is a " \
            "member of the group he hates.\n The hater has clear evidence that he is a member of the " \
            "hated group but is in denial. He refuses to identify with said group and often comes up " \
            "with convoluted explanations as to why he isn't actually a member. Will often invoke the " \
            "No True Scotsman fallacy.\n The hater privately accepts that he is a member of the hated " \
            "group but hides it from others.\n The hater hates all members of the group, including or " \
            "especially themselves.\nWhen the character is openly a member of the group he despises, " \
            "then that's a Boomerang Bigot. It is possible for the two to overlap. A bigot's membership " \
            "in the hated group might be secret to most people but known to a few. If he continues to " \
            "sincerely express hatred towards the group, even when in a situation where his secret will " \
            "not be exposed, then he might show shades of both Boomerang Bigot and You Are What You " \
            "Hate.\nOften a cause of Unfortunate Implications. See also Hypocritical Humor, " \
            "Psychological Projection, He Who Fights Monsters, Karmic Transformation, Cultural Cringe, " \
            "I Do Not Like Green Eggs and Ham. Contrast Pretend Prejudice, in which a person pretends " \
            "to hate a group but secretly likes or tolerates them. Armoured Closet Gay is one common " \
            "Sub-Trope. If the hater doesn't realize that they're a member of the group they hate, they " \
            "might just be a Tomato in the Mirror. Contrast Hunter of His Own Kind which usually " \
            "involves fantastic Half Human Hybrids. Contrast Color Me Black for when a bigot is " \
            "forcibly turned into a member of the group they hate, usually by supernatural means. See " \
            "also Stop Being Stereotypical in which a person doesn't hate his group but is embarrassed " \
            "by the behavior of some members."

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
