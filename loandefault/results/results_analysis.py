import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dict_from_list(dlist):
    if len(dlist) == 2:
        return {
            'id': str(dlist[0]).replace(' ', ''),
            'majority': dlist[1],
        }
    return {
        'id': str(dlist[0]).replace(' ',''),
        'majority': dlist[1],
        'minority': dlist[2],
    }



'''with open('./loan_results_analysis_baseline.txt') as file:
    lines = [line.rstrip().replace('\t', '').rstrip() for line in file]
len(lines)

data_maj = []
data_min = []
data = []
for l in lines:
    tmp = l.split('&')

    if len(tmp) < 2:
        continue

    data.append(dict_from_list(l.split('&')))

for i in data:
    data_maj.append([i['id'], i['majority']])
    data_min.append([i['id'], i['minority']])'''


with open('./loan_results_analysis_norace.txt') as file:
    lines = [line.rstrip().replace('\t', '').rstrip() for line in file]
len(lines)

data_norace = []
for l in lines:
    tmp = l.split('&')

    if len(tmp) < 2:
        continue

    data_norace.append(dict_from_list(l.split('&')))


print(len(data_norace))

count_norace = 0

for i in data_norace:
    count_norace += float(i['majority'])

avg_norace = round(count_norace, 3)

print(count_norace, avg_norace)

print('Done')