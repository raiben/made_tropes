from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PhoneTraceRaceTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "PhoneTraceRace"

    def get_long_name(self):
        return "Phone-Trace Race"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PhoneTraceRace"

    def get_rdf_element(self):
        return "PhoneTraceRace/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Played with by the villain in Die Hard with a Vengeance."}

    def get_categories(self):
        return ['DiscreditedTrope']

    def get_general_description(self):
        return "A horror and police procedural trope where the police set up a phone trace to catch a " \
            "criminal but they need them to stay on the line for a certain amount of time. The amount " \
            "of time will vary, yet somehow the criminal will know the exact amount of time and " \
            "purposely hang up just before the police can get a trace. If it's a particularly high-tech " \
            "setup, expect to see a computer generated map showing the tracing process.\nEven if the " \
            "person on the other line is encouraged to keep the other person talking, it never seems to " \
            "work. The criminal will say everything they want and still always hang up a few seconds " \
            "shy of the minimum time to trace the number. In some cases, the criminal will say they're " \
            "aware of the phone trace or say how many seconds the call took. This trope is often used " \
            "by serial killers or any particularly clever character. A common subversion is to stay on " \
            "the line just long enough for a trace, but the purpose is to lead the police somewhere " \
            "else as part of the criminal's elaborate plan.\nUp until perhaps the late 1970s and early " \
            "1980s this was somewhat accurate. Telephone switches were racks of mechanical switches in " \
            "which, when you dialed a number - using a rotary phone, a line selector used the clicks to " \
            "determine which frame in the next digit to connect your call to. You dialed a 3, and the " \
            "relay went to the 3xx-xxxx rack, then the next digit of 7 would connect to 7 rack in the 3 " \
            "series, and so on, until you got to the last digit of the subscriber's number. If it was " \
            "in use, you got dumped to the busy generator. Otherwise, you got to hear the ring tone as " \
            "the line was rung. All these connections were created to make a physical connection " \
            "between your phone and the destination phone. That means, to trace a call on a mechanical " \
            "switch, they had to see where the wire ran to, then trace what that one was connected back " \
            "to. This also meant, if the trace wasn't finished before the call was, the \"sickening " \
            "sound\" of a call collapsing as the circuit was released for another call to go " \
            "through.\nIf the call was long distance, they'd have to send someone to the central office " \
            "that connected the call to the city, then trace it back to wherever it was connected from, " \
            "and so on. This is why if someone was making obscene phone calls long distance, it would " \
            "require many repeated calls to trace back the caller because of the time involved to " \
            "trace, say, a call over mechanical switches from Pasadena, California to Ellicott City, " \
            "Maryland. Traces from major cities, say, Los Angeles to Baltimore or Chicago, even over " \
            "mechanical circuits would be much faster, however because the calls didn't have to go " \
            "through intermediate cities.\nAs digital computers became more powerful, a switch " \
            "basically was a mainframe computer with a bunch of phone lines plugged into it instead of " \
            "a bunch of racks connected by mechanical relays. As a result, tracing a call means nothing " \
            "more than going to the console, entering the phone number and asking who is connected to " \
            "it. Eventually with the development of SS 7 switches, it got to be sophisticated enough " \
            "you could get it yourself in real time for a few dollars extra through Caller ID.\nAn " \
            "essential part of The Calls Are Coming from Inside the House.\nAs technology marches on, " \
            "this trope has morphed into tracing the computer connection, but the essence remains the " \
            "same. Is often a source of artistic license, since (unless the work is set in the 1960s or " \
            "earlier) the phone company can use their computer records tell the cops what numbers " \
            "called a given phone, and when, even months after the call.\nNot counting Caller ID, which " \
            "landline phones can get at a fee, and which is included on cell phones as part of the " \
            "service, giving you the caller's number (and possibly name) before you even answer the " \
            "phone."

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
