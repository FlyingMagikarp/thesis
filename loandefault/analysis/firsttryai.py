from sklearn.neural_network import MLPClassifier
import pandas as pd

train = pd.read_csv('../data/train_clean.csv')
test = pd.read_csv('../data/test_clean.csv')

y_train = train.pop('target')
X_train = train

y_test = test.pop('target')
X_test = test

model = MLPClassifier(random_state=129, max_iter=300).fit(X_train, y_train)
print(model.score(X_test, y_test))

print('Done')