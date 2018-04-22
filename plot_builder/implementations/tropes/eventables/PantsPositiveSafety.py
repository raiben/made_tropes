from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PantsPositiveSafetyTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "PantsPositiveSafety"

    def get_long_name(self):
        return "Pants-Positive Safety"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PantsPositiveSafety"

    def get_rdf_element(self):
        return "PantsPositiveSafety/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance has McClane puts his pistol in his waistband instead of in the "
                "shoulder holster he is wearing! It takes a little longer to draw a gun out of a shoulder "
                "holster than from the hip; given how his day had been going thus far..."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "When a character stores or conceals a weapon, typically a gun, in a place which is not " \
            "suited for such a purpose, typically the waistband or sometimes pocket of his/her pants. " \
            "There, or loose in a civilian briefcase. Anywhere but a holster. Often as not, the safety " \
            "isn't on and the gun is loaded, too. Perhaps it's another source of the term \"going off " \
            "half-cocked\". He means shooting his penis.\nAlthough aversions aren't uncommon, the " \
            "weapons rarely fall down the pants leg (provided you are wearing a belt or pants at least " \
            "as sturdy as blue jeans), and only occasionally will the weapon accidentally discharge and " \
            "injure someone in an intimate place. As of the 1950s firearm actions are required to be " \
            "\"drop-safe\", so the not going off part is Truth in Television. Even when the weapon is " \
            "drawn suddenly, like for combat, and leaves the pants with the user's finger on the " \
            "trigger, it typically only happens for comedic purposes. Because what's funnier than " \
            "someone shooting themselves in the foot? That's right.\nSubtrope of Artistic License " \
            "\u2013 Gun Safety. See also I Just Shot Marvin in the Face, Hidden Weapons, Trouser Space, " \
            "Unorthodox Holstering, and Victoria's Secret Compartment."

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
