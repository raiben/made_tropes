import json
import re
import sys
from functools import reduce
from graphviz import Digraph


class CategoriesTree(dict):
    def add_category(self, parent, child):
        if parent not in self.keys():
            self[parent] = []
        self[parent].append(child)

    def children(self):
        return reduce(lambda x, y: x + y, self.values())

    def roots(self):
        return self.keys() - set(self.children())

    def get_tree_dictionary(self, element=None, parents=None):
        if element is None:
            roots = self.roots()
            children = []
            for root in roots:
                children.append(self.get_tree_dictionary(root, []))
            return {"tropes": children}

        url = "/".join([parent[0:1] for parent in parents]+[element])
        sys.stderr.write("Path: {}, level {}                    \r".format(url, len(parents)))
        if element in parents:
            return "{} (cycle)".format(element)

        if element is not None:
            if element in self:
                children = []
                for child in self[element]:
                    children.append(self.get_tree_dictionary(child, parents + [element]))
                return {element: children}
            else:
                return element

    def render_graph(self):
        dot = Digraph(comment='The Round Table')
        dot.node('A', 'King Arthur')
        nodes = set(self.keys()+self.children())
        for node in nodes:
            dot.node(node, node)

        for parent in self.keys():
            for child in self[parent]:
                print("{}->{}".format(parent, child))
                dot.edge(parent, child)

        dot.format = 'svg'
        dot.render("categories.svg")


class CategoriesRFDExtractor(object):
    LINES_TO_PRINT_LOG = 5000
    CATEGORY_SUBSTRING = "<http://dbtropes.org/ont/processingCategory"
    CATEGORY_TEMPLATE = "^<http://dbtropes.org/resource/Main/([^>]*)> " \
                        "<http://dbtropes.org/ont/processingCategory[0-9]*> " \
                        "<http://dbtropes.org/resource/Main/([^>]*)>.*$"
    PROGRESS_TEMPLATE = "Progress: {} Lines\r"

    def __init__(self, path_to_rdf):
        self.path_to_rdf = path_to_rdf
        self.line_number = 0
        self.category_pattern = None
        self.categories_tree = CategoriesTree()

    def extract_categories(self):
        self.line_number = 0
        self.category_pattern = re.compile(self.CATEGORY_TEMPLATE)
        self.categories_tree = CategoriesTree()

        with open(self.path_to_rdf) as rdf_file:
            for line in rdf_file:
                self.line_number += 1
                if self.CATEGORY_SUBSTRING in line:
                    matched = self.category_pattern.match(line)
                    if matched:
                        child = matched.group(1)
                        parent = matched.group(2)
                        self.categories_tree.add_category(parent, child)
                    else:
                        # sys.stderr.write("\nFound line that didn't match: {}\n".format(line))
                        pass
                self.print_percent()

    def print_percent(self):
        if self.line_number % self.LINES_TO_PRINT_LOG == 0:
            sys.stderr.write(self.PROGRESS_TEMPLATE.format(self.line_number))

    def print_json(self):
        #sys.stderr.write("\nPrinting JSON in stdout...\n")
        #sys.stdout.write(json.dumps(self.categories_tree, indent=2, sort_keys=True))
        #sys.stderr.write("\nPrinting JSON in stdout...\n")
        #sys.stdout.write(json.dumps(self.categories_tree.get_tree_dictionary(), indent=2, sort_keys=True))
        self.categories_tree.render_graph()


# main execution

if len(sys.argv) < 2:
    sys.stderr.write("Usage: {executable} <rdf_file_location>\n"
                     "Example: {executable} ~/dbtropes/dbtropes-20160701.nt".format(executable=sys.argv[0]))
    exit(1)

extractor = CategoriesRFDExtractor(path_to_rdf=sys.argv[1])
extractor.extract_categories()
extractor.print_json()
