#Example from "Artificial Intelligence with Python" - Prateek Joshi

import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

print("INPUT DATA")
print(input_data)

# Binarization

print("\nBINARIZATION")
data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
print("\nBinarized data:\n", data_binarized)

# Mean removal

print("\nMEAN REMOVAL")
print("\nBefore:")
print("\tMean = ", input_data.mean(axis=0))
print("\tStd deviation = ", input_data.std(axis=0))

data_without_mean = preprocessing.scale(input_data)
print("\nAfter:")
print("\tMean = ", data_without_mean.mean(axis=0))
print("\tStd deviation = ", data_without_mean.std(axis=0))
print("\nMean data removed:\n", data_without_mean)

# Scaling

print("\nSCALING (0-1)")
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)

# Scaling

# Normalization