from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class PoliticallyIncorrectVillainTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "PoliticallyIncorrectVillain"

    def get_long_name(self):
        return "Politically Incorrect Villain"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/PoliticallyIncorrectVillain"

    def get_rdf_element(self):
        return "PoliticallyIncorrectVillain/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Simon Gruber of Die Hard with a Vengeance plays with this trope like a kitten does a ball "
                "of yarn. Although he comes from a family of former Nazis, he harbors no bigoted attitudes "
                "in particular. Still, he seems to delight in making people think he is bigoted, mostly "
                "because he thinks it's fun to anger people and/or fake them out. When first speaking to "
                "Zeus Carver, for example, Simon (who is German but can mimic American Accents quite well, "
                "and who knows that Zeus is an Angry Black Man because he's been watching him on hidden "
                "video cameras) says: \"So whot's yowuh name, boy?\" in twangy, Corrupt Hick fashion just "
                "to irritate Zeus; he then apologizes, explaining that he's fond of tasteless jokes. Later "
                "the trope is seemingly played straight when Simon calls John McClane a \"dumb Irish "
                "flatfoot,\" but this is due not to anti-Irish sentiment but to Simon's general bitterness "
                "toward John for having killed his brother, Hans, in the first Die Hard movie. Simon admits "
                "that he didn't even like Hans, but he is still determined to exact vengeance on anyone who "
                "messes with his family, saying \"There's a difference between not liking one's brother, "
                "and not caring when some dumb Irish flatfoot drops him off a building.\""}

    def get_categories(self):
        return ['EvilTropes']

    def get_general_description(self):
        return "Want to show that your Evil Overlord, or someone within The Empire is a genuine bad guy, " \
            "regardless of their rank in The Empire or how minor a character they are? Simple, all you " \
            "have to do is have them Kick the Dog, right? Well, what if there isn't a handy dog around? " \
            "Have them kick whatever minority race/species or gender/sexuality or lower class scum is " \
            "around instead to show that they're a really bad guy. Bonus points if either the heroes or " \
            "some highly sympathetic character is a member of said minority.\nDepending on how and with " \
            "whom this is used, it can sometimes come across as just slightly odd. It generally works " \
            "best with minor characters who have not had a lot of time in the attention of the " \
            "audience, since you can easily reveal that their Hidden Depths are really rather " \
            "unpleasant, thus allowing you to cement them as unlikeable or have the character graduate " \
            "from being an annoying obstacle to someone the fans will cheer to see put down.\nIt " \
            "doesn't always work as well with the Magnificent Bastard Evil Overlord types, particularly " \
            "if introduced late into their run as an antagonist. Because honestly, if the fandom hasn't " \
            "turned against the Overlord after the character in question may have murdered thousands or " \
            "even millions, enslaved people in The Empire wholesale, and so on and so forth, is having " \
            "the character be a little sexist or racist really going to automatically turn people " \
            "against them? (In particularly bad cases of Misaimed Fandom where the fans were already " \
            "using every scrap of evidence and threadbare argument to argue that the bad guys weren't " \
            "that bad, you may risk the character's fans declaring this to be a Fanon Discontinuity, " \
            "and possibly even splitting the fanbase). In these cases, to make it work, you might have " \
            "to do a purposeful Flanderization to your character and make them all about their bias. Of " \
            "course, that will also mean you've gone and derailed your own plot if you need to do it to " \
            "that extent...\nA notable key to this is that the racism, sexism, Fantastic Racism, or " \
            "whatever displayed by the character is often completely gratuitous or extraneous to the " \
            "rest of their villainy. Usually, whatever their goal might be, they don't have to be a " \
            "racist, speciesist, or sexist to accomplish it - but they are.\nThis is the reason why " \
            "Those Wacky Nazis and The Klan are at the bottom of the villain food chain, and it's a " \
            "good bet that the Politically Incorrect Villain will be the one going down in an Even Evil " \
            "Has Standards team-up.\nAlso, people might sometimes see this trope where it doesn't " \
            "exist. Some villains are simply bullying types who go after minorities without really " \
            "caring whether people will find it politically incorrect or not - and it doesn't have to " \
            "matter if their targets remind them of themselves in some way. Why do they do this? Genre " \
            "savviness, primarily; after all, minorities lack the numbers to fight back, and there's " \
            "nothing to be gained from Bullying a Dragon.\nCompare Evil Is Petty and He-Man Woman " \
            "Hater; Contrast Equal-Opportunity Evil. Note however that they are not mutually exclusive; " \
            "a villain can be progressive towards some groups but intolerant towards others. Compare " \
            "and contrast the Politically Incorrect Hero. May lead to Felony Misdemeanor if this " \
            "character type is thought to be more evil than outwardly flamboyant villains. Any and all " \
            "instances of Those Wacky Nazis qualify automatically, and A Nazi by Any Other Name often " \
            "does.\nThis is not when a villain is a minority who is portrayed in a politically " \
            "incorrect manner. That's Unfortunate Implications, assuming it's unintentional. This " \
            "should also not be confused with Values Dissonance, where the author apparently has these " \
            "attitudes."

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
