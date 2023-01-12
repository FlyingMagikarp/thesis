from sklearn.neural_network import MLPClassifier
import pandas as pd

train = pd.read_csv('../data/train_clean.csv')
test = pd.read_csv('../data/test_clean.csv')

y_train = train.pop('target')
X_train = train

y_test = test.pop('target')
X_test = test

model = MLPClassifier(random_state=129, max_iter=100).fit(X_train, y_train)
print(model.score(X_test, y_test))

print('#####')
test_data = [
    [0, 0, 1, 57.23065034222223, 36.0509266155936, 205168.0222437496, 7600.29219942136, 3.3021933127354868, 0, 3.015553523369212, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 57.23065034222223, 36.0509266155936, 205168.0222437496, 7600.29219942136, 3.3021933127354868, 0, 3.015553523369212, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 57.23065034222223, 36.0509266155936, 205168.0222437496, 7600.29219942136, 3.3021933127354868, 0, 3.015553523369212, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 57.23065034222223, 36.0509266155936, 205168.0222437496, 7600.29219942136, 3.3021933127354868, 0, 3.015553523369212, 0, 1, 0, 0, 0, 1, 0]
]
print(model.predict(test_data))
print('#####')

print('Done')