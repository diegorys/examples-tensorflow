#Hi scikit-learn: http://scikit-learn.org/

#Example from "Artificial Intelligence with Python" - Prateek Joshi

from sklearn import datasets

house_prices = datasets.load_boston()

print(house_prices.data)