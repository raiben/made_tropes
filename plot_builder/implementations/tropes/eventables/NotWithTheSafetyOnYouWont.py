from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class NotWithTheSafetyOnYouWontTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "NotWithTheSafetyOnYouWont"

    def get_long_name(self):
        return "Not with the Safety on, You Won't"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/NotWithTheSafetyOnYouWont"

    def get_rdf_element(self):
        return "NotWithTheSafetyOnYouWont/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, hero John McClane (Bruce Willis) gives his reluctant ally "
                "Zeus (Samuel L. Jackson) a submachine gun lifted from a fallen mook to defend himself as "
                "they search the bad guys' boat, even giving him a short primer on how to use the gun. Zeus "
                "later comes upon Big Bad Simon Gruber (Jeremy Irons) and holds him at gunpoint; Simon "
                "takes the gun away, casually notes (of course) he's got the safety on, flips off the "
                "safety and shoots him."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "If guns are featured in a movie, and someone inexperienced takes to using one (the Damsel " \
            "in Distress or similar character), there's a good chance of this phrase being uttered. " \
            "There are three versions:\nIn the first case, the character being held up might use it as " \
            "a ruse to try to wrong-foot his opponent. Usually in this instance the character at " \
            "gunpoint is a veteran, his savvy attitude being contrasted to his inexperienced opponent. " \
            "It is extremely rare for the opponent to call his bluff; instead he will usually tilt his " \
            "gun and look down to check if the safety is on, letting the other person get the drop on " \
            "him. Note that in this case the safety need not actually be on; all that's necessary is to " \
            "trick the guy holding the gun into checking.\nIn the second, the person at gunpoint is " \
            "generally a villain and the one holding the gun an inexperienced good guy; in this case, " \
            "the villain will grab the gun after it fails to fire, mocking his opponent for their lack " \
            "of expertise only afterward.\nThe third example is when a Magnificent Bastard is on the " \
            "other end of the gun along with some other villain. Once the other guy is knocked out and " \
            "the hero is securing him, he'll casually comment that you can't fire a gun with the safety " \
            "on, and that 'next time' the hero should check first; thus showing that really he was just " \
            "going along with it because it suited him and enhancing his Magnificent " \
            "Bastardry.\nVariations exist; it might be that the gun is recognizably jammed, is " \
            "physically impossible to fire at the target for some reason, would kill both of them if " \
            "fired, is not cocked, or even is not loaded. Note that in Real Life, any (competent) gun " \
            "user or owner will leave the safety on until ready to fire, and especially make sure the " \
            "safety is engaged if they are going to hand it to someone else. In addition, nearly all " \
            "revolvers and many automatic pistols (Glock, Sig and others) do not feature a safety " \
            "catch, relying on internal mechanisms and a strong trigger pull.\nWhen the safety has been " \
            "deliberately left on in case the weapon gets stolen, the person stealing it may find It " \
            "Works Better with Bullets.\nThe inverse sometimes shows up in movies where a gun is fired " \
            "with the safety on, presumably to keep actors from death by blank. This annoys gun nuts; " \
            "the appropriate special effects hide the phenomenon from other viewers."

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
