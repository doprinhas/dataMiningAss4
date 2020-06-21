import pandas as pd
from PreProcessing import pre_processing
import plotly.express as plex
import chart_studio.plotly as pltly
from Clustering import cluster_k_means
import matplotlib.pyplot as plt
import numpy as np


class ViewController:

    def __init__(self):
        self.proc_data = None

    def pre_process(self, path):
        self.data = pd.read_excel(path)
        if len(self.data.index) == 0:
            raise ValueError("The given data is empty")
        self.proc_data = pre_processing(self.data, group_by_col='country')
        self.proc_data = self.proc_data.drop(['year'], axis=1)
        self.path = path

    def cluster(self, n_clusters=8, n_init=10):
        self.k_means = cluster_k_means(self.proc_data.drop('country', axis=1), n_clusters, n_init)
        self.proc_data['cluster'] = self.k_means.labels_
        return self.get_graphs(self.k_means)

    def get_graphs(self, k_means):
        # First graph prep
        fig, ax = plt.subplots()
        sc = ax.scatter(self.proc_data['Social support'].values, self.proc_data['Generosity'].values, c=k_means.labels_.astype(np.float), edgecolor='k')
        fig.colorbar(sc, ax=ax)

        ax.set_xlabel('Social support', fontsize=12)
        ax.set_ylabel('Generosity', fontsize=12)
        fig.suptitle('K-Means clustering: Generosity - Social support', fontsize=12, fontweight='bold')
        dir_path = self.path[:self.path.rfind('/')]
        first_path = dir_path + '/Graph1.png'
        plt.savefig(first_path)
        plt.close(fig)

        # Second graph prep
        countries_data = pd.read_csv('countries_codes.csv')
        countries_dict = dict([(country, code) for country, code in
                               zip(countries_data['Country'].to_numpy(), countries_data['Alpha-3code'].to_numpy())])
        self.proc_data['country id'] = [countries_dict[x] if x in countries_dict else x for x in self.proc_data['country'].values]

        choro_map = plex.choropleth(self.proc_data, locations="country id", color="cluster",
                                  color_continuous_scale=plex.colors.sequential.Aggrnyl,
                                  title='K-Means clustering by countries')
        pltly.sign_in('sfreiman', 'tQTEO9EOznyYp5HEu5Or')
        second_path = dir_path + '/Graph2.png'
        pltly.image.save_as(choro_map, filename=second_path)
        return first_path, second_path

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def proc_data(self):
        return self.__proc_data

    @proc_data.setter
    def proc_data(self, proc_data):
        self.__proc_data = proc_data

    @property
    def k_means(self):
        return self.__k_means

    @k_means.setter
    def k_means(self, k_means):
        self.__k_means = k_means


# controller = ViewController()
# controller.pre_process('Dataset.xlsx')
# controller.cluster(2)
# data = controller.proc_data
# data = pd.read_excel('Dataset.xlsx')
# data = pre_processing(data, group_by_col='country')
# data = data.drop(['year'], axis=1)
#
# kmeans = cluster_k_means(data.drop('country', axis=1), 8, 10)
# data['cluster'] = kmeans.labels_
#
# print(data.shape)
# print(data)