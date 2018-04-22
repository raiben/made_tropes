from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class TechnologyMarchesOnTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "TechnologyMarchesOn"

    def get_long_name(self):
        return "This entry is trivia, which is cool and all, but not a trope. On a work, it goes on the " \
            "Trivia " \
            "tab.\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\n\t\t\n\t\tTechnology " \
            "Marches On"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/TechnologyMarchesOn"

    def get_rdf_element(self):
        return "TechnologyMarchesOn/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Throughout Die Hard with a Vengeance (1995), Simon Gruber has John McClane and Zeus Carver "
                "driving all around New York City to answer specific payphones where Simon issues different "
                "instructions, and he bluffs the NYPD off their radios by insinuating some of the bombs "
                "were keyed to police frequencies... then he locks up the entire New York switchboard by "
                "calling a popular radio station about the fake bomb he planted in a school, to destroy the "
                "other means of communication the NYPD could've had. Cell phones would've beaten both in a "
                "second (but then, Simon would've probably had something for that eventuality as well.)\n "
                "Under heavy loads, cellular phone networks jam as well. A real life example would be "
                "during the Boston Marathon bombing in 2013."}

    def get_categories(self):
        return ['Trivia']

    def get_general_description(self):
        return "So little Timmy is watching a show from the 1990s. In one episode, the characters are all " \
            "excited because of a new computer game that will be released very soon. A computer game " \
            "\u2014 on CD-ROM!\nAnd Timmy says, \"'CD-ROMs?\"\nYou see, Technology has marched on, and " \
            "things like CD-ROMs and VHS cassette tapes and so on have relatively recently become " \
            "either so little-used as to be obscure, or obsolete altogether. This isn't Zeerust, which " \
            "is about futuristic tech becoming old rather than about modern tech becoming old. The " \
            "important qualifications of this trope are as follows:\n Show takes place in modern or " \
            "modern-ish times, usually the not-so-distant past.\n Show makes reference to something, " \
            "usually a form of technology, that is \"The next big thing\" or \"state of the art\", and " \
            "indeed it was \u2014 at the time the show was made.\n Said technology has since proved to " \
            "be impractical, has become obsolete, is at least gradually on its way out, or it is just " \
            "not in the spotlight anymore.\n Cue Hilarious in Hindsight for those who remember when " \
            "said tech was either very common or hyped as the next big thing.\nAs far as that last " \
            "point is concerned, remember that there have been spectacular technological leaps in just " \
            "the past twenty years \u2014 within the lifetimes of many (read: most) Tropers, in " \
            "fact!note\u00A0And if you haven't experienced it yet, don't worry. The first time will hit " \
            "you completely by surprise sometime within the next five years. For the most part, once a " \
            "technology is invented, it tends to develop at warp speed. Remember, it took only about 65 " \
            "years (1903-1969) to go from one rickety plane barely able to get off the ground to " \
            "putting a man on the MOON! So this can lead to some odd moments for those who grew up " \
            "watching certain things go from \"absolutely essential\" to \"taking up space in your " \
            "basement\".\nTo clarify, an excellent example would be a scene in Friends where Chandler " \
            "gleefully describes all the awesome features of his brand-new computer:\nThere was a time " \
            "when these specifications would be mockingly contrasted with a modern counterpart. " \
            "However, technology has moved on so far and so fast that Chandler's computer is now " \
            "unimaginably primitive; these days, even a low-end smartphone is several times more " \
            "powerful than that in every way, while fitting in the user's pocket and costing " \
            "considerably less than he would have spent. Because of this, most writers nowadays don't " \
            "get too specific about computer performance, to avoid sounding dated before " \
            "long.\nSomewhat related are those moments, during not-so-old films, where you realize the " \
            "entire plot could be resolved with something the world takes for granted today. (Cell " \
            "Phones, perhaps.) A related and increasingly common source of humor shows down-on-their- " \
            "luck characters as only able to afford the kind of older technology found in thrift stores " \
            "today. Additionally, shows set in the past will often lampshade this for humor.\nA Long " \
            "Runner might even have its earlier episodes/books/etc. have one level of technology, and " \
            "later installments have more up-to-date technology with little or no Hand Wave at " \
            "all.\nOften turns a work into an Unintentional Period Piece. Can sometimes be a Trope " \
            "Breaker: a change in cultural context that affects Tropes. A cousin of sorts to Our " \
            "Graphics Will Suck in the Future. See Magic Floppy Disk for cases when the tech onscreen " \
            "in a futuristic series was dated when the show was made.\nSee also Computer Equals Tape " \
            "Drive, Science Marches On, and some examples of Aluminum Christmas Trees. Long-Runner Tech " \
            "Marches On is when this happens In-Universe. Contrast I Want My Jetpack, where the writers " \
            "overestimated the advance in technology. A fictional world where Technology doesn't march " \
            "on despite the passage of time is in Medieval Stasis."

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
