import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/clean_data.csv')

print(len(df))
print('Male', df.loc[df['Male'] == 1].shape[0])
print('Female', df.loc[df['Male'] == 0].shape[0])

df_male = df.loc[df['Male'] == 1]
df_female = df.loc[df['Male'] == 0]

print(df_male[['DecileScore']].value_counts())

df_male.drop(df_male[df_male['DecileScore'] == -1].index, inplace=True)
df_male[['DecileScore']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('All males')
plt.show()

print(df_male[['African-American']].value_counts())
df_male_african_american = df_male.loc[df_male['African-American'] == 1]
df_male_african_american[['DecileScore']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 0.5)
plt.suptitle('African-American')
plt.show()

print(df_male[['Caucasian']].value_counts())
df_male_caucasian = df_male.loc[df_male['Caucasian'] == 1]
df_male_caucasian[['DecileScore', 'Caucasian']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 0.5)
plt.suptitle('Caucasian')
plt.show()

print(df_male[['Hispanic']].value_counts())
df_male_hispanic = df_male.loc[df_male['Hispanic'] == 1]
df_male_hispanic[['DecileScore', 'Hispanic']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 0.5)
plt.suptitle('Hispanic')
plt.show()