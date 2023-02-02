import tensorflow as tf
from datetime import datetime
import sys


def set_minority(dlist, minority):
    for i in dlist:
        i[0] = minority
    return dlist


def set_sex(dlist, sex):
    for i in dlist:
        i[1] = sex
    return dlist


# minority,sex,         == 2
# rent,education,age,   == 3
# income,loan_size,     == 2
# payment_timing,year,  == 2
# job_stability,        == 1
# zip0,zip1,zip2,zip3,  == 4
# occupation0,occupation1,occupation2,  == 3
def get_test_data(data_type):
    data = {}

    data['basic'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return data


def init_logfile(g):
    date = datetime.now()
    time_suffix = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '-' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second)
    filename = '../results/loan_results_{}.txt'.format(time_suffix)
    with open(filename, 'w') as f:
        f.write(time_suffix + '\n')
    return filename


def log_string(filename, string):
    with open(filename, 'a') as f:
        f.write(string)
        f.write('\n')


def log_predictions(filename, preds, key, i, j):
    with open(filename, 'a') as f:
        f.write(key + ' & ' + str(i) + ' & ' + str(j) + ' & ' + str(round(preds[0], 3)) + ' \\\\')
        f.write('\n')

start_time = datetime.now()

models = [
    {'model': tf.keras.models.load_model('./models/baseline'), 'model_type': 'baseline'},
]

for g in range(2):
    fn = init_logfile(g)
    log_string(fn, 'Gender: '+str(g))
    for i in range(2):
        log_string(fn, '#'+str(i)+'-'+str(j)+'#')
        for model_info in models:
            model = model_info['model']
            type = model_info['model_type']

            data = get_test_data(type)

            print('Model: ', type)
            print('##########')
            for key, value in data.items():
                print(key)
                value = set_minority(value, i)
                value = set_sex(value, g)
                print(value)
                predictions = model.predict(value)
                log_predictions(fn, predictions, key, i, g)
                print(model.predict(value))
            print('##########')

print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
