from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class IndyEscapeTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "IndyEscape"

    def get_long_name(self):
        return "Indy Escape"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/IndyEscape"

    def get_rdf_element(self):
        return "IndyEscape/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, McClane flees the water gushing through the aqueduct in a "
                "dump truck when the villains attempt to drown him."}

    def get_categories(self):
        return ['ActionAdventureTropes']

    def get_general_description(self):
        return "The character is chased down a tunnel by something very large, clich\u00E9dly a boulder or " \
            "a giant monster. There's only one thing to do: RUN!!\nThere's no stopping the rolling " \
            "boulder. You cannot avoid it or reason with it. It will just keep rolling towards you, " \
            "destroying everything in its path until it makes sure you are a steaming, bloody pancake " \
            "on the floor. The only way out is to race down the corridor as fast as you can, and " \
            "finally dive into some passageway that is too small for it to enter when you reach the " \
            "end. Alternatively, clearing a pit which the obstacle will fall into will also do the " \
            "trick.\nIn the event that the chase takes place outside in open space, it sometimes seems " \
            "that the characters can only run forward.\nClosely related is a bridge that collapses in " \
            "the hero's wake.\nWhile often an extended sequence, an Indy Escape scene can also be used " \
            "as part of a Death Course.\nIn video games, it is sometimes possible to get behind the " \
            "rolling obstacle of doom, making the whole stage much easier. In 3D video games, the " \
            "camera will often fixate on the boulder and obscure the path you have to run, making the " \
            "whole stage much harder.\nCompare with Rise to the Challenge, Escape Sequence and " \
            "Descending Ceiling. When the pursuing object or creature is full screen height, it's an " \
            "Advancing Wall of Doom. After the escape is over, expect someone to quip \"Wasn't That " \
            "Fun?\"\nUnrelated, despite the name, to the Indy Ploy. In order to turn an Indy Escape " \
            "into an Indy Ploy, the character would have to improvise pretty quickly.\nIf there are " \
            "some nooks and crannies along the way, but a neverending supply of hazards as well, it's a " \
            "Corridor Cubbyhole Run. If it's actually possible to evade the danger by moving sideways " \
            "out of the way, but our character never does, he or she has fallen prey to One-Dimensional " \
            "Thinking.\nSee also Raiders of the Lost Parody."

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
