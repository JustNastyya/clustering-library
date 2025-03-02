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

    def _predict_one(self, x: list):
        pass        
        