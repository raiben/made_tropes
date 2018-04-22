from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ConfiscatedPhoneTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ConfiscatedPhone"

    def get_long_name(self):
        return "Confiscated Phone"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ConfiscatedPhone"

    def get_rdf_element(self):
        return "ConfiscatedPhone/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane hijacks a car to use a car phone which then dies "
                "out. Earlier, Zeus needed to answer Simon's call on a payphone another person is using."}

    def get_categories(self):
        return ['StealThisIndex']

    def get_general_description(self):
        return "John Doe is using a phone, typically now it's a cellphone, but up until about the 1980s it " \
            "was a Pay Phone or in rare cases, his or another person's home phone. Richard Roe decides " \
            "he needs to use the phone. Richard will either interrupt the call (for a pay phone or a " \
            "home phone) or steal or confiscate John's cell phone. If Richard Roe just takes the phone " \
            "and isn't planning to give it back, that's stealing. If a police officer or public " \
            "official takes a phone because there's an emergency, that's a confiscation, because " \
            "presumably the owner will eventually get the phone returned.\nIn the case of a pay phone " \
            "or other landline, seizing a phone to use for a call is actually legal in the United " \
            "States if you have an emergency. Now, how do you know what is an \"emergency\"? Well, " \
            "every telephone book in the United States had a notice defining what an emergency is. \"An " \
            "emergency is a situation where life or property is in jeopardy and the prompt summoning of " \
            "aid is essential.\" What that means is if your car got hit and no one is injured, you " \
            "don't have an emergency, i.e. you can wait until the person finishes their call to get a " \
            "tow truck. But, if your dog or cat was hit by a car, a dog or cat is \"property\" and not " \
            "getting hold of a veterinarian or a cab \"promptly\" to take them there (for \"aid\") " \
            "means your \"property\" is in jeopardy of dying, and this is a valid reason to demand " \
            "emergency use of a phone.\nIn a lot of these cases, it might not be an emergency, it might " \
            "be Richard Roe just needs a phone in a hurry and steals one. In an older work, when " \
            "seizing control of the payphone, expect Richard to tell the person on the other end " \
            "\"He'll call you back\" before hanging up and dialing their own call.\nCompare Hero Stole " \
            "My Bike, where a vehicle is taken in an emergency."

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
