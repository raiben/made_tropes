from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SequelEscalationTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SequelEscalation"

    def get_long_name(self):
        return "Sequel Escalation"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SequelEscalation"

    def get_rdf_element(self):
        return "SequelEscalation/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance: In New York City."}

    def get_categories(self):
        return ['FilmTropes']

    def get_general_description(self):
        return "Sometimes a sequel is just the same story as the last one (Capcom Sequel Stagnation), or " \
            "downgraded by being Direct-to-Video (Starship Troopers 2: Hero of the Federation), or a " \
            "different story set in the same world (The Godfather II, the Star Trek films), or just the " \
            "next part in an ongoing series (Star Wars, The Lord of the Rings books and movies), or " \
            "even a Dolled-Up Installment (Super Mario Bros. 2).\nThis trope, on the other hand, is " \
            "when a sequel is made to be \"bigger and better\" than the last film, by taking one or " \
            "more elements from the first film and expanding upon it. The film makers feel a need to " \
            "\"top themselves\" in a sort of way.\nTake an action sequel, which has more explosions and " \
            "fist/gun/martial arts fights than the previous film. Or a slasher sequel, which has more " \
            "deaths, in more gory (and less realistic) ways. Sometimes what get expanded is the plot: " \
            "What started as a simple and straightforward plot in the first part may become " \
            "significantly expanded, deeper and more intricate in sequels.\nHow often this works " \
            "depends on if the expanded element is the one the audience liked. Choose the wrong " \
            "element(s), and it will be at the expense of the right element(s), and the audience will " \
            "not be pleased. Wrong elements can often be the toilet humor, sexual situations, " \
            "flanderization or meaningless action sequences.\nHowever, choose the right element(s), and " \
            "the sequel may even be considered superior to the first film. Usually these elements " \
            "involve the human element, expanding on the characters we care about, telling a dramatic " \
            "(or hilarious) story, and making the action sequences revolve around that.\nUsually, the " \
            "result is somewhere in the middle, often debated upon by the fans.\nTo avoid just " \
            "rehashing examples from Sequelitis, examples here should discuss the expanded element(s) " \
            "of the sequels.\nCompare Actionized Sequel, Sequel Difficulty Spike, Send in the Clones, " \
            "Serial Escalation, Up to Eleven, Sorting Algorithm of Evil, Power Creep. Big Damn Movie is " \
            "this trope applied to a film adaptation of a serial. Darker and Edgier often, but not " \
            "always, accompanies the upping of the stakes in sequels.\nContrast Lensman Arms Race and " \
            "Plot Leveling (both of which could be seen as symptoms of this trope's presence), Sequel " \
            "Difficulty Drop (difficulty getting lowered, although that doesn't preclude this trope in " \
            "other ways)."

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
