import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dict_from_list(dlist):
    return {
        'race': str(dlist[0]).replace(' ',''),
        'priors': dlist[1],
        'misdemeanors': dlist[2],
        '18': dlist[3],
        '25': dlist[4],
        '45': dlist[5]
    }



with open('./compas_baseline_formatted_for_analysis_male.txt') as file:
    lines = [line.rstrip().replace('\t', '').rstrip() for line in file]
len(lines)

data_white = []
data_black = []
data = []
for l in lines:
    tmp = l.split('&')

    if len(tmp) < 2:
        continue

    if 'Weiss' in tmp[0]:
        data_white.append(dict_from_list(l.split('&')))
    if 'Afroamerikaner' in tmp[0]:
        data_black.append(dict_from_list(l.split('&')))

    data.append(dict_from_list(l.split('&')))

print('Done')