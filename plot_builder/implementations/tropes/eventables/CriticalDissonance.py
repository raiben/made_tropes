from plot_builder.entities.event_entity import EventEntity
from plot_builder.interfaces.trope_definition_interface import TropeDefinitionInterface


class CriticalDissonanceTrope(TropeDefinitionInterface):
    def get_short_name(self):
        return "CriticalDissonance"

    def get_long_name(self):
        return "Critical Dissonance"

    def get_type(self):
        return ""

    def get_info(self):
        return "http://tvtropes.org/pmwiki/pmwiki.php/Main/CriticalDissonance"

    def get_rdf_element(self):
        return "CriticalDissonance/int_691166df"

    def get_description_for_film(self):
        return {"DieHardWithAVengeance":
                "Die Hard with a Vengeance was somewhat divisive to critics (though its reputation has "
                "improved since then), but was still the highest-grossing film of 1995 and well-received by "
                "fans."}

    def get_categories(self):
        return ['AudienceReactions']

    def get_general_description(self):
        return "Critical Dissonance is polar opposition of public to critical opinion. Critics might love " \
            "a certain work while general audiences shun it, or vice versa.\nCritics may look down on a " \
            "popular work on principle, denouncing it as Lowest Common Denominator garbage that\u2019s " \
            "all flash and no substance. Conversely, the public may see a work beloved by the critics " \
            "as boring, angsty and pretentious drivel engineered solely to win awards from equally " \
            "boring, angsty and pretentious Academy members.\nSometimes later opinions can match, and " \
            "then we have Vindicated by History (or Deader Than Disco, as the case may be), but not " \
            "always.\nSome media are less affected by this than others. Since comedy relies on what an " \
            "individual finds funny, this is the genre of movie most likely to spur on Critical " \
            "Dissonance. One critic may find a movie hilarious while another finds it tacky. Switch out " \
            "comedy for the horror genre and you get the same polarizing results. Art \u2014 all kinds, " \
            "not just abstract \u2014 is notoriously subject to this. And architects get hit with it " \
            "all the time.\nIn general, this trope has historically been uncommon with video games, " \
            "partly due to the far greater reliance on reviews among gamers, and partly because the " \
            "technical side (gameplay, graphics, etc.) tends to carry more weight with games than with " \
            "books or TV. Additionally, good gameplay (at least in terms of, say, lacking glitches) is " \
            "much more black-and-white than a good story, writing, or acting. However, video-game " \
            "journalism is infamous for its frightening degree of corruption, to the point where " \
            "reviewers who don\u2019t sufficiently praise games that buy enough advertising space on " \
            "their stomping grounds tend to get fired pretty quickly. When Critical Dissonance does " \
            "occur with games, it is more often than not because gamers thought that the critics had " \
            "been overly kind (like the Four Point Scale), or had even been paid upfront by the " \
            "publishers as part of an advertising and/or first-look article special.\nNiche media may " \
            "particularly suffer this because some or all of the critics assigned to review it " \
            "aren\u2019t members of its target demographic, or don\u2019t even have a basic knowledge " \
            "of the genre. To look at it another way, if the business model involves an audience who " \
            "will actively seek it out, those people will be predisposed to enjoy it, whereas critics " \
            "who see it out of professional necessity will not have that selection bias.\nTelltale " \
            "signs of Critical Dissonance include disagreement between a work\u2019s revenue and its " \
            "reviews, simultaneous nominations for both \u2018best X\u2019 and \u2018worst Y\u2019 " \
            "awards (bonus points if X=Y), and angry comments on those review sites that have " \
            "them.\nThat the main differences between the average audience viewer and the average " \
            "critic are vocabulary, sometimes ego, and employment in the field of journalism is what " \
            "makes the large contrast between viewpoints either fascinating or predictable, depending " \
            "on your degree of cynicism.\nSee also Critical Backlash, Critic-Proof, Bias Steamroller, " \
            "It's Popular, Now It Sucks, Opinion Myopia, 8.8 and Oscar Bait. Could overlap with Pop- " \
            "Culture Isolation and Acclaimed Flop. Contrast with Cult Classic where a work tends to " \
            "have neither critical acclaim nor general popularity, but is enjoyed by a few diehard " \
            "fans. Possibly the cause of Mainstream Obscurity.\n\nExamples"

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
