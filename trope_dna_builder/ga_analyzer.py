import csv
from unittest import TestCase

from scipy import stats


class Analyzer(object):
    def __init__(self, file_name):
        self.file_name = file_name
        csv_reader = None
        self.combinations = {}
        self.kolmogorov_smirnov_test = {}

        with open(file_name, 'r') as input_file:
            csv_reader = csv.DictReader(input_file, delimiter=',')

            for row in csv_reader:
                combination_key = ",".join([row["mutation"], row["crossover"], row["population"]])
                if combination_key not in self.combinations:
                    self.combinations[combination_key] = []
                self.combinations[combination_key].append(float(row["fitness"]))

        for combination in self.combinations:
            self.kolmogorov_smirnov_test[combination] = stats.kstest(self.combinations[combination], 'norm')

    def all_combinations_have_normal_distribution(self):
        return all(self.kolmogorov_smirnov_test[combination].pvalue <= 0.05
                   for combination in self.kolmogorov_smirnov_test)

    def get_run_matrix(self):
        text = ""
        combination_names = list(self.combinations.keys())
        text += ",".join([combination.replace(",","_") for combination in combination_names])
        text += "\n"

        run_size = len(self.combinations[combination_names[0]])
        for index in range(0,run_size):
            values = []
            for combination in combination_names:
                values.append(str(self.combinations[combination][index]))
            text += ",".join(values) + "\n"

        return text

class TestAnalyzer(TestCase):
    FILE_NAME = "/Users/phd/workspace/made/made_tropes/trope_dna_builder/data/genetic_tropes_execution_summary.csv"

    def test_analyzer_when_cvs_provided_then_kolgomorov_is_filled(self):
        analyzer = Analyzer(self.FILE_NAME)
        run_matrix = analyzer.get_run_matrix()

        self.assertTrue(analyzer.all_combinations_have_normal_distribution())
