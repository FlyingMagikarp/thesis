import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/train_clean.csv')

print('Total Entires', len(df))
print('Default', len(df.loc[df['target'] == 1]))
print('NO Default', len(df.loc[df['target'] == 0]))
print('#####')
print('Male', len(df.loc[df['sex'] == 1]))
print('Female', len(df.loc[df['sex'] == 0]))
print('Male Default', len(df.loc[(df['sex'] == 1) & (df['target'] == 1)]))
print('Female Default', len(df.loc[(df['sex'] == 0) & (df['target'] == 1)]))
print('#####')
print('Majority', len(df.loc[df['minority'] == 0]))
print('Minorities', len(df.loc[df['minority'] == 1]))
print('Majority Default', len(df.loc[(df['minority'] == 0) & (df['target'] == 1)]))
print('Minority Default', len(df.loc[(df['minority'] == 1) & (df['target'] == 1)]))

default_df = df.loc[df['target'] == 1]
nodefault_df = df.loc[df['target'] == 0]

male_df = df.loc[df['sex'] == 1]
female_df = df.loc[df['sex'] == 0]

male_default_df = male_df.loc[male_df['target'] == 1]
male_nodefault_df = male_df.loc[male_df['target'] == 0]

male_maj_df = male_df.loc[male_df['minority'] == 0]
male_min_df = male_df.loc[male_df['minority'] == 1]

female_maj_df = female_df.loc[female_df['minority'] == 0]
female_min_df = female_df.loc[female_df['minority'] == 1]

female_default_df = female_df.loc[female_df['target'] == 1]
female_nodefault_df = female_df.loc[female_df['target'] == 0]

majority_df = df.loc[df['minority'] == 0]
minority_df = df.loc[df['minority'] == 1]

majority_default_df = majority_df.loc[majority_df['target'] == 1]
majority_nodefault_df = majority_df.loc[majority_df['target'] == 0]

minority_default_df = minority_df.loc[minority_df['target'] == 1]
minority_nodefault_df = minority_df.loc[minority_df['target'] == 0]


values = df[['sex']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Geschlecht': ['Männlich', 'Weiblich']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Geschlecht', y='Verteilung', palette=['blue', 'pink']).set(title='Verteilung Geschlecht')
plt.show()

values = df[['minority']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Ethnische Zugehörigkeit': ['Minderheit', 'Mehrheit']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Ethnische Zugehörigkeit', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung ethnische Zugehörigkeit')
plt.show()

values = df[['target']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Kreditausfall': ['Ausfall', 'kein Ausfall']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Kreditausfall', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung Kreditausfälle')
plt.show()

values = male_df[['target']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Kreditausfall': ['Ausfall', 'kein Ausfall']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Kreditausfall', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung Kreditausfälle bei männlichen Personen')
plt.show()

values = female_df[['target']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Kreditausfall': ['Ausfall', 'kein Ausfall']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Kreditausfall', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung Kreditausfälle bei weiblichen Personen')
plt.show()

values = majority_df[['target']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Kreditausfall': ['kein Ausfall', 'Ausfall']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Kreditausfall', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung Kreditausfälle bei Angehöriger einer ethnischen Mehrheit')
plt.show()

values = minority_df[['target']].value_counts(normalize=True).values
d = {'Verteilung': values, 'Kreditausfall': ['Ausfall', 'kein Ausfall']}
df_plot = pd.DataFrame(data=d)
sns.barplot(data=df_plot, x='Kreditausfall', y='Verteilung', palette=['blue', 'green']).set(title='Verteilung Kreditausfälle bei Angehöriger einer ethnischen Minderheit')
plt.show()

print('done')