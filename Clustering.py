from sklearn.cluster import KMeans


def cluster_k_means(X, n_clusters, n_init):
    """ Clustering each record in X to one of n_cluster clusters by KMeans AI model """
    return KMeans(n_clusters=n_clusters, n_init=n_init).fit(X)