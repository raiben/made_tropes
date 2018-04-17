from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class StarCrossedLoversTrope(TropeDefinitionInterface):
    def get_type(self):
        return self.ARCHETYPE_TYPE

    def get_sorted_role_characters_array(self):
        return ["first lover", "second lover"]

    def get_sorted_role_places_array(self):
        return []

    def get_sorted_role_objects_array(self):
        return []

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/StarCrossedLovers"

    def get_description_with_replaced_existents(self, list_of_characters, list_of_places, list_of_objects):
        return "{} and {} are in love, but they find something in their way".format(list_of_characters[0],
                                                                                    list_of_characters[1])

    def get_number_of_events(self):
        1

    def get_events_from_coded_plot_entity(self, coded_plot_entity):
        return [EventEntity(subjects=[coded_plot_entity.list_of_character_ids[0]])]