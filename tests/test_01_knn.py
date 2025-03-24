from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from clustering.method_classes.k_nn import KNN
import matplotlib.pyplot as plt

def test_01():
    x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

    data = LabeledDataPoints([x, y], labels=classes)
    knn = KNN(data)
    knn.fit(k=3)
    
    new_points = [8, 21]
    new_points_data = DataPoints([new_points])

    prediction = knn.predict(new_points_data)

    assert prediction == [0]
