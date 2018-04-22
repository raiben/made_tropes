from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class BackwardsFiringGunTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "BackwardsFiringGun"

    def get_long_name(self):
        return "Backwards-Firing Gun"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/BackwardsFiringGun"

    def get_rdf_element(self):
        return "BackwardsFiringGun/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "An alternate ending for Die Hard with a Vengeance has John McClane threatening Simon "
                "Gruber with a Chinese rocket launcher with the sights removed, allowing Gruber to point "
                "the rocket whichever way he liked.  Gruber ultimately points the rocket launcher the wrong "
                "way."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "This is a comedy weapon trope (although there are dramatic examples) featuring a gun " \
            "designed or modified to fire backwards, tricking the person who uses it into shooting " \
            "themselves. A common version seen in cartoons is to bend the barrel back into a \"U\" " \
            "shape. Note that this trope may still come into play even if the person who might fire the " \
            "gun would have to be really stupid not to notice the modification.\nThese guns tend to " \
            "show up in cartoons and spy genre pastiches.\nDespite the trope title, other projectile " \
            "weapons, such as a crossbow or hwacha Hwacha!!!, may be examples of this trope.\nCompare " \
            "Had the Silly Thing in Reverse."

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
