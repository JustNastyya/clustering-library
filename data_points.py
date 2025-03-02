class DataPoints:
    # init takes a list of lists
    # where each list represents a data point (float)
    # data = [p1, p2, p3, ..., pn]
    # where p1 = [x1, x2, x3, ..., xk]
    # and len(p1) = len(p2) = len(p3) = ... = len(pn)
    def __init__(self, data: list):
        self._evaluate_data_points(data)
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def _evaluate_data_points(self, data_points: list):
        for data_point in data_points:
            if len(data_point) != len(data_points[0]):
                raise ValueError("data points must have the same length")
            if not(all(isinstance(x, (int, float)) for x in data_point)):
                raise ValueError("data points must be of type int or float")
        return True