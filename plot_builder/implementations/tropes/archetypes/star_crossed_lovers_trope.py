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
