from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from random import randint


class KMeans:
    def __init__(self, data: DataPoints):
        """
        Perform the k-means algorithm on given data of type `DataPoints`
        """
        self.data = data
        self.clustered_data = None

    def fit(self, k: int, max_iter: int):
        """Fit the model on a given k - number of clusters and max_iter - number of iterations
        returns the clustered data as `LabeledDataPoints`
        """
        # random initialization of centroids
        centroids = self._initialize_centroids(k)
        iterations = 0
        while iterations < max_iter:
            # assign points to centroids 
            assigned_points = self._assign_points_to_centroids(centroids, self.data)
            # calculate new centroids
            centroids = self._calculate_new_centroids(assigned_points)
            iterations += 1

        self.clustered_data = assigned_points

        return LabeledDataPoints(assigned_points)
    
    def _initialize_centroids(self, k: int) -> list:
        return [self.data[randint(0, len(self.data) - 1)] for _ in range(k)]
    
    def _assign_points_to_centroids(self, centroids: list, data: DataPoints) -> dict:
        assigned_points = {i: [] for i in range(len(centroids))}
        for point in data:
            # find the closest centroid one by one
            closest_centroid = self._find_closest_centroid(centroids, point)
            assigned_points[closest_centroid].append(point)
        return assigned_points
    
    def _find_closest_centroid(self, centroids: list, point: list) -> int:
        distances = []
        for centroid in centroids:
            distances.append(self._euclidean_distance(centroid, point))
        # return the index of the closest centroid
        return distances.index(min(distances))
    
    def _euclidean_distance(self, x: list, y: list) -> float:
        return sum([(x[i] - y[i])**2 for i in range(len(x))]) ** 0.5
    
    def _calculate_new_centroids(self, assigned_points: dict) -> list:
        new_centroids = []
        for key in assigned_points.keys():
            new_centroids.append(self._calculate_centroid(assigned_points[key]))
        return new_centroids
    
    def _calculate_centroid(self, points: list) -> list:
        # the mean value of points assigned to a centroid
        return [sum([point[i] for point in points]) / len(points) for i in range(len(points[0]))]
    
