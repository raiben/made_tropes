from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ToAbsentFriendsTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ToAbsentFriends"

    def get_long_name(self):
        return "To Absent Friends"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ToAbsentFriends"

    def get_rdf_element(self):
        return "ToAbsentFriends/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: When the bad guys are celebrating the successful theft, they're "
                "toasting to several things and then one says along the lines of 'auf gefallen kameraden', "
                "which translates something like 'for fallen comrades'. There is a moment of silence and "
                "then they all toast in honor of their lost brethren."}

    def get_categories(self):
        return ['DeathTropes']

    def get_general_description(self):
        return "Two or more characters gather to grieve for a dead comrade, without a formalized " \
            "structure. They reminiscence about the fallen, how much he will be missed \u2014 or has " \
            "been missed.\nAn actual wake is possible, as the bereaved can talk and drink without a " \
            "ceremony to go through. Or they may meet somewhere, and talk. (They may not even intend to " \
            "grieve, but they end up doing so.) A bar is likely, because the wake often involves " \
            "alcohol \u2014 so often that it generally does not appear only if it is impossible. Expect " \
            "the dead to be toasted. (Drowning My Sorrows may convert into this if the drinker bumps " \
            "into another friend.) Sometimes the drink is poured on the ground as a Libation for the " \
            "Dead.\nSoldiers on a mission may start to talk, and lead to this, if they are waiting for " \
            "something and have lost a comrade. (The situation in which alcohol is least likely to " \
            "feature. But the Military Moonshiner may have some.)\nThe informal equivalent of a " \
            "Meaningful Funeral. Possibly it immediately precedes or follows it, although that is " \
            "unlikely, because the two scenes concentrate on the same emotions, and so are likely to " \
            "duplicate. Also compare Personal Effects Reveal.\nMay also feature long after the death " \
            "(or deaths) as characters remember all their dead and tell stories of them. The toast is " \
            "often \"To absent friends\". This can overlap with Tell Me About My Father.\nSuitable for " \
            "a Bittersweet Ending or a Downer Ending, but can happen anywhere in a story \u2014 even as " \
            "a Framing Device at the very beginning of a work that Starts with Their Funeral. " \
            "Remembering the sacrifice may inspire characters to fight on, lest it have been a " \
            "Senseless Sacrifice.\nContrast Forgotten Fallen Friend, Dead Guy Junior.\nDeath Trope. " \
            "Spoilers follow."

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
