import logging
from collections import OrderedDict
from random import Random

import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_regression
from sklearn.externals import joblib

# see https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e
# see https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html

class FeatureSelectionTropes(object):
    META_COLUMN_NAME = ['Id', 'NameTvTropes', 'NameIMDB', 'Votes', 'Year']
    RATING_COLUMN_NAME = 'Rating'
    INDEX_FIRST_TROPE = len(META_COLUMN_NAME) + 1

    _logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%m', )

    def __init__(self, filename, number_of_features, seed=0):
        self.filename = filename
        self.all_data = None
        self.training_data = None
        self.testing_data = None
        self.random = Random()
        self.random.seed(seed)
        self.number_of_features = number_of_features
        self.featureScores = None

    def run(self):
        self._track_step(u'Running...')
        self._read_csv_in_an_optimized_way()
        self._select_features()
        self._store_selected_features()
        pass


    def _read_csv_in_an_optimized_way(self):
        self._track_step(u'Reading first line and setting column types')
        with open(self.filename) as file:
            first_line = file.readline()

        columns = first_line.split(',')
        column_types = OrderedDict(Id=np.str, NameTvTropes=np.str, NameIMDB=np.str, Votes=np.str,
                                   Year=np.str, Rating=np.float128)

        for column in columns[self.INDEX_FIRST_TROPE]:
            column_types[column] = np.bool

        self._track_step(u'Reading CSV in an optimized way')
        self.all_data = pd.read_csv(self.filename, dtype=column_types)
        self.tropes_column_names = list(self.all_data.columns[self.INDEX_FIRST_TROPE:])
        self._track_step('Data shape {}'.format(self.all_data.shape))

        self._track_step('Cleaning up rows with NaN rating')
        self.all_data = self.all_data[np.isfinite(self.all_data[self.RATING_COLUMN_NAME])]
        self._track_step('New data shape {}'.format(self.all_data.shape))

        self.number_of_rows = self.all_data.shape[0]

    def _track_step(self, message):
        try:
            self.counter += 1
        except AttributeError:
            self.counter = 1

        self._logger.info(u'Step {}.- {}'.format(self.counter, message))

    def _select_features(self):
        self._track_step('SelectKBest class to extract top best features')
        X = self.all_data.loc[:, self.tropes_column_names]  # independent columns
        y = self.all_data.loc[:, self.RATING_COLUMN_NAME]  # target column i.e price range
        bestfeatures = SelectKBest(score_func=mutual_info_regression, k=10)
        fit = bestfeatures.fit(X, y)

        self._track_step('Building dataframe from results')
        dfscores = pd.DataFrame(fit.scores_)
        dfcolumns = pd.DataFrame(X.columns)

        self._track_step('Concatenating two dataframes for better visualization')
        self.featureScores = pd.concat([dfcolumns, dfscores], axis=1)
        self.featureScores.columns = ['Specs', 'Score']  # naming the dataframe columns

    def _store_selected_features(self):
        self._track_step('Storing selected features')
        print(self.featureScores.nlargest(self.number_of_features, 'Score'))  # print 10 best features
        joblib.dump(self.featureScores, 'featureScores.pkl', compress=3)
        self.featureScores.to_csv('featureScores.csv')
        pass


if __name__ == "__main__":
    file_name = u'/Users/phd/workspace/made/made_tropes/scripts/data/film_extended_information_unique_values.csv'
    pca_tropes = FeatureSelectionTropes(file_name, 500)
    pca_tropes.run()
