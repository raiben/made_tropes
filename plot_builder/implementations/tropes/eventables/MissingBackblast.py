from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class MissingBackblastTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "MissingBackblast"

    def get_long_name(self):
        return "Missing Backblast"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/MissingBackblast"

    def get_rdf_element(self):
        return "MissingBackblast/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "An alternate ending to Die Hard with a Vengeance includes John McClane playing a variant "
                "of Russian Roulette with Simon Gruber using a Chinese rocket launcher with the sights "
                "removed, so they can't tell which end is the muzzle. He asks Simon a series of questions, "
                "and eventually asks a question that Simon gets wrong.  Turns out that the answer to the "
                "question is that he forgot to bring a flak jacket, which is what McClane is wearing and "
                "this would have protected Simon from the blast of the rocket, and the rocket fires on "
                "Simon, killing him instantly."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "In the world of fiction, rocket-propelled weaponry create negligible, if any, backblast. " \
            "The characters shown using such weapons are thus able to use rocket launchers with their " \
            "backs to a wall or within an enclosed space; as if the rocket just levitates away instead " \
            "of being accelerated by the thrust of a strong jet.\nIn Real Life, if you fire a " \
            "recoilless rifle or rocket launcher in an enclosed space it will create so much pressure " \
            "that you have a high chance of being killed by it. Additionally, firing them with your " \
            "back to a wall will result in the hot rocket exhaust being deflected back at you and " \
            "severely burning or possibly killing you. Not to mention that standing immediately behind " \
            "them will result in grievous injury or death. And then there's the fact that the huge " \
            "flash of flame and cloud of smoke coming out of the back of the weapon (and maybe even a " \
            "big black triangular scorch mark on the ground behind you, pointing directly at you, " \
            "depending on the weapon and the terrain) will probably be highly visible to anyone looking " \
            "in your direction, no matter how well camouflaged you were a moment ago, so you will gain " \
            "the immediate, sincere, and complete attention of everyone on the battlefield.\nNote " \
            "however, that this does not apply to all recoilless weapons: there are some rocket " \
            "launchers which utilize some kind of \"soft launch\" to eject the rocket from tube before " \
            "the rocket motor ignites. Others may utilize counterweight or frangible material that " \
            "counterbalances the effect of recoil and/or reduces the effect of backblast. Nevertheless, " \
            "many contemporary and most past rocket launchers or recoilless rifles lack these sort of " \
            "features, and among their number are those that are most often portrayed in media.\nSee " \
            "the Law of Inverse Recoil for a related weapons trope and Toasted Buns for another trope " \
            "involving missing rocket exhaust. Real Life aversions may be related to Too Dumb to " \
            "Live.\nThis trope is so common that only aversions and subversions should be listed."

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
