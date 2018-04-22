from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class AerithAndBobTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "AerithAndBob"

    def get_long_name(self):
        return "Aerith and Bob"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/AerithAndBob"

    def get_rdf_element(self):
        return "AerithAndBob/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Lampshaded a little in Die Hard with a Vengeance, where John McClane, archetypal New York "
                "EveryCop, runs into a militant black man played by Samuel L. Jackson. His name? \"ZEUS! AS "
                "IN FATHER OF APOLLO? MOUNT OLYMPUS? DON'T-FUCK-WITH-ME-OR-I'LL-SHOVE-A-LIGHTNING-BOLT-UP- "
                "YOUR-ASS ZEUS!\" And, for added yuks, John initially believes his name to be \"Jesus\" "
                "(the Spanish pronunciation) after hearing a character address him with \"Hey, Zeus!\" "
                "(Since \"Jesus\" and \"Zeus\" are deities in two incompatible religious systems, that "
                "counts as Fridge Humor.)"}

    def get_categories(self):
        return ['Starwars']

    def get_general_description(self):
        return "In some fantasy settings, people will have names that you would expect to see in real " \
            "life. In others, names are made up to sound exotic.\nAnd then you have the mixed approach: " \
            "people named Zelor and Lithnara alongside people named James and Catherine. Don't expect " \
            "the characters to acknowledge the distinction. Note that this doesn't count if the author " \
            "is making a distinction e.g. as a Translation Convention for different cultures (cf. The " \
            "Lord of the Rings, where the hobbits' and the nearby Men's Westron-language names are " \
            "\"translated\" as more real-world ones, but no others are), or in a cosmopolitan setting " \
            "where characters might be reasonably expected to have diverse cultural backgrounds without " \
            "this necessarily being explicitly stated.\nThis can also happen within an Overly Long " \
            "Name, where a Muggle-type name is liable to appear amid a long series of archaic names. " \
            "Most often, the \"normal\" name is \"Terry\", \"Scott\", \"Dave\", or \"Lyle\", because " \
            "those names are somehow inherently funny.\nIn stories set in The Future, new names can be " \
            "assumed to have been invented or become popular over the years, but older names would " \
            "still exist as well.\nThe Trope Namer is a combination of Final Fantasy VII, which has the " \
            "eponymous \"Aerith\" alongside names like \"Vincent\" and \"Barret\", plus a play on Alice " \
            "and Bob.\nNot to be confused (or transliterated) with Alice and Bob. When it's played for " \
            "laughs, it's an Odd Name Out. See also Special Person, Normal Name. Compare Melting-Pot " \
            "Nomenclature, Sesquipedalian Smith and My Friends... and Zoidberg."

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
