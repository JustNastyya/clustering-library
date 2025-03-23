from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from clustering.method_classes.k_nn import KNN
import matplotlib.pyplot as plt

data_points_raw = [
    [4, 21],
    [5, 19],
    [10, 24],
    [4, 17],
    [3, 16],
    [11, 25],
    [14, 24],
    [8, 22],
    [10, 21],
    [12, 21]
]
data_points = DataPoints(data_points_raw)
len(data_points)
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
data = LabeledDataPoints(data_points_raw, labels=classes)




x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
type(x).__name__
data = LabeledDataPoints([x, y], labels=classes)

data_raw = {0: [
    [4, 21],
    [5, 19],
    [4, 17],
    [3, 16],
    [8, 22]
], 1: [
    [10, 24],
    [11, 25],
    [14, 24],
    [10, 21],
    [12, 21]
]}
data = LabeledDataPoints(data_raw)