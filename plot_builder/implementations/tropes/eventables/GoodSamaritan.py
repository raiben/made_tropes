from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class GoodSamaritanTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "GoodSamaritan"

    def get_long_name(self):
        return "Good Samaritan"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/GoodSamaritan"

    def get_rdf_element(self):
        return "GoodSamaritan/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Zeus Carver from Die Hard with a Vengeance doesn't know anything about John McClane other "
                "than he's a white man in Harlem wearing nothing but a racist sandwich board sign. Despite "
                "being a rather unrepentantly bitter and biased man when it comes to white people, he saves "
                "him from a gang. Not that he necessarily wanted him to live, but he was afraid of what "
                "would happen if a white guy was killed on his block. Throughout the film, Simon Gruber "
                "calls him \"The Samaritan\"."}

    def get_categories(self):
        return ['CharactersAsDevice']

    def get_general_description(self):
        return "Part of being a Hero is taking up arms to fight the wicked and righting wrongs, even (or " \
            "perhaps especially) when no one else will. Some even have to fight the people they want to " \
            "help, but a rare few can count on the help of a Good Samaritan.\nThe Good Samaritan is a " \
            "character who, despite owing nothing to the hero helps them when they're at their weakest, " \
            "often at risk or cost to themselves. There are many variations, but they generally follow " \
            "this form: a wounded hero wanders in, while others pass him by (or even further harm the " \
            "hero), the Samaritan takes him in, tends his wounds and extends as much hospitality as " \
            "she's able. This has the bonus of roping the hero into owing her a debt and giving him a " \
            "reason to stick around the Adventure Town and fight off the Corrupt Corporate Executive " \
            "threatening the Samaritan. Also, in a pinch, she makes an excellent Love Interest what " \
            "with having proven she's got a heart of gold. (Good Samaritans who do not complicate the " \
            "hero's life like that may come across as a Deus ex Machina.)\nNot coincidentally, the " \
            "Samaritan is almost always a part of the blue collar or underclass of society. There's " \
            "almost no such thing as rich Samaritans in fiction. (Of course, in reality, one usually " \
            "needs money if he wants to make any real difference donating to a legitimate charity, let " \
            "alone starting one.) Interestingly, this is despite a pertinent aspect to the original " \
            "Biblical story that is often overlooked: \"No-one would have remembered the Good Samaritan " \
            "if he'd had only good intentions. He had money as well.\" All the same, it creates " \
            "Unfortunate Implications if someone in a privileged position sees others as helpless " \
            "without them; see White Man's Burden.\nIf the Samaritan follows the protagonist into the " \
            "m\u00EAl\u00E9e, expect her to be an Action Survivor to his Action Hero. Often overlaps " \
            "with The Chick, Innocent Bystander, Determined Homesteader, and Heroic Bystander.\nA nasty " \
            "subversion is that the Samaritan hasn't taken in a Hero, but a Viper intent on doing him " \
            "harm. If the villain the Samaritan helps is instead confused and curious at their " \
            "generosity, it may lead to the Samaritan becoming their Morality Pet prior to a Heel-Face " \
            "Turn.\nA lot of Superheroes are considered to be Good Samaritans taken Up to Eleven.\nThe " \
            "Trope Namer is one of Jesus' parables from The Bible, in which an Israelite is mugged and " \
            "left injured and naked on the side of the road. Several of his own people (including a " \
            "priest) simply walk past, and the only person who helps him is a Samaritan. However, this " \
            "parable carried some racial and cultural baggage lost to modern audiences. To Israelites, " \
            "Samaritans were a hostile if not enemy peoplenote\u00A0Samaritanism is an offshoot of " \
            "Judaism (or the other way around, from the perspective of the Samaritans) so the two " \
            "cultures might have seen each other they way Catholics and Protestants see each other now " \
            "\u2014 in agreement on the broad strokes, but disagreeing on the details, and having a " \
            "non-trivial amount of bad blood between them.. So when the traveler falls on the wayside " \
            "and the only one to help him is an enemy of his people, it carried a humanizing message " \
            "akin to Dark Is Not Evil (certainly, a story where a Samaritan was portrayed in a positive " \
            "light would have been a shock to the likely audience that Jesus was telling it to); the " \
            "modern day equivalent might be a Palestinian stopping to help an Israeli, or vice versa. " \
            "The closest trope to the above moral is probably I Was Just Passing Through. To further " \
            "complicate the story, the Israelites passed by the wounded man because the Sabbath was " \
            "beginning and it would be laborious to carry the man to safety, or in the case of the " \
            "priest, falling back on the excuse that he could reasonably assume the man was dead and " \
            "that being in contact with corpses was a gross impurity for a priest. The Samaritan story " \
            "shows that goodness is more important than blindly following the law. In many modern uses " \
            "of this trope, the Samaritan will protect and heal the hero even if the hero is explicitly " \
            "a hunted fugitive.\nThis Trope is often combined with No Good Deed Goes Unpunished (when a " \
            "Good Samaritan is treated negatively or unfairly) or with Androcles' Lion and/or Character " \
            "Witness (when what he does is rewarded).\nSub-Trope of A Friend in Need. See also " \
            "Samaritan Syndrome. Compare with Bad Samaritan, this character's moral opposite."

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
