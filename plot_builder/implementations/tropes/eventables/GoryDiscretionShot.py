from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class GoryDiscretionShotTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "GoryDiscretionShot"

    def get_long_name(self):
        return "Gory Discretion Shot"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/GoryDiscretionShot"

    def get_rdf_element(self):
        return "GoryDiscretionShot/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, we get one of these when one of the Mooks is sliced in half "
                "by a snapping cable. We see the cable whip towards him, we see him catapulted backwards by "
                "the hit, but cuts away before we see him bisected. Then McClane and Zeus come across his "
                "body. \"I'll get his arms, you get his legs.\" They start out carrying the body normally, "
                "until Zeus turns until he's side-by-side with McClane."}

    def get_categories(self):
        return ['DeathTropes']

    def get_general_description(self):
        return "Blood or brains are seen splattering against a wall and the rest is left to the " \
            "imagination.\nMost often used with women and children, because it's more okay to hurt men " \
            "in Hollywood, but available for everyone to control the tone/rating of the work. Often " \
            "found in the form of a Reaction Shot as the reacting characters' expression (or lack " \
            "thereof) can serve as a commentary on the action, the character, or the world they " \
            "inhabit. Sometimes combined with Blood Spattered Innocents, as the gore splatters on or " \
            "near them.\nA Japanese variation of this trope involves seeing the silhouettes of the " \
            "participants from behind a translucent washi screen, typically a shouji sliding door, on " \
            "which the blood gets spattered. The form has since been widely adopted by the west and is " \
            "often used to give a sense of art. A similar variation is to have the splatter hit the " \
            "other side of a pane of glass or a window. Another variation shows blood seeping out under " \
            "a door, through an opening or across a sill or a threshold to imply that violence has " \
            "occurred on the other side.\nA Gory Discretion Shot can serve to keep the rating PG-13 to " \
            "reach a wider audience. It may also be done for budgetary reasons: red dyed corn syrup " \
            "splashed over a window: cheap. Showing someone's head explode: expensivenote\u00A0Although " \
            "Scanners managed an effective budget version by filling a rubber head with chicken giblets " \
            "and blood and firing a shotgun at it from below and behind. Still more expensive than the " \
            "syrup/dye, though. Note that it could also be done to keep the truth hidden from the " \
            "viewer. Showing the murder in question straight out, so the viewers can see the culprit, " \
            "doesn't make a good murder mystery in most shows or movies after all.\nCombine it with " \
            "Bloodless Carnage, and you get the Sound-Only Death \u2014 the audience hears the gunshot " \
            "and the body hitting the deck, but what they see is (for instance) the victim's hat " \
            "falling to the ground with a hole through it. Or the killer walks through a door and we " \
            "hear gunshots and screams after it closes behind him. Also crosses paths frequently with " \
            "Scream Discretion Shot.\nA related trope is the camera cutting away when things get nasty. " \
            "Say if someone is getting whipped, we'll only see their face contorting in pain. " \
            "Alternately, a cut similar to a Screamer Trailer may be used, showing a split second worth " \
            "of the carnage. In the same vein, the aftermath of a murder may be demonstrated minimally " \
            "with a Dead Hand Shot, hopefully one still attached to the body.\nContrast Gorn. Compare " \
            "and contrast Battle Discretion Shot and Nothing Is Scarier; though this may be less " \
            "\"scary\" than not showing anything at all in a less overtly violent work, in Gornographic " \
            "works this can be used for horror\u2014with all this overt violence running around, what " \
            "is so horrible you don't get to see it...? See also Empathy Doll Shot and Pink Mist. May " \
            "precede a Mortal Wound Reveal, especially if it's unclear who exactly got " \
            "injured\u2014note that this is a Subversion of sorts, when it does happen."

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
