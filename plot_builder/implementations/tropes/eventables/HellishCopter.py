from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class HellishCopterTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "HellishCopter"

    def get_long_name(self):
        return "Hellish Copter"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/HellishCopter"

    def get_rdf_element(self):
        return "HellishCopter/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Before Die Hard with a Vengeance, the Clint Eastwood thriller The Gauntlet has a mob "
                "sniper's helicopter explode quite spectacularly after its rotor blades become tangled in "
                "some power lines."}

    def get_categories(self):
        return ['DeathTropes']

    def get_general_description(self):
        return "Watch enough action movies, and you soon realize that the only thing more dangerous than " \
            "being on a helicopter is wearing a V-neck Red Shirt or being the slutty girl in a Friday " \
            "the 13th movie. They've been described as 50,000 parts flying in close " \
            "formation.\nObviously, helicopters aren't quite that dangerous in Real Life, or else we " \
            "wouldn't use them for anything for fear of them haphazardly spinning out of control and " \
            "crashing into everything all the time. It just wouldn't be a productive way to get around. " \
            "Indeed, some helicopters, such as the Mi-24 Hind, are incredibly tough. So why do they get " \
            "knocked out of the air in seemingly every movie they ever appear in? Rule of Cool. Admit " \
            "it, it's just cool to watch one of these things spin out of control trailing smoke, " \
            "briefly becoming a Helicopter Blender for anybody unfortunate enough to be standing around " \
            "on the ground in the general area.\nIt's particularly unfortunate if that helicopter was " \
            "our heroes' ride home.\nThis trope is about that prevalent tendency of helicopters " \
            "crashing various media, as well as in situations where a helicopter crash wouldn't " \
            "necessarily be expected. If a military chopper in a warzone gets hit by a rocket launcher " \
            "and goes down, that's less of this and more of a Short Lived Aerial Escape\u2014but if " \
            "half a dozen helicopters get shot down in the same movie, it's probably a textbook case of " \
            "this trope. If a giant monster smacks the 'copter out of the sky, it's a Helicopter " \
            "Flyswatter. If a military chopper collides with another aircraft or power lines or " \
            "something due to remarkably bad luck, then it's this trope. If the chopper goes down " \
            "because Danger Takes a Backseat, it's this trope regardless of it being a military chopper " \
            "in a warzone or not. If it's a police or news chopper getting blown up by a rocket " \
            "launcher over downtown Los Angeles, it's both this trope and Short Lived Aerial " \
            "Escapenote\u00A0And for the news chopper, Deadline News as well, as you'd never really " \
            "expect that sort of thing to happen.\nIn unusual situations, such as military choppers in " \
            "a straight-up fight with aliens being taken out in ways that we would consider decidedly " \
            "unusual (such as the Combat Tentacles example in the Film section), just remember that " \
            "Tropes Are Flexible.\nThe fuel for this trope comes from many sources, but the most " \
            "prominent of which is likely Rule of Cool (combined with Everything's Better with " \
            "Spinning). Iconic scenes of Blackhawk helicopters getting shot down (an actually rare " \
            "event) in the famous movie Black Hawk Down are sure to have helped this trope's staying " \
            "power. It also gives plenty of opportunities for various kinds of drama, badassery, and " \
            "visceral action, making it as much a tool for creators as a source of entertainment for " \
            "the audience, if not more so.\nApplies to pretty much any helicopter or helicopter- " \
            "analogue (such as tilt-jet military transports in sci-fi films). See also Short Lived " \
            "Aerial Escape. No relation to Hellish Horse. Subtrope of Anti-Air."

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
