import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/data_with_caucasian.csv')

print(len(df))
print('Male', df.loc[df['Female'] == 0].shape[0])
print('Female', df.loc[df['Female'] == 1].shape[0])

df_male = df.loc[df['Female'] == 0]
df_female = df.loc[df['Female'] == 1]

print(df_male[['Two_yr_Recidivism']].value_counts())


df_male[['Two_yr_Recidivism']].value_counts().plot(kind='bar')
plt.suptitle('All males')
plt.show()

df_male_african_american = df_male.loc[(df_male['African_American'] == 0) & (df_male['Hispanic'] == 0) & (df_male['Asian'] == 0) & (df_male['Native_American'] == 0) & (df_male['Other'] == 0)]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('Caucasian')
plt.show()

print(df_male[['African_American']].value_counts())
df_male_african_american = df_male.loc[df_male['African_American'] == 1]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).sort_index().plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('African_American')
plt.show()

print(df_male[['Hispanic']].value_counts())
df_male_african_american = df_male.loc[df_male['Hispanic'] == 1]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('Hispanic')
plt.show()

print(df_male[['Asian']].value_counts())
df_male_african_american = df_male.loc[df_male['Asian'] == 1]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('Asian')
plt.show()

print(df_male[['Native_American']].value_counts())
df_male_african_american = df_male.loc[df_male['Native_American'] == 1]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('Native_American')
plt.show()

print(df_male[['Other']].value_counts())
df_male_african_american = df_male.loc[df_male['Other'] == 1]
df_male_african_american[['Two_yr_Recidivism']].value_counts(normalize=True).plot(kind='bar')
plt.ylim(0, 1)
plt.suptitle('Other')
plt.show()