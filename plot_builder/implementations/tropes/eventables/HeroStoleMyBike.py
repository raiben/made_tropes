from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HeroStoleMyBikeTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HeroStoleMyBike"

    def get_long_name(self):
        return "Hero Stole My Bike"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HeroStoleMyBike"

    def get_rdf_element(self):
        return "HeroStoleMyBike/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance:\n Done, coupled with an Ironic Echo, when McClane steals the "
                "bike of a shoplifting kid.\n Done again (And Lampshaded and Played With) when McClane "
                "trades up from his Yugo by stealing a Mercedes on the expressway. Zeus points out how "
                "pissed the other driver must be, until McClane reminds him that Zeus forgot his bar of "
                "gold in the Yugo's back seat."}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "A character is in a hurry, most likely during a Chase Scene, when he or she sees a bike or " \
            "some other mode of transportation propped on the side of the road. He or she promptly gets " \
            "on it and keeps going full-speed. If the owner is present, the character will hastily say " \
            "something like \"I'm just borrowing it!\" or \"I need your bike! I'll bring it back " \
            "later!\"\nNote that you usually never see the bike actually get returned, and if it is " \
            "returned, don't expect the warranty to cover the damage.\nA Sister Trope to Flashed Badge " \
            "Hijack. In Real Life, you can get away with this without criminal charges on the plea of " \
            "\"necessity\" if you can establish that the harm done by your stealing the vehicle was " \
            "less than would have occurred if you hadn't.\nContrast Casual Car Giveaway, in which the " \
            "hero gives a random soul their vehicle.\n\nExamples"

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
