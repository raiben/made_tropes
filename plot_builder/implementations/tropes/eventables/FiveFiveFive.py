from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class FiveFiveFiveTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "FiveFiveFive"

    def get_long_name(self):
        return "555"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/FiveFiveFive"

    def get_rdf_element(self):
        return "FiveFiveFive/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane must stop a bomb by dialing \"555 and the answer\" "
                "to the riddle the villain just gave."}

    def get_categories(self):
        return ['NumberTropes']

    def get_general_description(self):
        return "Virtually all US phone numbers on fictional programmes are made up of the following:\nArea " \
            "Code - 555 - four random digits\n\"555\" is an exchange number commonly thought to be " \
            "reserved by the phone companies for use by TV and movies in order to prevent prank phone " \
            "calls to real people. In fact, only 555-0100 through 555-0199 are now specifically " \
            "reserved for fictional use, and the other numbers have been released for actual " \
            "assignment. The 555 exchange was originally useful for this purpose because it was (in " \
            "North America) reserved for various internal phone company service numbers, so calling one " \
            "of the 555 numbers would not have reached an actual customer. In particular, in most areas " \
            "in North America (AREA CODE)-555-1212 connects with directory assistance.\nAnother fake " \
            "number used back in the 1950s through the 1970s when most of Southern California was " \
            "entirely one area code, 213, was to reserve the extension 1 plus the prefix in every " \
            "prefix, so that the number 462-1462 or 733-1733 was never a working number. Eventually the " \
            "714 area code would be split off from 213 in 1953 and later 818 would split from 213 in " \
            "the early 1980s, but Pacific Telephone continued the practice of reserving the " \
            "prefix-1-prefix number in every exchange as a non-working number. A number of TV shows and " \
            "made-for-tv movies took advantage of this fictional number feature.\nAs it happens, if the " \
            "area code is \"800\", \"888\", \"877\", \"866\", \"855\", or \"844\" (the US area codes " \
            "for toll-free dialing), \"555\" is a valid prefix. So 1-800-555-(four digits) will be a " \
            "real phone number. Not everyone knows that.\nA variation of this is IP addresses; media " \
            "will commonly use addresses such as 127.0.0.1 (which refers to the local computer) or " \
            "impossible addresses (an address in the most commonly used protocol, IPv4, is essentially " \
            "a 4-digit number in base-256, so any address with a \"digit\" 256 or greater is fake). " \
            "Similarly, any hexadecimal character higher than F is fake (Hex only uses the characters " \
            "0-9 and A-F). And to top it off, there are certain IP addresses that are reserved for " \
            "private networks and will never be assigned to internet-facing machines (see Real Life " \
            "section for more info).\nNot to be confused with A Kamen Rider of similar naming. Or a " \
            "popular timer IC of the same name.\nWorks set during an era when exchanges were commonly " \
            "specified as names (say, during World War II) may use the exchange name \"KLondike (or " \
            "KLamath)\" (followed, or not, by a 5 depending on the exact time period), which works out " \
            "to the same thing. Works actually from those eras normally don't; the songs \"Beechwood " \
            "4-5789\" and \"PEnnsylvania 6-5000\" are examples.\nSee also Logging onto the Fourth Wall " \
            "for the website equivalent."

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
