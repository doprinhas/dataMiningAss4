from sklearn.cluster import KMeans


def cluster_k_means(data, n_clusters, n_init):
    """ Clustering each record in data to one of n_cluster clusters by KMeans AI model """
    return KMeans(n_clusters=n_clusters, n_init=n_init).fit(data)