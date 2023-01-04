import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Low', 'Medium', 'High']

values = [55, 26.6, 18.4]
plt.ylim(0, 100)
plt.bar(names, values)
plt.suptitle('African-American')
plt.show()

values = [74.7, 17.5, 7.8]
plt.ylim(0, 100)
plt.bar(names, values)
plt.suptitle('Caucasian')
plt.show()