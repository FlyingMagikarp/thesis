import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/propublica_data_for_fairml.csv')

# score is 1-10, 1-4 low, 5-7 mid, 8-10 high
data = df.drop(['Two_yr_Recidivism'], axis=1)
y = df['Two_yr_Recidivism']

feature_columns = ['Number_of_Priors', 'Age_Above_FourtyFive', 'Age_Below_TwentyFive', 'African_American', 'Asian',
                   'Hispanic', 'Native_American', 'Other', 'Female', 'Misdemeanor']

data = df[feature_columns].values
y = df['score_factor'].values

train_x, test_x, train_y, test_y = train_test_split(data, y, test_size=0.25, shuffle=True, stratify=y, random_state=129)

# MLP
mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2
)

mlp.fit(train_x, train_y)

print('##########')
print('MLP')
print('##########')
print("Training set score: %f" % mlp.score(train_x, train_y))
print("Test set score: %f" % mlp.score(test_x, test_y))
print('##########')