from clustering.basic_data_structures.data_points import DataPoints

class LabeledDataPoints:
    def __init__(self, data, labels=None):
        """ init LabeledDataPoints
        data is either a dictionary of DataPoints or a dictionary of lists or 
        a list of lists and a third list of class labeles
        where each list represents a data point (float)
        data = {label1: [p1, p2, p3, ..., pn], label2: [p1, p2, p3, ..., pn], ...}
        where p1 = [x1, x2, x3, ..., xk]
        and len(p1) = len(p2) = len(p3) = ... = len(pn)"
        """
        
        if type(data) == dict:
            self._init_dict(data)
        elif type(data) == DataPoints or type(data) == list:
            if labels is None:
                raise ValueError("labels must be provided")
            self._init_datapoints(data, labels)
        else:
            raise ValueError("data must be a dictionary of DataPoints or a dictionary of lists")

    def _init_dict(self, data):
        if len(data) == 0:
            raise ValueError("data must be a non-empty dictionary of DataPoints")
        
        self.data = data
        self._evaluate_labeled_data_points(data)
    
    def _init_datapoints(self, data: DataPoints, labels: list):
        # reforming the data if it is not a dict or not a dict of DataPoints yet
        if type(data).__name__ == "list": # assuming data is a [x, y] list
            data = DataPoints(data)
            data.transformate()
        if len(data) != len(labels):
            raise ValueError("data and labels must have the same length")
        self.data = {
            label: DataPoints([data[j] for j in range(len(data)) if labels[j] == label])
            for label in set(labels)
        }
        self._evaluate_labeled_data_points(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return iter(self.data)

    def _evaluate_labeled_data_points(self, data: dict):
        # evaluating the data for dictionaries
        for key in data.keys():
            if not(isinstance(key, (int, float, str))):
                raise ValueError("keys types must be either int, float or str")
            if not isinstance(data[key], DataPoints):
                data[key] = DataPoints(data[key])
        return True