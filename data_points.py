class DataPoints:
    # init takes a list of lists
    # where each list represents a data point (float)
    # data = [p1, p2, p3, ..., pn]
    # where p1 = [x1, x2, x3, ..., xk]
    # and len(p1) = len(p2) = len(p3) = ... = len(pn)
    def __init__(self, data: list):
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)