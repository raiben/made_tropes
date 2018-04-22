from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ContinuityLockOutTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ContinuityLockOut"

    def get_long_name(self):
        return "Continuity Lock-Out"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ContinuityLockOut"

    def get_rdf_element(self):
        return "ContinuityLockOut/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance (1995) has a memorable allusion to \"that thing in the building "
                "in L.A.\", which knowledgeable viewers will recognize as a Continuity Nod to the attempt "
                "by Hans Gruber and his gang of thieves to rob the Nakatomi Plaza tower in the original "
                "1988 Die Hard movie. Even though there's a brief flashback to the climax of the 1988 film "
                "within the 1995 sequel, it can be difficult for first-time viewers to understand why Simon "
                "Gruber (Hans's brother) is so consumed with the desire to exact revenge on John McClane, "
                "the series' hero. The 1995 film even has an offscreen conversation between John and his "
                "ex-wife Holly, who was a major character in the first Die Hard (and is mentioned again in "
                "the fourth movie, Live Free or Die Hard, in 2008) and is the subject of the '95 film's "
                "closing punchline, which seems to come out of nowhere and make for a somewhat confused "
                "ending if you are new to the franchise.\n Although McClane does briefly explain to Zeus "
                "that he dropped Simon's brother off a building not long after The Reveal."}

    def get_categories(self):
        return ['ContinuityTropes']

    def get_general_description(self):
        return "The writers have let the mythos they have generated get so thick and convoluted that a " \
            "newcomer has very little chance of understanding the significance of anything. They are " \
            "'locked out' of understanding the story by all the continuity.\nThis is one of the main " \
            "bones of contention between creators and executives. Executives generally want each " \
            "episode to potentially bring in new audience. Creators generally want to entertain the " \
            "audience they have. In a rare case of this wiki taking the side of the executive meddlers, " \
            "we have to admit that continuity lock-out is never caused by the execs. It has to be " \
            "written.\nThe standard answer to this issue is the Previously On segment: many shows open " \
            "each episode with a short capsule summary of prior events. Of course, Previously Ons have " \
            "their own drawbacks, such as inadvertently providing spoilers or flat-out not working " \
            "(because it is impossible to explain everything adequately in the space of 60 " \
            "seconds).\nWhy bother with the intense continuity at all? Simple: An intricate series- " \
            "spanning plot often results in a stronger and more interesting overall show. You may not " \
            "catch as many fans, but the ones you do get are yours for life. This does mean that you " \
            "have be sure to rope in as many as possible early on before the Lockout effect takes hold " \
            "to make the effort worthwhile.\nSome Long Runners and certain mediums (such as novels) are " \
            "designed to be engaged within a linear multi-volume fashion over a period of time, and the " \
            "authors can't reasonably be expected to keep everything entirely accessible to a newcomer " \
            "if they want to engage in any meaningful plot or Character Development; if you start " \
            "reading a seven-volume series at volume five and find yourself hopelessly lost, then you " \
            "arguably have only yourself (or in some cases the publisher) to blame.\nThis is " \
            "particularly prevalent in comic book series, more so than television or film, because " \
            "while most TV shows run for a maximum of a few hundred episodes (most of which are easily " \
            "obtainable one way or another) some comic book series run for much longer. (Like Superman: " \
            "Consistently in print since the 1930s). This, and the fact that comic books can be " \
            "incredibly rare (with the auction prices this entails), ensures that most new readers are " \
            "just going to either give up or ignore most of the last 70 years of continuity. In the " \
            "past, it wasn't uncommon for long-running series to actually recycle storylines with " \
            "little variation, in keeping with the Seven Year Rule.\nA Compressed Adaptation might " \
            "cause this. In Web Comics, this can be the impetus for an Archive Binge or a justification " \
            "for Archive Panic.\nThe rise of services like on-demand video have done wonders to push " \
            "this toward Dead Horse Trope status, especially as more series move toward airing fewer " \
            "episodes in order to put a higher production budget into each and making it easier to " \
            "catch up (Game of Thrones is the most potent example of this.) The internet allowing for " \
            "easy access of fan-made sources of information (see: The Wiki Rule) has also made this " \
            "less existent.\n\nExamples"

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
