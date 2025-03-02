class KMeans:
    def __init__(self, k, max_iter=1000):
        self.k = k
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        for _ in range(self.max_iter):
            labels = np.argmin(np.linalg.norm(X[:, None] - self.centroids, axis=2), axis=1)
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids
        return self

    def predict(self, X):
        return np.argmin(np.linalg.norm(X[:, None] - self.centroids, axis=2), axis=1)