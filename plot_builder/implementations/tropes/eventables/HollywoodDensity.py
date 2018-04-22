from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HollywoodDensityTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HollywoodDensity"

    def get_long_name(self):
        return "Hollywood Density"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HollywoodDensity"

    def get_rdf_element(self):
        return "HollywoodDensity/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, the trucks loaded with looted gold bullion would not have "
                "been able to drive uphill. The producers admitted to just ignoring the issue.  The trucks "
                "wouldn't have been able to drive at all. In 1995, 150 billion dollars worth of gold should "
                "have weighed around over 9,000 tons. 13 trucks? 130 would have had trouble carrying that "
                "load. One thief tosses a gold bar to another thief. The way it hits him when he catches "
                "it, it should've ruptured a few organs. On the other hand, Zeus is very surprised at how "
                "heavy a single gold brick is."}

    def get_categories(self):
        return []

    def get_general_description(self):
        return "Writers frequently misapply, distort, or outright forget about the concept of density and " \
            "its implications. This results in such oddities as most metals, including gold, being " \
            "treated as weighing the same as an equivalent volume of iron or steel, with the possible " \
            "exceptions of aluminum (famous for weighing less) and lead (famous for weighing a lot). " \
            "The only thing typically treated as denser than lead is matter from a neutron star, by " \
            "orders of magnitude \u2014 there's apparently nothing in between.\nBy the same token, " \
            "anyone can lift as much of a \"light\" object, such as feathers, Styrofoam, or in the " \
            "worst cases even stacked flat paper, as can be made practical to carry (though, " \
            "interestingly, if the paper is in another form, this doesn't seem to apply as much, as " \
            "characters will frequently acknowledge that stacks of books or newspapers are " \
            "heavy.)\nWhat's worse, even if the writers get it right, sometimes the actors won't, due " \
            "to not compensating for the difference between the weight of the prop and the weight of " \
            "the object it's supposed to represent through acting.\nGenerally, the only exception to " \
            "\"people carrying around big gold ingots with ease\" comes when the density of gold " \
            "relative to other substances is itself a major plot point. Especially since gold is " \
            "actually 70% more dense than lead. To say nothing of the fact that gold's status as a " \
            "dense substance is rather well known; anyone who's ever worn a gold ring can tell that " \
            "it's heavier than a silver one.\nSometimes an Acceptable Break from Reality, sometimes " \
            "not. It helps to be in a fantasy setting, and consistency is key. Keep in mind that " \
            "sometimes reality can make something incredibly boring. (One of the most common house " \
            "rules for most tabletop games is that gold is weightless, because having a weight penalty " \
            "for your character's money would detract from the fun of the game.) Balloonacy is a " \
            "subtrope dealing with wild over- and under-estimations of the lifting capacity of Helium, " \
            "Hydrogen or hot air. Soft Water follows this trope, and Briefcase Full of Money is closely " \
            "related."

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
