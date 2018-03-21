import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

from utilities import visualize_classifier

# Input file containing data
input_file = '../../data/data_multivar_nb.txt'

# Load data from input file
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1] 

# Create Naive Bayes classifier 
classifier = GaussianNB()

# Train the classifier
classifier.fit(X, y)

joblib.dump(classifier, '../../models/sklearn-naive-bayes.pkl') 

# Predict the values for training data
y_pred = classifier.predict(X)

# Compute accuracy
# X.shape[0] is the total of records in X (400).
accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
print("Accuracy of Naive Bayes classifier =", round(accuracy, 2), "%")

# Visualize the performance of the classifier
visualize_classifier(classifier, X, y)