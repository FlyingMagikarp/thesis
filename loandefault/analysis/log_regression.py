from sklearn.linear_model import LogisticRegression
import pandas as pd

df = pd.read_csv('../data/train_clean.csv')
#feature_names = ['Number_of_Priors','score_factor','Age_Above_FourtyFive','Age_Below_TwentyFive','Caucasian','African_American','Asian','Hispanic','Native_American','Other','Female','Misdemeanor']
#feature_names = ['Number_of_Priors','Age_Above_FourtyFive','Age_Below_TwentyFive','Caucasian','African_American','Asian','Hispanic','Native_American','Other','Female','Misdemeanor']
feature_names = ['minority', 'sex', 'rent', 'education', 'age', 'income', 'loan_size', 'payment_timing', 'year', 'job_stability', 'zip0', 'zip1', 'zip2', 'zip3', 'occupation0', 'occupation1', 'occupation2']

#z = df.pop('score_factor')
y = df.pop('target')
X = df

model = LogisticRegression(random_state=129).fit(X, y)
result = list(zip(feature_names, model.coef_[0]))

for r in result:
    print(r)
