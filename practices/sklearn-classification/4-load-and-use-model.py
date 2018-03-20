import numpy as np
from sklearn import linear_model 
from sklearn.externals import joblib

classifier = joblib.load('../../models/sklearn-classification.pkl')

X = np.array([[2.3, 3.2],
              [4.2, 5.1],
              [1.1, 4.2],])
y = classifier.predict(X)
print(y)