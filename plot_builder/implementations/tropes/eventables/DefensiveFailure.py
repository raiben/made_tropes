from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class DefensiveFailureTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "DefensiveFailure"

    def get_long_name(self):
        return "Defensive Failure"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/DefensiveFailure"

    def get_rdf_element(self):
        return "DefensiveFailure/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance Zeus (another Samuel L. Jackson character) is holding up the "
                "entire bad guy parade with a gun, at which point Simon Gruber walks up to him, promptly "
                "explains that Samuel L. Jackson of all people forgot to turn the safety off, then captures "
                "him."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "The armed victim has the killer in her gunsights and at her mercy (it's usually a woman in " \
            "these situations), but the killer knows they have nothing to fear. The victim is either " \
            "unable or unwilling to use her weapon as the killer walks up to her and plucks the gun out " \
            "of her hands, leaving her a tearful heap begging for her life. Often involves a Breaking " \
            "Speech. If she had captured him beforehand or otherwise cornered him but doesn't shoot, " \
            "then it's a Hannibal Lecture.\nCompare You Wouldn't Shoot Me."

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
