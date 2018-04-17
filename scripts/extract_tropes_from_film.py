import json
import re
import sys


class TropeEntity(object):
    def __init__(self, short_name, rdf_element, web_page):
        self.short_name = short_name
        self.rdf_element = rdf_element
        self.web_page = web_page
        self.name = ""
        self.descriptions = {}
        self.categories = []


class TvTropesRFDExtractor(object):
    FILM_URL_TEMPLATE = "<http://dbtropes.org/resource/Film/{}>"
    TROPE_URL_TEMPLATE = "<http://dbtropes.org/resource/Main/{}>"
    TROPE_WEB_URL_TEMPLATE = "http://tvtropes.org/pmwiki/pmwiki.php/Main/{}"
    CATEGORY_TEMPLATE = "^<http://dbtropes.org/resource/Main/{}> " \
                        "<http://dbtropes.org/ont/processingCategory[0-9]*> " \
                        "<http://dbtropes.org/resource/Main/([^>]*)>.*"
    DESCRIPTION_TEMPLATE = "^<http://dbtropes.org/resource/Main/{}> " \
                           "<http://www.w3.org/2000/01/rdf-schema#comment> \"(.*)\"[^\"]*$"
    LABEL_TEMPLATE = "^<http://dbtropes.org/resource/Main/{}> " \
                     "<http://www.w3.org/2000/01/rdf-schema#label> \"(.*)\"[^\"]*$"
    PROGRESS_TEMPLATE = "Progress: {:.2f}%, Lines: {:,}, Tropes: {}, Descriptions: {}, Implementations: {}, " \
                        "Full names: {}, Categories: {}       \r"
    LINES_TO_PRINT_LOG = 5000

    trope_dictionary = {}
    trope_names_found = []
    line_number = 0
    trope_descriptions = 0
    trope_implementations = 0
    trope_full_names = 0
    trope_categories = 0
    tropes = []

    trope_film_patterns = {}
    trope_general_patterns = {}
    trope_general_hierarchy = {}
    trope_full_name_patterns = {}

    def __init__(self, path_to_rdf, film_short_name):
        self.path_to_rdf = path_to_rdf
        self.film_short_name = film_short_name
        self.film_url = self.FILM_URL_TEMPLATE.format(self.film_short_name)
        self.film_pattern = re.compile("^{}.*".format(self.film_url))
        self.number_of_lines = 0

    def retrieve_tropes(self):
        self.reset_retrieved_info()
        self.get_number_of_lines()
        self.retrieve_trope_names_for_film()
        self.retrieve_trope_extra_info_for_film()

    def reset_retrieved_info(self):
        self.trope_names_found = []
        self.line_number = 0
        self.trope_descriptions = 0
        self.trope_implementations = 0
        self.trope_full_names = 0
        self.trope_categories = 0
        self.tropes = []

    def get_number_of_lines(self):
        self.number_of_lines = 0
        with open(self.path_to_rdf) as rdf_file:
            for line in rdf_file:
                self.number_of_lines += 1

    def retrieve_trope_names_for_film(self):
        sys.stderr.write("First loop: Detecting tropes for the film...\n")

        self.trope_names_found = []
        self.line_number = 0

        with open(self.path_to_rdf) as rdf_file:
            for line in rdf_file:
                self.line_number += 1
                self.search_film_in_line(line)
                self.print_percent()

    def search_film_in_line(self, line):
        matched = self.film_pattern.match(line)
        if matched:
            trope_finder_pattern = ".*<http://dbtropes.org/resource/Main/([^/]+/int_[^>]+).*>"
            trope_matched = re.match(trope_finder_pattern, line)
            if trope_matched:
                self.trope_names_found.append(trope_matched.group(1))

    def print_percent(self):
        if self.line_number % self.LINES_TO_PRINT_LOG == 0:
            percent = self.line_number * 100 / self.number_of_lines
            sys.stderr.write(self.PROGRESS_TEMPLATE.format(
                percent, self.line_number, len(self.trope_names_found), self.trope_descriptions,
                self.trope_implementations, self.trope_full_names, self.trope_categories))

    def retrieve_trope_extra_info_for_film(self):
        sys.stderr.write("\nSecond loop: Filling the information...\n")

        self.build_trope_dictionary()
        self.build_trope_patterns()

        self.line_number = 0

        with open(self.path_to_rdf) as rdf_file:
            for line in rdf_file:
                self.line_number += 1
                if line.startswith("<http://dbtropes.org/resource/Main/"):
                    for trope_instance in self.trope_names_found:
                        self.check_film_description_in_line(line, trope_instance)

                        self.check_general_description_in_line(line, trope_instance)

                        self.check_category_in_line(line, trope_instance)

                        self.check_full_name_in_line(line, trope_instance)

                self.print_percent()

        self.tropes = [trope.__dict__ for trope in self.trope_dictionary.values()]

    def check_film_description_in_line(self, line, trope_instance):
        if trope_instance in self.trope_film_patterns:
            matched = self.trope_film_patterns[trope_instance].match(line)
            if matched:
                text = matched.group(1)
                self.trope_dictionary[trope_instance].descriptions[self.film_short_name] = text
                self.trope_implementations += 1
                del self.trope_film_patterns[trope_instance]

    def check_general_description_in_line(self, line, trope_instance):
        if trope_instance in self.trope_general_patterns:
            matched = self.trope_general_patterns[trope_instance].match(line)
            if matched:
                text = matched.group(1)
                self.trope_dictionary[trope_instance].descriptions["general"] = text
                self.trope_descriptions += 1
                del self.trope_general_patterns[trope_instance]

    def check_category_in_line(self, line, trope_instance):
        if trope_instance in self.trope_general_hierarchy:
            matched = self.trope_general_hierarchy[trope_instance].match(line)
            if matched:
                text = matched.group(1)
                self.trope_dictionary[trope_instance].categories.append(text)
                self.trope_categories += 1
                del self.trope_general_hierarchy[trope_instance]

    def check_full_name_in_line(self, line, trope_instance):
        if trope_instance in self.trope_full_name_patterns:
            matched = self.trope_full_name_patterns[trope_instance].match(line)
            if matched:
                text = matched.group(1)
                self.trope_dictionary[trope_instance].name = text
                self.trope_full_names += 1
                del self.trope_full_name_patterns[trope_instance]

    def build_trope_dictionary(self):
        self.trope_dictionary = {}
        for trope_instance in self.trope_names_found:
            trope_name = trope_instance.split("/")[0]
            web_page = self.TROPE_WEB_URL_TEMPLATE.format(trope_name)
            self.trope_dictionary[trope_instance] = TropeEntity(short_name=trope_name, rdf_element=trope_instance,
                                                                web_page=web_page)

    def build_trope_patterns(self):
        self.trope_film_patterns = {}
        self.trope_general_patterns = {}
        self.trope_general_hierarchy = {}
        self.trope_full_name_patterns = {}

        for trope_instance in self.trope_names_found:
            trope_pattern = self.DESCRIPTION_TEMPLATE.format(trope_instance)
            self.trope_film_patterns[trope_instance] = re.compile(trope_pattern)

            trope_class = trope_instance.split("/")[0]
            trope_pattern = self.DESCRIPTION_TEMPLATE.format(trope_class)
            self.trope_general_patterns[trope_instance] = re.compile(trope_pattern)

            trope_pattern = self.CATEGORY_TEMPLATE.format(trope_class)
            self.trope_general_hierarchy[trope_instance] = re.compile(trope_pattern)

            trope_name_pattern = self.LABEL_TEMPLATE.format(trope_class)
            self.trope_full_name_patterns[trope_instance] = re.compile(trope_name_pattern)

    def print_json(self):
        sys.stderr.write("\nPrinting JSON in stdout...\n")
        sys.stdout.write(json.dumps(self.tropes, indent=2, sort_keys=True))


# main execution

if len(sys.argv) < 3:
    sys.stderr.write("Usage: {executable} <rdf_file_location> <short_name_of_the_film>\n"
                     "Example: {executable} ~/dbtropes/dbtropes-20160701.nt ANewHope".format(executable=sys.argv[0]))
    exit(1)

extractor = TvTropesRFDExtractor(path_to_rdf=sys.argv[1], film_short_name=sys.argv[2])
extractor.retrieve_tropes()
extractor.print_json()
