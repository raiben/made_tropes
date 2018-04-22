from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class SuperCellReceptionTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "SuperCellReception"

    def get_long_name(self):
        return "Super Cell Reception"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/SuperCellReception"

    def get_rdf_element(self):
        return "SuperCellReception/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance, released in 1995, has the villain calling from the vault of the "
                "New York Federal Reserve Bank. While it's in Wall Street, this is still underground... and "
                "the phone somehow doesn't pick up the noise made by the heavy machinery picking up gold as "
                "he speaks."}

    def get_categories(self):
        return ['SpeculativeFictionTropes']

    def get_general_description(self):
        return "With the advent of the computer age, writers still don't quite know how to work cell " \
            "phones into a story. Half the time, the mere existence of the cell phone breaks the story " \
            "entirely unless the author invokes some rationale to lose, break, or disable them.\nThis " \
            "trope covers the other half, when writers have cell phones function like crazy James Bond- " \
            "esque communication devices. Except when the plot demands, they work in places that no " \
            "cell phone should \u2014 such as in a sewer, a cave system, Antarctica (which would only " \
            "be viable with a very expensive and large satellite phone), or even other worlds and " \
            "dimensions. They might probably come equipped with flawless webcams to boot.\nA sub-trope " \
            "of Plot-Sensitive Items. Futuristic communications not working have a Phlebotinum " \
            "Breakdown. Such a cell phone could be a Supernatural Phone, if it's justified in-universe. " \
            "Compare The Web Always Existed for another kind of devices working all logic. Contrast " \
            "Sudden Lack Of Signal, where a phone logically fails to work in a different " \
            "world.\n\nExamples"

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
