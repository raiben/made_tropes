import json
import os
import sys
import textwrap
from string import Template


class TropeClassFactory(object):
    def __init__(self, tropes_url, template_url, target_directory):
        self.tropes_url = tropes_url
        self.template_url = template_url
        self.target_directory = target_directory
        if not self.target_directory.endswith("/"):
            self.target_directory += "/"

    def build_classes(self):
        with open(self.tropes_url) as tropes_file:
            tropes_as_json = "".join(tropes_file.readlines())
            tropes = json.loads(tropes_as_json)

        with open(self.template_url) as template_file:
            template_string = "".join(template_file.readlines())

        for trope_definition in tropes:
            path = "{path}{trope}.py".format(path=self.target_directory, trope=trope_definition["short_name"])
            print("Building file {}".format(path))

            with open(path, "w") as text_file:
                template = Template(template_string)
                film_name = [key for key in trope_definition["descriptions"].keys() if key != 'general'][0]

                content = template.substitute(
                    class_name=trope_definition["short_name"], short_name=trope_definition["short_name"],
                    categories=trope_definition["categories"], long_name=self.split_long_text(trope_definition["name"]),
                    url=trope_definition["web_page"], rdf_element=trope_definition["rdf_element"],
                    general_description=self.split_long_text(trope_definition["descriptions"]["general"]),
                    film_name=film_name,
                    description_in_film=self.split_long_text(trope_definition["descriptions"][film_name]))
                text_file.write(content)

            self.reformat_file(path)

    @staticmethod
    def split_long_text(long_text):
        line_length = 90
        safe_text = long_text.replace('"', '\"')
        lines = textwrap.wrap(safe_text, line_length, break_long_words=False)
        return ' " \\\n"'.join(lines)

    @staticmethod
    def reformat_file(path):
        os.system("autopep8 --in-place --aggressive {}".format(path))

if len(sys.argv) < 4:
    sys.stderr.write("Reads JSON input and build the classes\n"
                     "Usage: {executable} <film_json> <template_url> <target_directory>\n"
                     "Example: film_RaidersOfTheLostArk_tropes.json > {executable} ../".format(executable=sys.argv[0]))
    exit(1)

factory = TropeClassFactory(tropes_url=sys.argv[1], template_url=sys.argv[2], target_directory=sys.argv[3])
factory.build_classes()
