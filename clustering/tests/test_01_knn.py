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
    print(prediction)

    # evaluate
    assert prediction == [0]

    plot_data(x, y, classes, new_points[0], new_points[1], prediction[0])


def plot_data(x, y, classes, new_x, new_y, prediction):
    x_0 = [x[i] for i in range(len(x)) if classes[i] == 0]
    y_0 = [y[i] for i in range(len(y)) if classes[i] == 0]

    x_1 = [x[i] for i in range(len(x)) if classes[i] == 1]
    y_1 = [y[i] for i in range(len(y)) if classes[i] == 1]

    plt.figure(figsize=(6, 6))
    plt.scatter(x_0, y_0, marker='o', label='Class 0', color='blue')
    plt.scatter(x_1, y_1, marker='x', label='Class 1', color='green')
    
    marker = "o" if prediction == 0 else "x"
    plt.scatter(new_x, new_y, marker=marker, color='red', edgecolor='black')

    plt.show()


