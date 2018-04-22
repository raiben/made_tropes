from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class LittleUselessGunTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "LittleUselessGun"

    def get_long_name(self):
        return "Little Useless Gun"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/LittleUselessGun"

    def get_rdf_element(self):
        return "LittleUselessGun/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "At the end of Die Hard with a Vengeance, McClane asks for a gun and is given a tiny "
                "revolver of which he is extremely disdainful. Subverted in that he manages to take out the "
                "helicopter attacking him with it by shooting some overhead power lines."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "A character treats a small firearm with contempt. The firearm will likely be physically " \
            "small and will probably fire small-caliber ammunition, which is considered by some users " \
            "to be weak.\nThere is a common perception that any round smaller than a .38 Special is " \
            "essentially a joke bullet unable to do any real damage. The truth is that Bullets Do Not " \
            "Work That Way. Guns, by definition, are weapons that are designed to kill. Just about any " \
            "gun made today can inflict a mortal wound in one shot, though a small caliber bullet " \
            "probably won't drop you on the spot. Even the oft mocked .22 Short can tear deep enough " \
            "into a human body to tear major veins and arteries, and if the bullet reaches the throat " \
            "or vital organs the damage will be severe. Even air weapons firing small pellets at low " \
            "speed can inflict lethal injuries if they hit someone in a critical area such as the " \
            "temple or the heart. This is exactly why airsoft events have very strictly enforced safety " \
            "rules about minimum engagement distances and protective equipment. It's also why it's both " \
            "frequently forbidden and a bad idea to use frozen paint balls.\nThe idea that small- " \
            "caliber and/or low-powered weapons are useless in combat probably comes from the somewhat " \
            "vague notion of \"stopping power\" and that Bigger Is Better in this regard. Even wounds " \
            "that are fatal will generally not result in an Instant Death Bullet, and it is not unknown " \
            "for a target to keep going after having been shot, sometimes not even noticing. So the " \
            "theory goes that larger caliber weapons are more likely to ensure that a target will " \
            "actually stop in fewer shots. The other side of the argument is that most of the " \
            "\"evidence\" for stopping power is almost purely anecdotal and no scientific mechanism for " \
            "its function has been confirmed. Furthermore many comparatively smaller guns can have " \
            "twice the rounds (or more) per magazine versus a massive Hand Cannon as well as far less " \
            "recoil and weight so are \"more likely\" to be accurate. While certainly size does matter " \
            "in ballistics the debate mostly centers around weapons of the same type (pistols vs " \
            "pistols, rifle vs rifles) not a Derringer next to a .50 BMG sniper rifle thus the " \
            "differences are comparatively small.\nSince you can't exactly subject live humans to " \
            "rigorously controlled lethal testing its doubtful that debate will end any time " \
            "soon.\nOften popular as a Hidden Weapon stored in Victoria's Secret Compartment. For the " \
            "opposite end of the spectrum, see Hand Cannon and BFG."

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
