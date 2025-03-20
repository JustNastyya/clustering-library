from basic_data_structures.labeled_data_points import LabeledDataPoints
from basic_data_structures.data_points import DataPoints

class KNN:
    def __init__(self, data: LabeledDataPoints):
        if type(data).__name__ != "LabeledDataPoints":
            data = LabeledDataPoints(data)
        self.data = data
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

    def _get_most_frequent_value(self, x: list):
        frequency = {}
        for num in x:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        max_freq = 0
        most_common_numbers = 0

        for num, freq in frequency.items():
            if freq > max_freq:
                max_freq = freq
                most_common_numbers = num

        return most_common_numbers

    def _predict_one(self, x: list):
        distances = []
        for label in self.data:
            for data_point in self.data[label]:
                distances.append([label, self._euclidean_distance(x, data_point)]) # TODO andere distanzen?
        distances.sort(key=lambda x: x[1])
        print(distances)

        most_used_labeles = distances[:self.k]
        most_used_labels = [label for label, _ in most_used_labeles]
        return self._get_most_frequent_value(most_used_labels)
    