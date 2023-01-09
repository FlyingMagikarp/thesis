from sklearn.linear_model import LogisticRegression
import pandas as pd

df = pd.read_csv('../data/data_with_caucasian.csv')
#feature_names = ['Number_of_Priors','score_factor','Age_Above_FourtyFive','Age_Below_TwentyFive','Caucasian','African_American','Asian','Hispanic','Native_American','Other','Female','Misdemeanor']
feature_names = ['Number_of_Priors','Age_Above_FourtyFive','Age_Below_TwentyFive','Caucasian','African_American','Asian','Hispanic','Native_American','Other','Female','Misdemeanor']

z = df.pop('score_factor')
y = df.pop('Two_yr_Recidivism')
X = df

model = LogisticRegression(random_state=129).fit(X, y)
result = list(zip(feature_names, model.coef_[0]))

for r in result:
    print(r)
