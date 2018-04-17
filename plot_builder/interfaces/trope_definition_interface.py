from abc import abstractmethod


class TropeDefinitionInterface:
    ARCHETYPE_TYPE = "archetype"

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sorted_role_characters_array(self):
        pass

    @abstractmethod
    def get_sorted_role_places_array(self):
        pass

    @abstractmethod
    def get_sorted_role_objects_array(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_description_with_replaced_existents(self, list_of_characters, list_of_places, list_of_objects):
        pass

    @abstractmethod
    def get_number_of_events(self):
        pass

    @abstractmethod
    def get_events_from_coded_plot_entity(self, coded_plot_entity):
        pass
