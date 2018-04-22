from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class UncomfortableElevatorMomentTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "UncomfortableElevatorMoment"

    def get_long_name(self):
        return "Uncomfortable Elevator Moment"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/UncomfortableElevatorMoment"

    def get_rdf_element(self):
        return "UncomfortableElevatorMoment/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Subverted in Die Hard with a Vengeance. McClane gets into an elevator to go down to the "
                "Federal Reserve's vault with three security guards and Detective \"Otto\", and just at the "
                "point where uncomfortable silence begins, McClane catches a reflection of Otto's badge and "
                "the number \"6991\", allowing him to suddenly deduce that Otto killed NYPD detective Ricky "
                "Walsh and stole his badge, and he's surrounded by a group of Simon's men. Also, he notices "
                "that one of them accidentally calls the elevator a \"lift\". The answer: McClane makes "
                "some petty small talk about the lottery, and then when he says he's got the \"tickets\", a "
                "gunfight ensues that ends with Otto getting his head blown off."}

    def get_categories(self):
        return ['ComedyTropes']

    def get_general_description(self):
        return "(For the proper reading experience, run the music from this video while reading this " \
            "page.)\nIn several European cultures, there is an unspoken code of behavior that applies " \
            "inside elevators, and also sometimes on trains and other modes of public transportation: " \
            "when someone enters an elevator, the custom is to face the front and stand in silence " \
            "whilst absentmindedly watching the floor numbers change. If there is any conversation, it " \
            "amounts only to small talk. An individual who breaks with this custom, for example facing " \
            "the other passengers, is often a source of considerable unease to the other individuals in " \
            "the elevator with you. The protocol does vary a lot between cultures, even between " \
            "neighboring countries; for example, the UK has the elevator protocol, while almost none of " \
            "Europe does. Depending on where you are, you might be expected to greet the other people " \
            "in the elevator and/or make light conversation, or to completely ignore them. This is " \
            "apparently a part of basic animal behavior, too: primates in small enclosed spaces " \
            "instinctively avoid drawing attention to themselves. The cultural differences in elevator " \
            "protocol reflect differences in what behaviour is inconspicuous. And yes, primates \u2014 " \
            "monkeys go quiet too, but rats tend to fight.\nParticularly in visual fiction, the Western " \
            "\"protocol\" is often milked to generate ironic, uncomfortable silences from characters " \
            "inside the elevator, when some other reaction might well be expected or justified. In " \
            "short: an Uncomfortable Elevator Moment.\nUncomfortable Elevator Moments traditionally " \
            "take place inside The Elevator from Ipanema. The elevator \"music\" itself often forms " \
            "part of the humor and/or tension in the scene, but will get cut off abruptly when the " \
            "scene ends. It can also take the form of a Mid-Battle Tea Break in a fight.\nFor added " \
            "discomfort, cue the fart, with an elevator filled with many, many people.\nIf it becomes " \
            "overly long, it may overlap with Leave the Camera Running."

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
