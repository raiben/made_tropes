from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class EqualOpportunityEvilTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "EqualOpportunityEvil"

    def get_long_name(self):
        return "Equal-Opportunity Evil"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/EqualOpportunityEvil"

    def get_rdf_element(self):
        return "EqualOpportunityEvil/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance. While the film's villain, Simon Gruber, doesn't quite fit this "
                "trope in terms of his mooks (they're all Germans and Slavs, with a token Hungarian as "
                "second-in-command), John McClane uses this description to convince Zeus to help him. "
                "McClane lies and tells Zeus that Simon put a bomb in Harlem (he actually put it in "
                "Chinatown), saying, \"This guy doesn't care about skin color even if you do.\"."}

    def get_categories(self):
        return ['MetaConcepts']

    def get_general_description(self):
        return "Bad guys are often remarkably open when it comes to race, gender, religion, species, and " \
            "so forth of their members. Some races might always be evil, but evil really knows no " \
            "bounds. If the characters have the ambition, the bloodlust, the hatred of puppies, or the " \
            "simple enjoyment of being evil, they're welcome to sign up. Evil Is One Big Happy Family, " \
            "after all.\nAt full force, this trope leads to a remarkably diverse set of top brass, as " \
            "well.\nIf this trait is emphasized more than necessary, it might come across as a Pet the " \
            "Dog moment. It might even result in Rooting for the Empire if the \"good guys\" are not so " \
            "unbiased. It might even suggest that it's okay to be unethical or even murderous as long " \
            "as you're \"fair\" about it. A villain could do this if it serves their own evil ends, and " \
            "someone who employs equally can just as easily hate everyone equally and may have no " \
            "problems with disposing of their minions just as easily, often permanently.\nWhile often " \
            "done to avoid Unfortunate Implications about certain races, it can just as easily fall " \
            "into it, such as portraying the heroes as all one ethnicity and every other race as the " \
            "villains. Compare White Gang-Bangers and Straight Edge Evil. Contrast Politically " \
            "Incorrect Villain. Note however that they are not mutually exclusive; a villain can be " \
            "intolerant towards some groups but progressive towards others. See also Alike and " \
            "Antithetical Adversaries and Anti-Human Alliance. May go hand in hand with Better Living " \
            "Through Evil. See Five-Token Band for the good-aligned version."

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
