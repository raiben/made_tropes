import logging
from collections import OrderedDict

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# see https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales
# see https://www.pybonacci.org/2012/10/08/analisis-de-componentes-principales-con-python/
# see https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html
# see http://www.aprendemachinelearning.com/comprende-principal-component-analysis/
# see https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
# see https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/

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

        # Result
        # shape of X_pca (5639, 3120)
        # plt.savefig('cumulative_explained_variance.png')
        # see cumulative_explained_variance.png

    def _track_step(self, message):
        self._logger.info(u'Step {}.- {}'.format(self.step,message))
        self.step+=1

if __name__ == "__main__":
    file_name = u'/Users/phd/workspace/made/made_tropes/scripts/data/film_extended_information_unique_values.csv'
    pca_tropes = PCATropes2(file_name)
    pca_tropes.run()