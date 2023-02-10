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
def get_test_data():
    data = {}

    data['sample_maj_f_0'] = [
        [0, 0, 1, 48, 26, 157549, 2000, 3, 3, 105, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 52, 36, 186519, 6757, 4, 25, 68, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 42, 50, 165075, 2403, 3, 13, 69, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 54, 37, 196092, 9541, 3, 8, 93, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 51, 46, 195693, 3467, 3, 2, 92, 0, 0, 1, 0, 1, 0, 0]
    ]

    data['sample_maj_f_1'] = [
        [0, 0, 1, 49, 67, 209830, 723, 2, 23, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 47, 44, 181625, 3927, 4, 21, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 42, 22, 132979, 4540, 3, 20, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 55, 39, 203231, 5378, 4, 3, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 53, 32, 187240, 7278, 2, 26, 4, 0, 1, 0, 0, 1, 0, 0]
    ]

    data['sample_maj_m_0'] = [
        [0, 1, 0, 2, 46, 8318, 8591, 1, 5, 95, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 4, 53, 16869, 5299, 3, 29, 99, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 24, 5217, 7873, 3, 11, 109, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 3, 60, 15732, 257, 2, 9, 96, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 2, 41, 11078, 106, 3, 15, 108, 0, 1, 0, 0, 1, 0, 0]
    ]

    data['sample_maj_m_1'] = [
        [0, 1, 1, 3, 18, 8622, 3356, 4, 28, 3, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 30, 6766, 8043, 3, 14, 6, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 50, 8436, 7203, 3, 22, 2, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, 2, 50, 8274, 1621, 3, 26, 4, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 51, 2947, 8731, 3, 20, 3, 0, 0, 0, 1, 1, 0, 0]
    ]

    data['sample_min_f_0'] = [
        [1, 0, 0, 55, 35, 197724, 6844, 3, 14, 119, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 56, 36, 202159, 4873, 3, 18, 101, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 51, 63, 212661, 9703, 4, 12, 113, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 57, 37, 208171, 5890, 2, 20, 81, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 54, 53, 215696, 7965, 1, 19, 96, 0, 0, 1, 0, 0, 1, 0]
    ]

    data['sample_min_f_1'] = [
        [1, 0, 1, 56, 21, 173630, 4483, 4, 18, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 55, 41, 206173, 3723, 3, 3, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 48, 59, 200226, 9208, 3, 3, 4, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 46, 50, 181387, 6869, -1, 26, 2, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 59, 34, 209100, 7009, 3, 23, 2, 0, 1, 0, 0, 0, 1, 0]
    ]

    data['sample_min_m_0'] = [
        [1, 1, 1, 0, 43, 135, 8665, 3, 0, 2, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 41, 4397, 8698, 3, 24, 81, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 3, 23, 9068, 7788, 3, 15, 77, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 53, 141, 7851, 2, 26, 2, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 22, 7, 9466, 3, 21, 2, 0, 1, 0, 0, 0, 0, 1]
    ]

    data['sample_min_m_1'] = [
        [1, 1, 1, 1, 67, 4739, 8424, 3, 22, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 63, 2172, 9815, 2, 20, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 33, 4814, 5252, 3, 20, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 66, 6575, 1374, 1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 46, 2791, 8194, 3, 21, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    data['testing'] = [
        [0, 0, 0, 0,  0,      0,     0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 67, 240739, 8424, 3, 22, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

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


def log_predictions(filename, preds, key, minority, sex):
    tmp_str = ''
    for i in preds:
        tmp_str += str(round(i[0], 3)) + ' : '
    with open(filename, 'a') as f:
        f.write(
            '{0} & {1} & {2} & {3} \\\\'.format(key, str(minority), str(sex), tmp_str)
        )
        f.write('\n')


start_time = datetime.now()

models = [
    {'model': tf.keras.models.load_model('./models/baseline'), 'model_type': 'baseline'},
]

for gender in range(2):
    fn = init_logfile(gender)
    log_string(fn, 'Gender: '+str(gender))
    for minority in range(2):
        log_string(fn, 'Minority: '+str(minority))
        for model_info in models:
            model = model_info['model']

            data = get_test_data()

            print('##########')
            for key, value in data.items():
                print(key)
                value = set_sex(value, gender)
                value = set_minority(value, minority)
                print(value)
                predictions = model.predict(value)
                log_predictions(fn, predictions, key, gender, minority)
                print(predictions)
            print('##########')

print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
