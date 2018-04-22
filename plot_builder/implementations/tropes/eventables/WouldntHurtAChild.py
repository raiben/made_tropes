from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class WouldntHurtAChildTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "WouldntHurtAChild"

    def get_long_name(self):
        return "Wouldn't Hurt a Child"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/WouldntHurtAChild"

    def get_rdf_element(self):
        return "WouldntHurtAChild/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance has Anvilicious moments about this: the line \"children may find "
                "it [the bomb]\" is uttered by both the good guy and a bad guy. This brings a question of "
                "doubt in the perpetrators' actions, and it's revealed the Big Bad never planted a real "
                "bomb, just a fake one, because \"he's a soldier, not a monster\"."}

    def get_categories(self):
        return ['MoralityTropes']

    def get_general_description(self):
        return "Many adult viewers and writers are upset about kids being harmed. Kid viewers aren't, but " \
            "then, kids aren't the ones doing the writing, are they? As a result, many characters on TV " \
            "Wouldn't Hurt a Child.\nThis is often done simply by not showing kids at all in action and " \
            "suspense shows, but sometimes it's rather conspicuous when characters seemingly go out of " \
            "their way to not hurt kids, or circumstances happen to conveniently align themselves so " \
            "that kids don't get hurt. For example, a slasher movie where the slasher just happens to " \
            "not encounter children in hiding, or the kids manage to be rescued just in time, while the " \
            "adults and teens get killed. It's also pretty common that when Even Evil Has Standards, " \
            "not harming children is one of them.\nIn fact, when this trope does get averted and " \
            "children do get harmed, it can often be shocking for the audience.\nSee Also Wouldn't Hit " \
            "a Girl for the female-specific version of this trope. See Friend to All Children for those " \
            "adults who not only don't hurt kids, but will actively protect them (even if the adults in " \
            "question are clearly evil). For video games, see Hide Your Children, where children aren't " \
            "even portrayed so as to avoid the implications that they could be hurt. For a more " \
            "specific form of Wouldn't Hurt a Child, in which very young children are shielded from " \
            "danger by the plot due to society's squeamishness about hurting babies, see Infant " \
            "Immortality.\nA common subversion is when a character who goes by this motto has to face a " \
            "Creepy Child, or worse an Enfant Terrible.\nMay be a form of Heroic Vow.\nOddly enough, " \
            "it's also Truth in Television as many gangs, such as the Mexican Mafia, brutally murder " \
            "their members that hurt children. This even extends to prison, where inmates, or even " \
            "prison-based gangs, that welcome robbers and murderers into their fold will not tolerate " \
            "someone who hurts a kid. In fact, killing one of these people often results in being well " \
            "liked by the other inmates.\nContrast Child Hater and Would Hurt a Child."

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
