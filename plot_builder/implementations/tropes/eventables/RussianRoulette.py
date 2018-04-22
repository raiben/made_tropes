from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class RussianRouletteTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "RussianRoulette"

    def get_long_name(self):
        return "Russian Roulette"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/RussianRoulette"

    def get_rdf_element(self):
        return "RussianRoulette/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "An alternate ending to Die Hard with a Vengeance includes John McClane playing a variant "
                "of Russian roulette with Simon Gruber using a Chinese rocket launcher without the pin. He "
                "asks Simon a series of questions, and eventually asks a question that Simon gets wrong. "
                "Turns out that the answer to the question is that he forgot to bring a flak jacket, which "
                "is what McClane is wearing and this would have protected Simon from the blast of the "
                "rocket, and the rocket fires on Simon, killing him instantly."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "Russian Roulette: A game of suicide and/or luck for one to six players.\nEquipment:\n 1 " \
            "revolver\n 1 round of ammunition\nSetup:\n Load one chamber.\n Half-cock the hammer to " \
            "free the cylinder.\n Spin it.\n Fully cock the hammer to stop it.\n (Alternative for " \
            "double-action revolvers) With the cylinder swung out to the side, spin it and slap it back " \
            "into the frame.\nRules:\n Each player, in turn, puts the gun to his head and pulls the " \
            "trigger.\n First player to die loses.\n Portrayals of the game differ as to whether the " \
            "cylinder is spun after each trigger pull. If it is, the game can continue indefinitely " \
            "with a 1 in 6 chance of hitting the loaded chamber each time. If not, there are a maximum " \
            "of 5 chances to not die, assuming the cylinder has 6 chambers and the ammunition round " \
            "isn't a dud.\nHistory: The game was allegedly invented by the Russians either during World " \
            "War One or by those assigned to Siberia. If the latter, to deal with the extreme boredom, " \
            "as their assignment was often referred to as 'counting trees', while the former was to try " \
            "and get out of the extremely bloody and inglorious war. There are no indication however " \
            "that this is true (and such outlandish behaviour would have most likely been recorded as " \
            "suicides and duels were usually described in length) as the first mention of this game (as " \
            "well as the name 'Russian roulette' itself) appears in a 1937 short story of the same " \
            "title by Georges Sundez, a Frenchman. Also, the most common revolver issued by the Russian " \
            "army at the time had a cylinder that could not be freely spun (and also had seven " \
            "chambers, but that's not really important).\nToday, it's seen as the one of the more manly " \
            "stunts available because of the risks involved, reduced somewhat by the common one-round- " \
            "six-chambers setup. Perfect for proving you're not afraid to (or want to) die, you're a " \
            "real man, or you're just Too Dumb to Live.\nSome claim that if the original game existed, " \
            "it could be a largely harmless entertainment - if there is a single round and a gun is " \
            "well oiled, the full chamber will end at the bottom.\nIt can also be used to scare " \
            "information out of prisoners, as a form of psychological torture.\nNeed we say it: Don't " \
            "Try This at Home. Besides the risk to your life if you lose, if you play with others you " \
            "can be charged with murder if someone dies (at least in common-law jurisdictions, under " \
            "the theory of depraved-heart/grossly reckless murder\u2014see for instance the " \
            "Pennsylvania case Commonwealth v. Malone), and in some jurisdictions you can be tried for " \
            "attempted murder even if everyone lives. One notable case in 1984, was American actor Jon- " \
            "Erik Hexum who died a Russian roulette stunt, despite only loading the revolver with " \
            "blanks. Despite his belief that this made it harmless, the overpressure wave from the " \
            "discharge of the blank propelled the round's wadding into his temple, shattering his " \
            "skull, and causing brain trauma. Six days later he was declared brain dead and was taken " \
            "off life support.\nSee also False Roulette. For the wider trope of lethal \"games\" that " \
            "don't involve handguns, see Absurdly High-Stakes Game. The Other Wiki also has an article. " \
            "One of the reasons why Revolvers Are Just Better.\nFor the TV game show, click here."

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
