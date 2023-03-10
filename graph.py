import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


d = {'Model': [
        'Baseline',
        'Baseline',
        'Ohne Ethnie',
        'Ohne Ethnie',
        'Ohne Geschlecht ',
        'Ohne Geschlecht ',
        'Künstlich ergänzte Daten',
        'Künstlich ergänzte Daten'
    ],
    'Metrik': [
        'Accuracy',
        'Recall',
        'Accuracy',
        'Recall',
        'Accuracy',
        'Recall',
        'Accuracy',
        'Recall'
    ],
    'Value': [
        0.7183,
        0.7385,
        0.7252,
        0.6677,
        0.7727,
        0.7385,
        0.7374,
        0.6005
    ]
}

df = pd.DataFrame(data=d)


#plt.figure(figsize=(10,6))
#ax = sns.barplot(data=df, x='Model', y='Value', hue="Metrik", orient='v').set(title='Übersicht Metriken COMPAS')
#plt.ylabel('Modell', rotation=90)
#plt.show()



d = {'Model': [
        'Baseline',
        'Baseline',
        'Ohne Ethnie',
        'Ohne Ethnie',
        'Künstlich ergänzte Daten',
        'Künstlich ergänzte Daten'
    ],
    'Metrik': [
        'Accuracy',
        'Recall',
        'Accuracy',
        'Recall',
        'Accuracy',
        'Recall'
    ],
    'Value': [
        0.8924,
        0.6454,
        0.8503,
        0.6121,
        0.7884,
        0.5805
    ]
}

df = pd.DataFrame(data=d)

plt.figure(figsize=(10,6))
ax = sns.barplot(data=df, x='Model', y='Value', hue="Metrik", orient='v').set(title='Übersicht Metriken Kreditausfälle')
plt.show()



print('done')
