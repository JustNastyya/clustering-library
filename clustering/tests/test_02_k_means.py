from clustering.basic_data_structures.data_points import DataPoints
from clustering.basic_data_structures.labeled_data_points import LabeledDataPoints
from clustering.method_classes.k_means import KMeans
from clustering.method_classes.k_nn import KNN
import matplotlib.pyplot as plt

# TODO jypzter notebook
def test_01():
    x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    
    data = DataPoints([x, y], reverse=True)
    knn = KMeans(data)
    points = knn.fit(k=3, max_iter=100)
    
    plot_data(points)


def plot_data(data: LabeledDataPoints):
    plt.figure(figsize=(6, 6))
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
    for key in data:
        x_0 = [data[key][i][0] for i in range(len(data[key]))]
        y_0 = [data[key][i][1] for i in range(len(data[key]))]

        plt.scatter(x_0, y_0, color=colors[key])
        
    plt.show()


