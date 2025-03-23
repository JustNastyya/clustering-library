from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from clustering.method_classes.k_nn import KNN
from clustering.method_classes.k_means import KMeans
import matplotlib.pyplot as plt

x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = DataPoints([x, y], reverse=True)

knn = KMeans(data)
points = knn.fit(k=3, max_iter=100)

points.data