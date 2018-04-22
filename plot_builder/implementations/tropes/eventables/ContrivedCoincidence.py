from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ContrivedCoincidenceTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ContrivedCoincidence"

    def get_long_name(self):
        return "Contrived Coincidence"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ContrivedCoincidence"

    def get_rdf_element(self):
        return "ContrivedCoincidence/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane is chasing Simon Gruber through the half-finished "
                "aqueduct, when the latter blows a dam and floods it. The water pressure shoots McClane out "
                "of a drainspout literally the moment Zeus passes it, allowing him to pick him up and "
                "continue the plot. Had the two missed each other and taken any time to reconnect, they "
                "would have missed their opportunity to later board the boat and Gruber's plan would have "
                "gone off without a hitch. Not to mention, of the hundreds of schools in New York City, the "
                "one Simon has planted his bomb in is the one where Zeus (who only entered the story "
                "randomly) has his two kids enrolled.\n The school may not be so much of a contrived "
                "coincidence, just not explained. McClane only met Zeus because Gruber forced him to be in "
                "that area. It makes a sort of sense that Gruber picked the area because he was already "
                "there to plant the explosives in the school there. So the chances of a local having kids "
                "at that school is much much higher."}

    def get_categories(self):
        return ['OlderThanSteam']

    def get_general_description(self):
        return "In order to keep a story moving, things need to happen a certain way. Sometimes everything " \
            "is carefully set up and orchestrated, so that events unfold in an organic, natural " \
            "fashion. More often than not, though, things happen the way they do simply Because Destiny " \
            "Says So.\nThere's just one tiny little problem with that theory: Sometimes, Destiny " \
            "doesn't say so.\nContrived Coincidence describes a highly improbable occurrence in a story " \
            "which is required by the plot, but which has absolutely no outward justification \u2014 " \
            "not so much as a character saying There Are No Coincidences. The concept of \"destiny\" is " \
            "glossed over altogether, and the events in question are simply disguised as mere " \
            "happenstance. This would be jarring, but most of the time no attention is drawn to the " \
            "event at all. It's just a narrative convention designed to skip over lots of irrelevant " \
            "stuff by putting the important events all together, leaving the audience to forget the " \
            "improbability of the event.\nFor example, when two characters are separated in a huge " \
            "battle involving millions of combatants, they will bump into each other again just in time " \
            "for one to save the other's life. This is not highlighted as an example of destiny or " \
            "fortuity in any way, and in fact the improbability of the two people meeting again at such " \
            "a convenient moment is ignored altogether. If the coincidence is noted, it will be in the " \
            "form of \"lucky you showed up when you did\" as if it provides some justification to the " \
            "events that just transpired.\nIn many an action/adventure show or movie, the protagonists " \
            "are introduced to at the very beginning or portrayed to retain various gadgets that " \
            "invariably play perfectly into a dire situation they find themselves in later on. It has " \
            "the potential to be reasonable, such as bringing hiking equipment to a mountainous terrain " \
            "mission, but more often than not it's just a flat-out Asspull. Honestly, what didn't " \
            "Batman \"just so happen to\" carry in that little belt of his? (For that matter, RPGs and " \
            "Adventure games are particularly common offenders, as inventory coincidences are often " \
            "used to maintain the progression of gameplay.)\nIt's not Destiny, it's not By Design; " \
            "heck, the writer may not even bother calling it a coincidence. It just happens. Deal with " \
            "it and move on.\nIn cases where the coincidence is acknowledged, it's likely a Lampshade " \
            "Hanging. Characters may invoke Maybe Magic, Maybe Mundane for that.\nCan be justified to a " \
            "limited extent by the Anthropic Principle (see also The Other Wiki). Unlikely coincidences " \
            "are bound to happen once in a while. Exceptional things don't happen to the main " \
            "characters because they are main characters; rather, they are designated main characters " \
            "because exceptional things happen to them. In other words, there would be no story without " \
            "this first exceptional coincidence. The earlier in the story the plot-driving coincidences " \
            "occur, the more leeway the writer has with them.\nExcept for Farce. Contrived Coincidence " \
            "is one of the driving forces of Farce, decreed by the Rule of Funny. This is a major " \
            "reason why wariness is needed in other genres; too much of it will make the story " \
            "farcical.\nOne, less justifiable use for it is Doing In the Wizard. When the creator " \
            "requires a coincidence, or worse, a combination of them, not to move the action forward " \
            "but to say that it really could happen mundanely, it's not magic or the supernatural, the " \
            "effect is usually not pleasing. Audiences disliked it as far back as the ancient Greeks, " \
            "and Aristotle deplored it in Poetics.\nMake note that like its sister trope Theory of " \
            "Narrative Causality, this is one of the most pervasive tropes out there. Remember though, " \
            "that just because a work uses this trope is not an automatic black mark against it. Even " \
            "the greatest works out there sometimes need a great leap to get the plot to go in an " \
            "interesting direction.\nFor a more grandiose or plot-wrapping version, see Deus ex " \
            "Machina. See also Fridge Logic for the moment it sinks in, and Not My Driver for the " \
            "vehicular version.\nIt's a Small World After All is a subtrope of this. A person who is a " \
            "Weirdness Magnet tends to be a walking contrived coincidence. So is the variant of Framing " \
            "the Guilty Party where the one doing the framing didn't know that party was guilty. Too " \
            "many contrived coincidences may result in One Degree of Separation. Often, these can " \
            "disguise a Gambit Roulette as The Plan."

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
