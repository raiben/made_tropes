import json
import re

import sys


class TropeDictionary(object):
    def __init__(self):
        self.trope_dictionary = {}

    def link_film_and_trope(self, film, trope):
        if film not in self.trope_dictionary:
            self.trope_dictionary[film] = []
        self.trope_dictionary[film].append(trope)

    def as_printable_version(self):
        return json.dumps(self.trope_dictionary, sort_keys=True, indent=2)

    def as_a_priori_transactions(self):
        string_to_return = ""
        for key, value in self.trope_dictionary.iteritems():
            sorted_list_of_tropes = sorted(value)
            string_to_return += ",".join(sorted_list_of_tropes)+"\n"
        return string_to_return



class FilmsWithTropesInFile():
    PATTERN = '<http://dbtropes.org/resource/Film/([^/]+)/int_[^>]*>.*<http://dbtropes.org/resource/Main/([^>]*)>'

    def __init__(self, path_to_rdf):
        self.path_to_rdf = path_to_rdf
        self.pattern = re.compile(self.PATTERN)
        self.trope_dictionary = TropeDictionary()

    def extract(self):
        TropeDictionary
        with open(self.path_to_rdf) as rdf_file:
            self.process_line(rdf_file)

    def process_line(self, rdf_file):
        for line in rdf_file:
            matches = self.pattern.match(line)
            if matches:
                film = matches.group(1)
                trope = matches.group(2)
                sys.stderr.write("\r{}                                                     ".format(film))
                self.trope_dictionary.link_film_and_trope(film, trope)

    def as_printable_version(self):
        return self.trope_dictionary.as_printable_version()

    def as_a_priori_transactions(self):
        return self.trope_dictionary.as_a_priori_transactions()

# main execution

if len(sys.argv) < 2:
    sys.stderr.write("Usage: {executable} <rdf_file_location>\n"
                     "Example: {executable} ~/dbtropes/dbtropes-20160701.nt".format(executable=sys.argv[0]))
    exit(1)

films_and_tropes = FilmsWithTropesInFile(path_to_rdf=sys.argv[1])
films_and_tropes.extract()
print(films_and_tropes.as_a_priori_transactions())

