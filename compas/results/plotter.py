import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# general recidivism
# d = {'Anzahl Einträge': [2809, 3363], 'Rückfälligkeit': ['Rückfällig', 'nicht Rückfällig']}
# df = pd.DataFrame(data=d)
#
# sns.barplot(data=df, x='Rückfälligkeit', y='Anzahl Einträge', palette=['red', 'green']).set(title='Verteilung Rückfälligkeit')
# plt.show()
#
# # general gender distribution
# d = {'Anzahl Einträge': [4997, 1175], 'Geschlecht': ['Männlich', 'Weiblich']}
# df = pd.DataFrame(data=d)
#
# sns.barplot(data=df, x='Geschlecht', y='Anzahl Einträge', palette=['blue', 'pink']).set(title='Verteilung Geschlecht')
# plt.show()

# general races distribution
# d = {'Anteil %': [34.1, 51.5, 8.2, 0.5, 0.2, 5.5],
#      'Ethnische Zugehörigkeit': ['Weiss', 'Afroamerikaner', 'Latinoamerikaner', 'Asiaten', 'Amerikanische Ureinwohner', 'Andere']}
# df = pd.DataFrame(data=d)
#
# sns.barplot(data=df, x='Ethnische Zugehörigkeit', y='Anteil %').set(title='Verteilung ethnische Zugehörigkeit')
# plt.xticks(rotation=90)
# plt.subplots_adjust(bottom=0.5)
# plt.show()

# male recidivism
# d = {'Anzahl Einträge': [2396, 2601], 'Rückfälligkeit': ['Rückfällig', 'nicht Rückfällig']}
# df = pd.DataFrame(data=d)
# sns.barplot(data=df, x='Rückfälligkeit', y='Anzahl Einträge', palette=['red', 'green']).set(title='Verteilung Rückfälligkeit bei männlichen Straftätern')
# plt.show()

# female recidivism
d = {'Anzahl Einträge': [413, 762], 'Rückfälligkeit': ['Rückfällig', 'nicht Rückfällig']}
df = pd.DataFrame(data=d)
sns.barplot(data=df, x='Rückfälligkeit', y='Anzahl Einträge', palette=['red', 'green']).set(title='Verteilung Rückfälligkeit bei weiblichen Straftätern')
plt.show()