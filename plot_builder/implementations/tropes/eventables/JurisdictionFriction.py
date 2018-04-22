from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class JurisdictionFrictionTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "JurisdictionFriction"

    def get_long_name(self):
        return "Jurisdiction Friction"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/JurisdictionFriction"

    def get_rdf_element(self):
        return "JurisdictionFriction/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Averted in Die Hard with a Vengeance. The NYPD Captain is ordering his men to search the "
                "schools and challenges the FBI Agent not to pull a jurisdictional stunt. The FBI Agent has "
                "kids in one of the threatened schools, and he's more than happy to help."}

    def get_categories(self):
        return ['CrimeAndPunishmentTropes']

    def get_general_description(self):
        return "When two or more law enforcement organizations both can lay claim on a particular criminal " \
            "case or suspect they will rarely see eye-to-eye on the best way to prosecute/investigate " \
            "the case. In the US, local cops vs. the Federal government (FBI, DEA, etc) is the most " \
            "common setup. Usually, the locals will want to shut down a petty crook to protect their " \
            "town and the \"little guy\", while the Feds are focused on the big picture and would " \
            "rather he go free so they can focus on building a case against the \"big fish\" higher up " \
            "the criminal ladder. When a case is particularly sensitive or difficult, the friction may " \
            "be reversed: each group of investigators wants to absolve themselves of jurisdiction to " \
            "avoid the problems that will come with it. This is most likely to happen if one of the " \
            "groups is under pressure to improve their conviction rate and does not want to risk taking " \
            "on a case they cannot solve.\nJurisdiction Friction may also occur at the initial crime " \
            "scene: the hero investigator will barely have the time to unearth a few clues before the " \
            "rival investigation outfit shows up to flash badges all over the place and claim " \
            "jurisdiction. At this point, the hero will either turn Vigilante Man or move on to a new " \
            "case that's oddly reminiscent of the old one.\nWhich side of the dispute is sympathetic " \
            "and which is heartless/incompetent/arrogant/corrupt/trigger happy/working for the shadow " \
            "government depends entirely on who the main characters are. FBI agent series such as The " \
            "X-Files and Without a Trace naturally will have them in the right, while a Police " \
            "Procedural like Law & Order is frequently on the other side.\nIn addition to local versus " \
            "Feds, the friction can occur between other law enforcement subdivisions over the same " \
            "suspect, like drug enforcement officers versus homicide investigators, or simply one of a " \
            "city's police districts versus another. Internal Affairs can also get involved at some " \
            "point. And everybody has it in for the Private Detective.\nOccasionally, the normal effect " \
            "is inverted: the friction lies in everyone trying to shove off responsibility, if any part " \
            "of the investigation is likely to be unduly burdensome.\nCompare Right Hand Versus Left " \
            "Hand and We ARE Struggling Together for when the factions bickering over a common goal are " \
            "not part of any government."

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
