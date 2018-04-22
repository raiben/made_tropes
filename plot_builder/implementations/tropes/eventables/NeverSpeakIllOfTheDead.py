from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class NeverSpeakIllOfTheDeadTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "NeverSpeakIllOfTheDead"

    def get_long_name(self):
        return "Never Speak Ill of the Dead"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/NeverSpeakIllOfTheDead"

    def get_rdf_element(self):
        return "NeverSpeakIllOfTheDead/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Subverted in Die Hard with a Vengeance, as Simon agrees with McClane that Hans was an "
                "asshole. But \"there is a difference between not liking one's brother and not caring when "
                "some dumb Irish flatfoot drops him out of a window.\""}

    def get_categories(self):
        return ['Dialogue']

    def get_general_description(self):
        return "Regardless of how disliked or embarrassing a person was in life, no matter how odd they " \
            "were considered, or what crimes they had committed, the moment they leave this mortal " \
            "coil, a Nostalgia Filter falls into place causing the deceased to be remembered as being " \
            "better than they were, for the most part. For some people, the reasoning is that the dead " \
            "person isn't here to defend themselves anymore, or at the very least cannot continue to do " \
            "the unpleasant things they were reviled for anymore.\nAn Asshole Victim can be \"spared\" " \
            "this provided they were enough of an asshole. Alternatively, can be a justification for " \
            "Alas, Poor Scrappy.\nVillains, particularly ones at the lighter end of the Sliding Scale " \
            "of Antagonist Vileness, will sometimes extend the same courtesy to fallen heroes " \
            "(particularly ones they regarded as a Worthy Opponent).\nDefinitely Truth in Television, " \
            "as the idea has been around since at least the 4th century. Whether or not it should be is " \
            "rather contentious. Plenty of people seem to deride it for those they hate but invoke it " \
            "for public figures they like. An alternative formulation, suggested by Christopher " \
            "Hitchens (who loved speaking ill of the dead) is: \"Never say anything nasty about the " \
            "dead that you weren't brave enough to say while they were alive. Everything else is fair " \
            "game.\"\nSee also Treachery Coverup, Unacceptable Targets and Dead Artists Are Better. If " \
            "people choose to lie to preserve the departed's reputation, they're using The Power of " \
            "Legacy.\nContrast with Speak Ill of the Dead for the serious version and The Fun in " \
            "Funeral for less serious ones.\nThis is a Death Trope, so expect UNMARKED SPOILERS!"

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
