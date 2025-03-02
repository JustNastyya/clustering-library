from basic_data_structures.data_points import DataPoints
from basic_data_structures.labeled_data_points import LabeledDataPoints


class UnsupervisedClusterer:
    def __init__(self, data: DataPoints):
        self.data = data
    
    # method = "single linkage", "complete linkage", "average linkage"
    # returns LabeledDataPoints
    def get_clusters(self, method: str):
        # TODO define cluster class
        while not(self._is_one_cluster()):
            self._merge_closest(method)

    def _is_one_cluster(self):
        pass

    def _merge_closest(self, method: str):
        pass

    def plot_dendogram(self): # TODO should i?
        pass