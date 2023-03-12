import pandas as pd

# clean train dataset
df = pd.read_csv('../data/train.csv')

df = df.drop('Unnamed: 0', axis=1)
zip_code = pd.get_dummies(df['ZIP'])
df = pd.concat([df, zip_code], axis=1)
df = df.drop('ZIP', axis=1)
df = df.rename(columns={'MT01RA': 'zip0',
                        'MT04PA': 'zip1',
                        'MT12RA': 'zip2',
                        'MT15PA': 'zip3'})

occup = pd.get_dummies(df['occupation'])
df = pd.concat([df, occup], axis=1)
df = df.drop('occupation', axis=1)
df = df.rename(columns={'MZ01CD': 'occupation0',
                        'MZ10CD': 'occupation1',
                        'MZ11CD': 'occupation2'})

df['target'] = df['default'].astype(int)
df = df.drop('default', axis=1)

df.to_csv('../data/train_clean.csv', encoding='utf-8', index=False)

#####

# clean test dataset
df = pd.read_csv('../data/test.csv')

df = df.drop('Unnamed: 0', axis=1)
df = df.drop('Unnamed: 0.1', axis=1)

zip_code = pd.get_dummies(df['ZIP'])
df = pd.concat([df, zip_code], axis=1)
df = df.drop('ZIP', axis=1)
df = df.rename(columns={'MT01RA': 'zip0', 'MT04PA': 'zip1', 'MT12RA': 'zip2', 'MT15PA': 'zip3'})

occup = pd.get_dummies(df['occupation'])
df = pd.concat([df, occup], axis=1)
df = df.drop('occupation', axis=1)
df = df.rename(columns={'MZ01CD': 'occupation0', 'MZ10CD': 'occupation1', 'MZ11CD': 'occupation2'})

df['target'] = df['default'].astype(int)
df = df.drop('default', axis=1)

df = df[['minority', 'sex', 'rent', 'education', 'age', 'income', 'loan_size', 'payment_timing', 'year', 'job_stability', 'zip0', 'zip1', 'zip2', 'zip3', 'occupation0', 'occupation1', 'occupation2', 'target']]

df.to_csv('../data/test_clean.csv', encoding='utf-8', index=False)
