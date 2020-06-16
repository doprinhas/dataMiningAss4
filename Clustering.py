from sklearn.cluster import KMeans


def cluster_k_means(X, n_clusters, n_init):
    return KMeans(n_clusters=n_clusters, n_init=n_init).fit(X)