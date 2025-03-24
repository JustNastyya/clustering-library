# clustering

[![PyPI - Version](https://img.shields.io/pypi/v/clustering.svg)](https://pypi.org/project/clustering)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/clustering.svg)](https://pypi.org/project/clustering)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install clustering

python -m pip install -e .
```

## Introduction

# Working with Data Structures

The Library containes two Datastructures: `DataPoints` and `LabeledDataPoints`

### `Data Points`
`Data Points` is used to store Data vectors. The data is stored as a list of lists, where:

where each list represents a data point (float)

data = [p1, p2, p3, ..., pn]

where p1 = [x1, x2, x3, ..., xk] and len(p1) = len(p2) = len(p3) = ... = len(pn)

You can acess and iterate over the data just like a normal list of lists

it is also possible to initialize Data Points with a given list of Variables. To do so use `reverse=True`

### `LabeledDataPoints`

Class `LabeledDataPoints` stores classified DataPoints as a Dictionary of DataPoints.

Can be initialized as:

1. list of Variables with classes attatched to it. Here `classes[0]` is the label for point `(x[0], y[0])`

2. a Dictionary of a list of vectors, where a vector is one point

3. Datapoints with classes attatched. Here `classes[0]` is the label for `data_points[0]`

### Training a K-NN Model

1. Initialize the knn model by giving an argument data of type `LabeledDataPoints`

2. execute `.fit()` function with parameter k

3. initialize data points you want to classify

4. make a prediction using `predict` function.

### Training a K-Means Model

1. Initialize the data of type DataPoints

2. Training the model by providing the number of wished classes and Maximum of iteration

3. The Output of the `fit` function of an Object of type `labeledDataPoints`.


## License

`clustering` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
