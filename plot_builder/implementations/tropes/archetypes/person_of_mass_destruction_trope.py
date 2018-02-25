from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PersonOfMassDestructionTrope(TropeDefinitionInterface):
    def get_type(self):
        return self.ARCHETYPE_TYPE

    def get_sorted_role_characters_array(self):
        return ["person of mass destruction"]

    def get_sorted_role_places_array(self):
        return []

    def get_sorted_role_objects_array(self):
        return []

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PersonOfMassDestruction"

    def get_description_with_replaced_existents(self, list_of_characters, list_of_places, list_of_objects):
        return "{} is capable of causing a big damage".format(list_of_characters[0])
