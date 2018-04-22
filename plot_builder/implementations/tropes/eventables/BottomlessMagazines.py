from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class BottomlessMagazinesTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "BottomlessMagazines"

    def get_long_name(self):
        return "Bottomless Magazines"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/BottomlessMagazines"

    def get_rdf_element(self):
        return "BottomlessMagazines/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "In Die Hard with a Vengeance, the security guard in the bank vault fires his shotgun about "
                "15 times before coming up empty, nearly twice as many shells as a typical law-enforcement "
                "model can hold."}

    def get_categories(self):
        return ['GunsAndGunplayTropes']

    def get_general_description(self):
        return "Possibly one of the oldest and most abused tropes when it comes to gunplay is the frequent " \
            "ignorance of just how many shots the good guys/bad guys have fired from their guns without " \
            "stopping for a reload. In Real Life, most revolvers hold between 5 to 8 shots, depending " \
            "on caliber, while semiautomatic handguns have magazines that usually hold 10\u201315 " \
            "shots. Pump-action, bolt-action, and lever-action longarms generally hold 5\u20138 rounds " \
            "(but the magazine can easily be topped off) and detachable-magazine semi-automatic or " \
            "automatic rifles generally hold at least 20, if not 30 rounds.note\u00A0That great big " \
            "circular magazine seen on the classic Thompson Submachine Gun in gangster movies holds 50 " \
            "rounds in real life, and an even bigger one holds 100. But keep a running count, and " \
            "you'll sometimes see a weapon go for much longer without hesitation.\nAmmo capacity of " \
            "guns on TV seems to be totally dependent on how much drama and suspense is needed. The " \
            "hero will always have plenty of ammo to mow down the mooks, but will run out just before " \
            "reaching the Big Bad, or confront him with One Bullet Left. Reloading is usually only done " \
            "when it adds to the drama or when you need to show off how badass the gunslinger is. If " \
            "someone is firing an automatic weapon that's belt-fed or has a large banana-shaped " \
            "magazine in it, forget it \u2014 he's never going to run out until you shoot him dead. The " \
            "only thing that seems to stop a movie or TV gun from firing is the inevitable and dramatic " \
            "jam.\nCan be partially explained by editing in some of the less unrealistic movies. If " \
            "multiple shots of a gunfight flow well together, shot counts might be ignored, rather than " \
            "breaking the flow by putting in a reload shot.\nThis is a common characteristic of Energy " \
            "Weapons; seldom do you see a ray gun run out of zap juice.\nAn adjunct to this would be " \
            "the Bottomless Quiver for archers. Many an archer in animation and videogames can pour out " \
            "a stream of arrows without ever hitting the supply cart.\nSee also Infinite Supplies, " \
            "Hammerspace. Unorthodox Reload is an aversion of this trope. Not at all related to Topless " \
            "Magazines.\nThis may end up becoming an Acceptable Break from Reality in many Video Games; " \
            "who wants to pull their fighter plane over to the side to top up on the 20mm ammo in the " \
            "middle of a Shoot 'em Up?\nEven in video games where you do have to reload, typically " \
            "shooters, the game doesn't keep track of individual magazines. You can reload at any point " \
            "without wasting bullets or having to move bullets from one magazine to another. When the " \
            "game invokes Universal Ammunition, the rules just get that much fuzzier. If you're " \
            "unlucky, though, some people's magazines might be more bottomless than others.\nA common " \
            "justification in science fiction stories is that future firearms actually fire extremely " \
            "tiny projectiles (hundreds or even thousands of which can be packed into a single " \
            "magazine). Since kinetic energy is a factor of both mass and velocity, firing mechanisms " \
            "that allow the projectile to be shot in a very, very high velocity can compensate (or " \
            "more) for the size of the bullet. Stronger characters sometimes have the 'cheats' of an " \
            "absurdly large magazine relative to their body size (e.g. having their gun belt-fed from a " \
            "backpack) or internal magazines whose capacity cannot be accurately calculated. Neither of " \
            "these can actually be bottomless, but since viewers can't tell the actual number of " \
            "rounds, they're less likely to have their Willing Suspension of Disbelief broken.\nThis " \
            "trope often goes hand-in-hand with More Dakka. Compare against Counting Bullets, which is " \
            "about limited magazines.\nThere's a separate \"Exceptions\" subsection on the bottom of " \
            "this page. Please post aversions and subversions there.\nNOTE: Clips are devices used to " \
            "help load cartridges into a magazine, such as the en-bloc clips used to help feed the M1 " \
            "rifle's fixed magazine or \"moon clips\" used hold multiple rounds in-place for loading " \
            "revolvers. It's a common and understandable mistake to mix clips and magazines up, " \
            "especially since most people already refer to magazines as clips in movies or video-games. " \
            "Regardless, it's a Berserk Button among many firearm enthusiasts.\n\nExamples"

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
