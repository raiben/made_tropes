from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class EveryoneHatesMimesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "EveryoneHatesMimes"

    def get_long_name(self):
        return "Everyone Hates Mimes"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/EveryoneHatesMimes"

    def get_rdf_element(self):
        return "EveryoneHatesMimes/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: John McClane briefly considers running over a mime. And that "
                "scene where he and Samuel L. Jackson are in a taxi screaming across Central Park:"}

    def get_categories(self):
        return ['DesignatedAcceptableTargets']

    def get_general_description(self):
        return "Mimes are universally hated in fiction. They're an Acceptable Target of sorts. No real " \
            "reason is ever given, but the Uncanny Valley may have something to do with it - after all, " \
            "their pure white faces and refusal to speak give them a definite alien aura. This trope " \
            "isn't limited to people who hate mimes, but also works of fiction that seem to have it out " \
            "for them. In other words a character doesn't have to say \"I hate mimes\" for it to be " \
            "this trope. All the character needs to do is fall on, punch, kick, or otherwise cause " \
            "intentional or accidental harm to a mime. Compare Enemy Mime."

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
