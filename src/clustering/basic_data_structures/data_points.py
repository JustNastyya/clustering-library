class DataPoints:
    def __init__(self, data: list, reverse=False):
        """init takes a list of lists
        where each list represents a data point (float)
        data = [p1, p2, p3, ..., pn]
        where p1 = [x1, x2, x3, ..., xk]
        and len(p1) = len(p2) = len(p3) = ... = len(pn)
        can also be initialized as a list of variables. to do
        so use: reverse=True
        """
        self.data = data
        if reverse:
            self.transformate()
        self._evaluate_data_points(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]
    
    def transformate(self):
        """perform a matrix transformation on your data"""
        self.data = [
            [self.data[j][i] for j in range(len(self.data))]
            for i in range(len(self.data[0]))
        ]

    def __iter__(self):
        return iter(self.data)

    def _evaluate_data_points(self, data_points: list):
        for data_point in data_points:
            if len(data_point) != len(data_points[0]):
                raise ValueError("data points must have the same length")
            if not(all(isinstance(x, (int, float)) for x in data_point)):
                raise ValueError("data points must be of type int or float")
        return True