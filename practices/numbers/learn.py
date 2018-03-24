    import numpy as np
    from sklearn.naive_bayes import GaussianNB
    from sklearn import linear_model
    from sklearn.externals import joblib

    class Learn:

        @staticmethod
        def createLogisticalRegression(solver, c):
            return linear_model.LogisticRegression(solver = solver, C = c)

        @staticmethod
        def createGausianNB():
            return GaussianNB()

        @staticmethod
        def play(X, y, test):
            print("NAÏVE BAYES")
            gauss = GaussianNB()
            Learn.train(gauss,X, y)
            Learn.test(gauss, test)

            print("LOGISTIC REGRESSION")
            logis = linear_model.LogisticRegression(solver='liblinear', C=1)
            Learn.train(logis,X, y)
            Learn.test(logis, test)

        @staticmethod
        def train(classifier, X, y):
            classifier.fit(X, y)
            y_pred = classifier.predict(X)
            accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
            print("Accuracy: ", round(accuracy, 2), "%")

        @staticmethod
        def test(classifier, X):
            print("Examples:")
            for x in X:
                print(str(x) + ": " + str(classifier.predict(x)))

        @staticmethod
        def load(classifier, path):
            classifier = joblib.load(path)

        @staticmethod
        def save(classifier, path):
            joblib.dump(classifier, path)