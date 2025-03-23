from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from clustering.method_classes.k_means import KMeans


def test_01():
    x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    
    data = DataPoints([x, y], reverse=True)
    knn = KMeans(data)
    points = knn.fit(k=3, max_iter=100)
    
    assert points.data[0].data == [[4, 21], [5, 19]]
    assert points.data[1].data == [[4, 17], [3, 16]]
    assert points.data[2].data == [[10, 24], [11, 25], [14, 24], [8, 22], [10, 21], [12, 21]]
