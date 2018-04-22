from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HeroicBystanderTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HeroicBystander"

    def get_long_name(self):
        return "Heroic Bystander"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HeroicBystander"

    def get_rdf_element(self):
        return "HeroicBystander/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "'Die Hard with a Vengeance: McClane himself is not a bystander this time - he's a target. "
                "It's Samuel L. Jackson's Zeus who's the Heroic Bystander."}

    def get_categories(self):
        return ['CharactersAsDevice']

    def get_general_description(self):
        return "When something bad happens, most people gape in fear and shock. They are the Innocent " \
            "Bystanders. But sometimes one person decides to help out, and in the doing, becomes a " \
            "hero. That's the Heroic Bystander.\nThe Heroic Bystander is not someone who is normally " \
            "expected to be a hero in time of crisis, such as a police officer or a lifeguard. Instead, " \
            "it's an ordinary person, with no special training, who happens to save a life through " \
            "their own inner courage and resolve.\nIt doesn't have to be a life that is saved. A Heroic " \
            "Bystander can also defend a person's reputation, distract a villain with a Defiant Stone " \
            "Throw or help someone out who needs help, when no one else is doing so.\nThis can be used " \
            "as a device to show the growth of a character, such as having a cowardly individual show " \
            "remarkable resolve in coming to someone's rescue. It can show how someone is transformed " \
            "from a passive outsider, to someone who gets involved and tries to help others. Sometimes, " \
            "it can be used to let a wimp have their day in the sun. Sometimes (especially in real " \
            "life) a whole crowd will get involved, possibly sparked by one person showing courage to " \
            "ignite the powder keg.\nOf course, those bystanders live in a world that is basically " \
            "similar to our own. An Anti-Hero of a Crapsack World (who is usually a bystander, not a " \
            "Knight in Shining Armor) is something different.\nSee also I Am Spartacus, which sometimes " \
            "uses this. If he's the protagonist, then he becomes an Action Survivor. Compare Good " \
            "Samaritan, Badass Bystander, Civilian Power, and Hero of Another Story.\nSomewhere between " \
            "this and a Superhero lie The Real Heroes: ordinary people in jobs that require them to do " \
            "this day-in, day-out without anyone writing a comic strip about them.\nContrast Never Be a " \
            "Hero."

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
