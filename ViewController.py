import pandas as pd
from PreProcessing import pre_processing
from Clustering import cluster_k_means


class ViewController:

    def __init__(self):
        pass

    def pre_process(self, path):
        self.data = pd.read_excel(path)
        self.proc_data = pre_processing(self.data, group_by_col='country')
        self.proc_data = self.proc_data.drop(['year'], axis=1)
        print('finish pre processing: ', self.proc_data)

    def cluster(self, n_clusters=8, n_init=10):
        self.k_means = cluster_k_means(self.proc_data.drop('country', axis=1), n_clusters, n_init)
        self.proc_data['cluster'] = self.k_means.labels_
        print('finish cluster: ', self.proc_data)

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