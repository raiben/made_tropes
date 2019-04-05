import logging
from collections import OrderedDict

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# see https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html

class PCATropes(object):
    META_COLUMN_NAME = ['Id', 'NameTvTropes', 'NameIMDB', 'Votes', 'Year']
    RATING_COLUMN_NAME = 'Rating'
    INDEX_FIRST_TROPE = len(META_COLUMN_NAME) + 1

    _logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%m',)

    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.column_types = OrderedDict()
        self.step = 1

    def run(self):
        self._read_csv_in_an_optimized_way()
        #self._build_clean_column_names()
        self._build_clean_column_names_good()
        #self._build_fit_scaled_transformation()
        #self._build_correlation_matrix()
        #self._build_correlation_matrix_good()
        self._build_covariance_matrix_good()
        self._build_eigen_things()
        pass

    def _read_csv_in_an_optimized_way(self):
        self._track_step(u'Reading first line and setting column types')
        with open(self.filename) as file:
            first_line = file.readline()

        columns = first_line.split(',')
        self.column_types = OrderedDict(Id=np.str, NameTvTropes=np.str, NameIMDB=np.str, Votes=np.str,
                                        Year=np.str, Rating=np.float16)

        for column in columns[self.INDEX_FIRST_TROPE]:
            self.column_types[column] = np.bool

        self._track_step(u'Reading CSV in an optimized way')
        self.data = pd.read_csv(self.filename, dtype=self.column_types)
        self.tropes_column_names = list(self.data.columns[self.INDEX_FIRST_TROPE:])

    def _build_clean_column_names(self):
        self._track_step(u'Scaling tropes... is it necessary?')

        X = self.data.loc[:, self.tropes_column_names].values
        y = self.data.loc[:, self.RATING_COLUMN_NAME].values
        X_std = StandardScaler().fit_transform(X)

        constant_rows = []
        for index, row in enumerate(X_std.T):
            if len(set(row)) <= 1:
                constant_rows.append(index)
        print('Constant rows ({}): {}'.format(len(constant_rows), constant_rows))

        # get columns for tropes in the constant rows
        columns = list(self.data.columns)
        problematic_trope_names = [
            columns[self.INDEX_FIRST_TROPE + index] for index in constant_rows
        ]
        print('Problematic tropes ({}): {}'.format(
            len(problematic_trope_names), problematic_trope_names))

        self.clean_column_names = []
        for trope_column_name in self.tropes_column_names:
            if trope_column_name not in problematic_trope_names:
                self.clean_column_names.append(trope_column_name)

    def _build_clean_column_names_good(self):
        self._track_step(u'Building list of useful columns')

        X = self.data.loc[:, self.tropes_column_names].values

        constant_rows = []
        for index, row in enumerate(X.T):
            if len(set(row)) <= 1:
                constant_rows.append(index)
        self._logger.info('Constant rows ({}): {}'.format(len(constant_rows), constant_rows))

        columns = list(self.data.columns)
        problematic_trope_names = [
            columns[self.INDEX_FIRST_TROPE + index] for index in constant_rows
        ]
        self._logger.info('Problematic tropes ({}): {}'.format(len(problematic_trope_names), problematic_trope_names))

        self.clean_column_names = []
        for trope_column_name in self.tropes_column_names:
            if trope_column_name not in problematic_trope_names:
                self.clean_column_names.append(trope_column_name)

    def _build_fit_scaled_transformation(self):
        X = self.data.loc[:, self.clean_column_names].values
        y = self.data.loc[:, self.RATING_COLUMN_NAME].values
        from sklearn.preprocessing import StandardScaler
        self.X_std = StandardScaler().fit_transform(X)
        print(self.X_std.T)

    def _build_correlation_matrix(self):
        # cor_mat1 = np.corrcoef(ma.masked_invalid(X_std.T))
        self.cor_mat1 = np.corrcoef(self.X_std.T)
        print('NumPy correlation matrix: \n{}'.format(self.cor_mat1))
        print('has NaN? {}'.format(np.isnan(self.cor_mat1).any()))
        print('has inf? {}'.format(np.isinf(self.cor_mat1).any()))

    def _build_correlation_matrix_good(self):
        self._track_step(u'Building correlation matrix')

        X = self.data.loc[:, self.clean_column_names].values
        self.cor_mat1 = np.corrcoef(X, rowvar=0)
        print('NumPy correlation matrix: \n{}'.format(self.cor_mat1))
        print('has NaN? {}'.format(np.isnan(self.cor_mat1).any()))
        print('has inf? {}'.format(np.isinf(self.cor_mat1).any()))

    def _build_covariance_matrix_good(self):
        self._track_step(u'Building covariance matrix')

        X = self.data.loc[:, self.clean_column_names].values
        self.covariance_matrix = np.cov(X, rowvar=False)
        self._logger.info('Covariance matrix: \n{}'.format(self.covariance_matrix))

    def _build_eigen_things(self):
        self._track_step(u'Building eigen values and eigen vectors')

        self.eig_vals, self.eig_vecs = np.linalg.eig(self.covariance_matrix)
        print('Eigenvectors \n%s' % self.eig_vecs)
        print('\nEigenvalues \n%s' % self.eig_vals)

    def _track_step(self, message):
        self._logger.info(u'Step {}.- {}'.format(self.step,message))
        self.step+=1

if __name__ == "__main__":
    file_name = u'/Users/phd/workspace/made/made_tropes/scripts/data/film_extended_information_unique_values.csv'
    pca_tropes = PCATropes(file_name)
    pca_tropes.run()


class PCATropes2(object):
    META_COLUMN_NAME = ['Id', 'NameTvTropes', 'NameIMDB', 'Votes', 'Year']
    RATING_COLUMN_NAME = 'Rating'
    INDEX_FIRST_TROPE = len(META_COLUMN_NAME) + 1

    _logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%m', )

    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.column_types = OrderedDict()
        self.step = 1

    def run(self):
        self._read_csv_in_an_optimized_way()
        self.lo_demas()

    def _read_csv_in_an_optimized_way(self):
        self._track_step(u'Reading first line and setting column types')
        with open(self.filename) as file:
            first_line = file.readline()

        columns = first_line.split(',')
        self.column_types = OrderedDict(Id=np.str, NameTvTropes=np.str, NameIMDB=np.str, Votes=np.str,
                                        Year=np.str, Rating=np.float16)

        for column in columns[self.INDEX_FIRST_TROPE]:
            self.column_types[column] = np.bool

        self._track_step(u'Reading CSV in an optimized way')
        self.data = pd.read_csv(self.filename, dtype=self.column_types)
        self.tropes_column_names = list(self.data.columns[self.INDEX_FIRST_TROPE:])

    def lo_demas(self):
        # normalizamos los datos
        scaler = StandardScaler()

        df = self.data.drop(self.META_COLUMN_NAME + [self.RATING_COLUMN_NAME], axis=1)

        scaler.fit(df)  # calculo la media para poder hacer la transformacion
        X_scaled = scaler.transform(df)  # Ahora si, escalo los datos y los normalizo

        # Instanciamos objeto PCA y aplicamos
        pca = PCA(0.9)  # Otra opción es instanciar pca sólo con dimensiones nuevas hasta obtener un mínimo "explicado" ej.: pca=PCA(.85)
        pca.fit(X_scaled)  # obtener los componentes principales
        X_pca = pca.transform(X_scaled)  # convertimos nuestros datos con las nuevas dimensiones de PCA

        print("shape of X_pca", X_pca.shape)
        expl = pca.explained_variance_ratio_
        print(expl)
        print('suma:', sum(expl[0:5]))
        # Vemos que con 5 componentes tenemos algo mas del 85% de varianza explicada

        # graficamos el acumulado de varianza explicada en las nuevas dimensiones
        plt.plot(np.cumsum(pca.explained_variance_ratio_))
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')
        plt.show()

        pass

    def _track_step(self, message):
        self._logger.info(u'Step {}.- {}'.format(self.step,message))
        self.step+=1

if __name__ == "__main__":
    file_name = u'/Users/phd/workspace/made/made_tropes/scripts/data/film_extended_information_unique_values.csv'
    pca_tropes = PCATropes2(file_name)
    pca_tropes.run()