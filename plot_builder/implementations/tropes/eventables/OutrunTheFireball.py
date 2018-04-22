from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class OutrunTheFireballTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "OutrunTheFireball"

    def get_long_name(self):
        return "Outrun the Fireball"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/OutrunTheFireball"

    def get_rdf_element(self):
        return "OutrunTheFireball/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Subverted in Die Hard with a Vengeance: After being told that a bomb was in a garbage can "
                "by the phone booth, both Samuel L. Jackson and John McClane try to push people aside and "
                "then dive to the ground; when no one responds and no explosion happens, the terrorist's "
                "laughing reveals the joke."}

    def get_categories(self):
        return ['OlderThanDirt']

    def get_general_description(self):
        return "A Time Bomb, superweapon, crashed car, etc. is about to explode. The heroes run as fast as " \
            "they can and try to leap behind shelter, just as it explodes. Often features a cool shot " \
            "of the heroes diving towards the camera.\nVirtually every action series has had its share " \
            "of these moments. In fact, it is easy to imagine that some remote civilization studying " \
            "Earth through its television transmissions might conclude that Earthlings running causes " \
            "Stuff Blowing Up, not the other way around.\nCan also be done with cars, airplanes, " \
            "spaceships, snowmobiles, mine carts... anything that moves, or doesn't, for that " \
            "matter.\nThough all are related to Non-Fatal Explosions, there are also two more directly " \
            "related tropes. One is the Rocket Jump: an extremely hard-ass character may exploit the " \
            "power of the blast as it propels them through the air to reach places they wouldn't " \
            "normally have been able to. The second is combining this with Out of the Inferno: for a " \
            "second it seems that the characters won't make it as the flames from the explosion reach " \
            "and engulf them...Then a few second later they come out bursting through the flames, " \
            "slightly parched but unharmed.\nOn rare occasion, the characters will be made to look like " \
            "fools by there being no explosion after diving into the dust (toward the camera). This " \
            "will be followed by a four-count beat, to share an embarrassed moment, which will be " \
            "punctuated by an explosion.\nThe Badass often showcases just how cool he is by always " \
            "calmly walking away from the building or car, and perhaps casually putting on his Cool " \
            "Shades or lighting up a cigarette just as the explosion goes off. Badass characters don't " \
            "have to run unless it's darned important. Cool guys don't look at explosions.\nExamined " \
            "exhaustively at the website The Reality of Running Away from Stuff.\nFor when a character " \
            "doesn't outrun the fireball and walks calmly out of and away from the fire anyway, see Out " \
            "of the Inferno. See also Convection Schmonvection. In Real Life, the accepted reaction to " \
            "an approaching fireball is to either jump down a deep hole and pull it in after you, or " \
            "bend over and kiss your posterior goodbye. See also Bomb Disposal when this is done " \
            "intentionally.\nThe fireball is often depicted in Slow Motion.\nContrast Riding into the " \
            "Sunset."

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
