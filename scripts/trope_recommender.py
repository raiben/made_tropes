import re
import sys

from __builtin__ import raw_input


class Recommender():
    RULE_TEMPLATE = "^Rule: \\(([^\)]+)\\) ==> \\(([^\)]+)\\) , ([0-9.]*)$"

    def __init__(self, path_to_rules):
        self.path_to_rules = path_to_rules
        self.rule_pattern = re.compile(self.RULE_TEMPLATE)
        self.rules_tropes = {}
        self.rules_confidence = {}
        self.sorted_tropes = []
        self.line_number = 0

    def retrieve_info(self):
        print("Processing file...")
        self.line_number = 0
        with open(self.path_to_rules) as file:
            for line in file:
                self._process_line(line)
        self.sorted_tropes = sorted(list(set(self.sorted_tropes)))
        if self.sorted_tropes[0] == "":
            del self.sorted_tropes[0]

    def _process_line(self, line):
        self.line_number += 1
        if self.line_number % 10 == 0:
            sys.stdout.write("\rLine: {}".format(self.line_number))
        matches = self.rule_pattern.match(line)
        if matches:
            antecedent = matches.group(1)
            consequent = matches.group(2)
            confidence = matches.group(3)

            self.register_antecendent_and_consequent(antecedent, consequent)
            self.register_confidence(antecedent, confidence, consequent)
            self.update_sorted_tropes(antecedent, consequent)

    def register_antecendent_and_consequent(self, antecedent, consequent):
        if not antecedent in self.rules_tropes:
            self.rules_tropes[antecedent] = []
        self.rules_tropes[antecedent].append(consequent)

    def register_confidence(self, antecedent, confidence, consequent):
        rules_confidence_key = self.build_rules_confidence_key(consequent, antecedent)
        self.rules_confidence[rules_confidence_key] = float(confidence)

    def update_sorted_tropes(self, antecedent, consequent):
        tropes = [trope.strip() for trope in
                  antecedent.replace("'", "").split(",") + consequent.replace("'", "").split(",")]
        self.sorted_tropes = self.sorted_tropes + tropes

    def get_recommendations(self, list_of_elements):
        recommendations_to_modify = {}
        for key in self.rules_tropes.keys():
            self.process_rule(key, list_of_elements, recommendations_to_modify)

        self.delete_empty_key_from_dictionary(recommendations_to_modify)
        self.delete_current_tropes_from_recommendations(list_of_elements, recommendations_to_modify)

        return recommendations_to_modify

    @staticmethod
    def delete_empty_key_from_dictionary(recommendations_to_modify):
        if "" in recommendations_to_modify:
            del (recommendations_to_modify[""])

    @staticmethod
    def delete_current_tropes_from_recommendations(list_of_elements, recommendations_to_modify):
        for original_trope in list_of_elements:
            if original_trope in recommendations_to_modify:
                del (recommendations_to_modify[original_trope])

    def process_rule(self, key, list_of_elements, recommendations):
        tropes_in_key = [trope.strip() for trope in key.replace("'", "").split(",")]
        if "" in tropes_in_key:
            del (tropes_in_key[tropes_in_key.index("")])

        if self.is_sublist(superlist=list_of_elements, sublist=tropes_in_key):
            consequents = self.rules_tropes[key]
            for consequent in consequents:
                tropes_to_recommend = [trope.strip() for trope in consequent.replace("'", "").split(",")]
                for trope_to_recommend in tropes_to_recommend:
                    if self.should_update_trope_in_recommendation(recommendations, trope_to_recommend):
                        confidence = self.rules_confidence[self.build_rules_confidence_key(consequent, key)]
                        recommendations[trope_to_recommend] = confidence

    def should_update_trope_in_recommendation(self, recommendations, trope_to_recommend):
        return trope_to_recommend not in recommendations or recommendations[trope_to_recommend] < \
                                                            recommendations[trope_to_recommend]

    def build_rules_confidence_key(self, consequent, key):
        return "{}->{}".format(key, consequent)

    def is_sublist(self, superlist, sublist):
        for element in sublist:
            if element not in superlist:
                return False
        return True


class UserInterface():
    def __init__(self, recommender):
        self.recommender = recommender
        self.current_list_of_tropes = []
        self.input = ""
        self.loop = False

    def print_list_of_tropes(self):
        longest_length = max([len(trope) for trope in self.recommender.sorted_tropes])
        tropes_with_indexes = [
            '{{index}}: {{trope: <{fill}}}'.format(fill=longest_length).format(index=index, trope=trope)
            for index, trope in enumerate(recommender.sorted_tropes)]
        columns = ["\t".join(trope_set) for trope_set in self.chunks(tropes_with_indexes, 4)]
        print("List of tropes:\n{}".format("\n".join(columns)))

    def chunks(self, l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i + n]

    def start_loop(self):
        self.loop = True
        while (self.loop):
            self.print_list_of_tropes()
            self.print_current_tropes()
            self.print_alternatives()
            self.process_input()

    def print_current_tropes(self):
        print("\nYour current tropes are:\n\x1b[34m{}\x1b[0m".format(self.current_list_of_tropes))

    def print_alternatives(self):
        print("\nYou might be interested in adding:")
        recommendations = self.recommender.get_recommendations(self.current_list_of_tropes)
        recommendations_keys_in_order_of_confidence = sorted(recommendations.keys(), key=lambda x: recommendations[x],
                                                             reverse=True)

        lines = [self.build_line_for_confidence(recommendations, trope)
                 for trope in recommendations_keys_in_order_of_confidence]
        for line in lines:
            print(line)

    def build_line_for_confidence(self, recommendations, trope):
        return "- {}: {} - confidence: \x1b[32m{}\x1b[0m".format(self.recommender.sorted_tropes.index(trope),
                                                                 trope, recommendations[trope])

    def process_input(self):
        self.input = raw_input("\nPlease write the index of the trope to add. Type 'exit' to quit > ")
        self.input = self.input.strip()
        print('You wrote {}'.format(self.input))
        if self.input == "":
            print("Empty input, please try again")
            return self.process_input()

        if self.input == "exit":
            self.loop = False
            return

        try:
            number = int(self.input)
            trope = self.recommender.sorted_tropes[number]
            if trope not in self.current_list_of_tropes:
                self.current_list_of_tropes.append(trope)
        except Exception as exception:
            print(exception)
            return self.process_input()


if len(sys.argv) < 2:
    sys.stderr.write("Usage: {executable} <rules_text_file>\n"
                     "Example: {executable} ~/data/apriori_rules_0.005_0.05.txt".format(executable=sys.argv[0]))
    exit(1)

recommender = Recommender(path_to_rules=sys.argv[1])
recommender.retrieve_info()

user_interface = UserInterface(recommender)
user_interface.start_loop()
