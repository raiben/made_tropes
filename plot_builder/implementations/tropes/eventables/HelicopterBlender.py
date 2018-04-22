from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HelicopterBlenderTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HelicopterBlender"

    def get_long_name(self):
        return "Helicopter Blender"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HelicopterBlender"

    def get_rdf_element(self):
        return "HelicopterBlender/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Played with in Die Hard with a Vengeance. The Big Bad's helicopter hits a light pole with "
                "its main rotor, producing a shower of sparks; however, instead of this causing the rotor "
                "to shatter and the helicopter to simply drop a few metres on the ground, the whole thing "
                "just blows up for no clearly defined reason."}

    def get_categories(self):
        return ['CombatTropes']

    def get_general_description(self):
        return "The hero is being chased by some Mooks in a helicopter. He's probably on a car or " \
            "motorbike (rarely running). The baddies are shooting automatic weapons at him, but they've " \
            "of course attended the Imperial Stormtrooper Marksmanship Academy. But wait, the hero has " \
            "just gotten himself into a wide open space with no exit! He's trapped!\nThe helicopter " \
            "first comes to a low altitude, and you may think the baddies would just open fire en masse " \
            "and rain hot lead all over the place because, hey, there's only so many bullets a hero can " \
            "dodge. But no, that'd be too easy.\nInstead, the helicopter first hovers right above " \
            "ground, then tilts forward at a very steep angle. It then proceeds to slowly move forward, " \
            "its rotor becoming a deadly, razor-sharp weapon that slices and dices everything it " \
            "touches. All sorts of objects, people, even vehicles are thrown aside and shredded to " \
            "pieces by the Helicopter Blender.\nThe hero seems doomed, but at the last moment he always " \
            "finds a way out (bonus points if it involves jumping over the helicopter)."

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
