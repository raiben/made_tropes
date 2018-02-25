from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class LovableRogueTrope(TropeDefinitionInterface):
    def get_type(self):
        return self.ARCHETYPE_TYPE

    def get_sorted_role_characters_array(self):
        return ["lovable rogue"]

    def get_sorted_role_places_array(self):
        return []

    def get_sorted_role_objects_array(self):
        return []

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/LovableRogue?from=Main.LoveableRogue"

    def get_description_with_replaced_existents(self, list_of_characters, list_of_places, list_of_objects):
        return "{} is an adorable rascal".format(list_of_characters[0])
