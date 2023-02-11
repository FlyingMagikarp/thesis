import pandas as pd
import tensorflow as tf
from datetime import datetime
import sys


def set_minority(dlist, minority):
    dlist[0] = minority
    return dlist


def drop_extra(dlist):
    dlist.pop(-1)
    dlist.pop(-1)
    dlist.pop(-1)
    dlist.pop(-1)
    dlist.pop(-1)
    dlist.pop(-1)
    dlist.pop(-1)

    return dlist


# minority,sex,         == 2
# rent,education,age,   == 3
# income,loan_size,     == 2
# payment_timing,year,  == 2
# job_stability,        == 1
# zip0,zip1,zip2,zip3,  == 4
# occupation0,occupation1,occupation2,  == 3
def get_test_data():
    df = pd.read_csv('../model/test_data.csv')
    data = []

    for i in df.iterrows():
        data.append(i[1].to_list())

    return data


def init_logfile(g):
    date = datetime.now()
    time_suffix = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '-' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second)
    filename = '../results/loan_results_{}.txt'.format(str(g)+'_'+time_suffix)
    with open(filename, 'w') as f:
        f.write(time_suffix + '\n')
    return filename


def log_string(filename, string):
    with open(filename, 'a') as f:
        f.write(string)
        f.write('\n')


def log_predictions(filename, preds, minority):
    tmp_str = ''
    for i in preds:
        tmp_str += str(round(i[0], 6)) + ' : '
    with open(filename, 'a') as f:
        f.write(
            '{0} & {1} \\\\'.format(str(minority), tmp_str)
        )
        f.write('\n')


start_time = datetime.now()

models = [
    {'model': tf.keras.models.load_model('./models/baseline'), 'model_type': 'baseline'},
    #{'model': tf.keras.models.load_model('./models/baseline_noextra'), 'model_type': 'baseline noextra'},
]

for minority in range(2):
    fn = init_logfile(minority)
    log_string(fn, 'Minority: '+str(minority))
    for model_info in models:
        model = model_info['model']

        data = get_test_data()

        print('##########')
        for value in data:
            value = set_minority(value, minority)
            #value = drop_extra(value)
            print(value)
            predictions = model.predict([value])
            log_predictions(fn, predictions, minority)
            print(predictions)
        print('##########')

print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
