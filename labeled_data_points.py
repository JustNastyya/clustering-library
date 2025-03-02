from data_points import DataPoints

class LabeledDataPoints:
    # init LabeledDataPoints
    # data is either a dictionary of DataPoints or a dictionary of lists
    # where each list represents a data point (float)
    # data = {label1: [p1, p2, p3, ..., pn], label2: [p1, p2, p3, ..., pn], ...}
    # where p1 = [x1, x2, x3, ..., xk]
    # and len(p1) = len(p2) = len(p3) = ... = len(pn)
    def __init__(self, data: dict):
        if len(data) != 0 and type(data[0]) == DataPoints:
            self.data = data
        elif len(data) != 0 and type(data[0]) == list:
            self.data = {
                key: DataPoints(data[key])
                for key in data.keys()
            }
        else: # TODO add pandas?
            raise ValueError("data must be a dictionary of DataPoints or a dictionary of lists")
        
    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return iter(self.data)