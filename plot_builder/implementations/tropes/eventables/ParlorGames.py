from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class ParlorGamesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "ParlorGames"

    def get_long_name(self):
        return "Parlor Games"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/ParlorGames"

    def get_rdf_element(self):
        return "ParlorGames/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "The villain of Die Hard with a Vengeance used Simon Says in his games. His name is Simon, "
                "so he has a lot of fun with it."}

    def get_categories(self):
        return ['Media']

    def get_general_description(self):
        return "Before Board Games, Card Games, Tabletop Games, Video Games, and Web Games came along, " \
            "people just had their own persons to play games with guests. These are known as Parlor " \
            "Games. In the past, these were used in fiction for the same purpose as Board Games are " \
            "these days. Nowadays, it's either a Discredited Trope used to show how boring or geeky the " \
            "people playing are, or it's used as an actual Plot Device.\n Simon Says, a children's game " \
            "where someone gives orders (usually silly things like \"clap your hands\" or \"jump up and " \
            "down\"). Everyone playing has to follow the commands as long as they're preceded by " \
            "\"Simon says\". So if \"Simon says clap your hands\" you have to clap, but just \"clap " \
            "your hands\", you don't. You're out if you either follow the command without the \"Simon " \
            "says\" or don't follow it when they do say it. One variation has Simon do an action in " \
            "addition to saying one, but you must do what \"Simon says\". Usually, Simon will do and " \
            "say the same thing, but it could lead to situations where \"Simon says clap your hands\" " \
            "but he physically jumps up and down as a trick; the proper action is to clap your hands. " \
            "Last of the group still in usually gets to be the next one to call out the orders. This " \
            "game can be challenging enough that it can still be used legitimately in fiction.\n Twenty " \
            "Questions, a game where, counting the first question (usually if it's animal, vegetable, " \
            "or mineral), the players can ask no more than twenty questions to guess what the active " \
            "player is thinking of, and all questions after the first must be the \"yes or no\" kind. " \
            "Usually parodied now instead of played straight. Computers can play it quite well, e.g. " \
            "20Q and Akinator.\n Who Am I? is an inverted variant where each player has a post-it note " \
            "on their forehead and take turns to ask the other players questions to figure out what's " \
            "written on it (normally a famous person's name). Often played straight and used for the " \
            "silliness of everyone having post-its on their heads. The names on the notes will often " \
            "reflect or contrast with the person they're given to.\n I Spy, a guessing game similar to " \
            "but even more basic than Twenty Questions. The active player thinks of something within " \
            "their line of sight and tells everyone else its color or first letter. They try to guess " \
            "what it is. Only ever played by really bored characters.\n Musical Chairs, is usually just " \
            "played in children's parties now. Someone sets up enough chairs for all but one of the " \
            "players to sit on. They walk in a circle while some music is played for a short time. As " \
            "soon as it stops, everyone tries to sit in a chair, often resulting in a Big Ball of " \
            "Violence. The one who can't is out, and one chair is removed for the next round, until one " \
            "chair is left, and the one sitting is the winner.\n Charades, nowadays the lowest of these " \
            "games in fiction. Unless it takes place in the past, it rarely is portrayed for any reason " \
            "other than to show what losers the players are. It is played by acting out the words the " \
            "active player is thinking, puns and homophones allowed. The only other clue was to hold up " \
            "a finger for each word in the answer, and fingers for which word is being played. Such " \
            "improvised Hand Signals are sometimes used by a character to attempt to convey information " \
            "which for whatever reason, such as being mute, they cannot simply say aloud.\n Pictionary " \
            "is Charades with drawings, where one partner must draw the clue instead of acting it out. " \
            "This variant is more common in animation for obvious reasons. Sometimes the drawings " \
            "aren't seen by the viewer.\n Blind Man's Bluff, is usually seen in portrayals of older " \
            "times. One player is blindfolded, while the others hide. The blind man has to find the " \
            "other players. This game is sometimes depicted as a flirtatious man looking for giggling " \
            "young women in a parlor.\n Marco Polo is a variation on Blind Man's Bluff, with three " \
            "differences: a) It usually takes place in water, such as a pool. b) The hunter doesn't " \
            "wear a blindfold, but rather just keep their eyes shut. c) Most importantly, the hunter " \
            "can call out \"Marco!\" as often as they like, and if the hunted ones hear it then they " \
            "must respond with \"Polo!\". It's pretty much a miniature version of submarine warfare, " \
            "sonar and all.\n Truth or Dare is stereotypically most common at a slumber party, but can " \
            "take place in other situations as well. The very point of this game is to elicit personal " \
            "revelations if someone picks \"Truth,\" or wacky hijinks if someone picks \"Dare\"; " \
            "therefore, just by playing the game normally, it's quite likely that the events of the " \
            "game will generate results interesting enough to be the plot of a story. Fan Fic writers " \
            "know this very well, and Truth or Dare fics are practically a genre.\n I Never is a " \
            "similar game to Truth or Dare. Usually played more as a drinking game, although other " \
            "forfeits are common. The premise is for one person to say something which (hopefully " \
            "truthfully...or not, as the case may be) they have never done, and all the other players " \
            "have to commit the forfeit if they have done that thing.\n Spin the Bottle and Ten Minutes " \
            "in the Closet (or whatever variation) are the classic young-coed-teen-party games. In the " \
            "first one, sit in a circle, take turns spinning a bottle and kiss the first member of the " \
            "opposite sex it points to. In the second, pull names/number out of a hat to form couples " \
            "and go into the closet for two minutes and... amuse yourselves in some fashion. This is " \
            "often a way to trap/nudge a character into his/her First Kiss, to set up/exacerbate " \
            "romantic jealousies or to contrast different levels of sexual activity among a bunch of " \
            "kids of the same age. There will be much awkwardness, blushing and wiping of sweaty " \
            "palms.\n Mafia divides the players into two teams. One team is initially much smaller than " \
            "the other, but the composition of the teams is unknown to the members of the larger team. " \
            "The game alternates between turns during which the larger team keep their eyes shut, " \
            "allowing the smaller team to communicate in secrecy, and turns during which all players " \
            "claim they belong to the larger team. The elimination of a player is debated every turn. " \
            "Paper sheets or cards are often used to create the teams at the beginning and to " \
            "\"unmask\" any player who was just eliminated. A referee is normally required. " \
            "Furthermore, a single player of the larger team has a hidden turn of his own, during which " \
            "he learns the true allegiance of another player. Additional roles and teams can be " \
            "introduced, potentially leading to at least one Double Reverse Quadruple Agent. In " \
            "fictional works, Ten Little Murder Victims will sometimes play this kind of game right " \
            "before it becomes the plot.\n The Werewolves of Miller's Hollow is one of many commercial " \
            "versions, with a dedicated deck of cards."

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
