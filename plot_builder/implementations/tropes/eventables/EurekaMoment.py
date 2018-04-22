from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class EurekaMomentTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "EurekaMoment"

    def get_long_name(self):
        return "Eureka Moment"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/EurekaMoment"

    def get_rdf_element(self):
        return "EurekaMoment/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, running into a band of under-aged looters alerts John "
                "McClane (Bruce Willis) that the villain's apparent plan is likely a distraction."}

    def get_categories(self):
        return ['IntelligenceTropes']

    def get_general_description(self):
        return "All complex problems are solved by sudden epiphany!\nIn every Locked Room Mystery, the " \
            "detective can't solve the crime just by examining the relevant evidence. They always need " \
            "some external inspiration (apparently) completely unrelated to everything, something along " \
            "the lines of:\n...or...\nThis will lead directly to The Summation, unless there's an " \
            "Evidence Scavenger Hunt in between. Often the character having the epiphany will tell the " \
            "person whose offhand remark inspired it that they're \"a genius\" or the like; the " \
            "remarker will then variously nod in a befuddled manner, ask \"I'm what?\", or simply " \
            "demand an explanation.\nNamed for perhaps the most famous non-detective related example, " \
            "Archimedes' exclamation of \"Eureka!\" after jumping into a bath and realizing that held " \
            "the key to the problem he was trying to solve. (See below for details.)\nThe Eureka Moment " \
            "shows up a lot on diagnosis-mystery medical shows, such as House, in which he does it in " \
            "nearly every episode, and in the first episode of Grey's Anatomy, which isn't even a " \
            "medical detective show! It may also show up on telenovelas or soap operas with some " \
            "ongoing secret that defines a character or even the main plot. The truth is often almost " \
            "revealed several times, by easily overheard conversations or weak evidences, and each time " \
            "the status quo is kept with some contrived explanation. When the Eureka Moment takes " \
            "place, The Reveal is not the result of a confession or an evidence that is too solid to be " \
            "ignored, but instead the result of the hero putting all the small hints together and " \
            "figuring out the truth by himself. In this case, expect a wave of several flashbacks of " \
            "those hints before the \"Eureka!\".\nNot to be confused with a Bat Deduction. While both " \
            "can initially appear almost identical, a Eureka Moment leads to a coherent chain of " \
            "reasoning that the detective can explain to the bystanders later; whereas a Bat Deduction, " \
            "if it gets explained at all, makes even less sense after the explanation. However, " \
            "although logically sound, the Eureka Moment may be enough to convince the one who came to " \
            "it, but not to convince others (specially a court of law). In this case, the character may " \
            "began a quest to obtain a Smoking Gun to prove things beyond any reasonable doubt.\nOften " \
            "used as a Deus ex Machina, albeit one that is acceptable more often than annoying. If the " \
            "detective actually takes the idea literally rather than uses it as an inspiration, that is " \
            "I Was Just Joking.\nCan even happen in your sleep, with Dreaming the Truth.\nHas no " \
            "relation to a small town full of scientists. Or mecha with surfboards.\nCompare Shaggy " \
            "Search Technique and You Were Trying Too Hard. See Placebo Eureka Moment for when there " \
            "wasn't any external inspiration, but they act like there was, and Love Epiphany, when the " \
            "insight gained is that one party loves the other. See also Explain, Explain... Oh, Crap! " \
            "for a similar situation where instead of finding a solution, someone becomes aware of a " \
            "problem.\nMay contain unmarked spoilers."

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
