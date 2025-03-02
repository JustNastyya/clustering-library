from labeled_data_points import LabeledDataPoints
from data_points import DataPoints

class KNN:
    def __init__(self, data: LabeledDataPoints):
        self.data = data
        self.k = None
    
    def __init__(self, data: dict):
        self.data = LabeledDataPoints(data)
        self.k = None
    
    def fit(self, k: int): # TODO do i need it?
        self.k = k

    def predict(self, data_points: DataPoints) -> list:
        predictions = []
        for data_point in data_points:
            predictions.append(self._predict_one(data_point))
        return predictions

    def _euclidean_distance(self, x: list, y: list) -> float:
        return sum([(x[i] - y[i])**2 for i in range(len(x))]) ** 0.5

    def _predict_one(self, x: list):
        distances = []
        for label in self.data:
            for data_point in self.data[label]:
                distances.append((label, self._euclidean_distance(x, data_point)))
        distances.sort(key=lambda x: x[1])

        most_used_labeles = distances[:self.k]
        return max(set(most_used_labeles), key=most_used_labeles.count) # TODO check if it works
        