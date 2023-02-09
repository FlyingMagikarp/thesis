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


def set_job_stab(dlist, jstab):
    for i in dlist:
        i[-8] = jstab
    return dlist


def set_year(dlist, year):
    for i in dlist:
        i[-9] = year
    return dlist


def set_payment_timing(dlist, payment_timing):
    for i in dlist:
        i[-10] = payment_timing
    return dlist


def set_loan_size(dlist, loan_size):
    for i in dlist:
        i[-11] = loan_size
    return dlist


def set_income(dlist, income):
    for i in dlist:
        i[-12] = income
    return dlist


def set_age(dlist, age):
    for i in dlist:
        i[-13] = age
    return dlist


def set_education(dlist, edu):
    for i in dlist:
        i[-14] = edu
    return dlist


def set_rent(dlist, rent):
    for i in dlist:
        i[-15] = rent
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

    data['data_rent0'] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]

                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],

                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]

    #data['data_rent1'] = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],

                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],

                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                         #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]

    return data


data_education = [30, 40, 50, 60, 70, 80]
data_age = [18, 28, 38, 48, 58, 68]
data_income = [70000, 100000, 150000, 200000]
data_loan_size = [200, 400, 800, 1000, 5000, 10000]
data_payment_timing = [1, 2, 3, 4]
data_job_stability = [40, 50, 60, 70, 80, 90, 100]


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


def log_predictions(filename, preds, key, minority, sex, education, age, income, loan_size, payment_timing, job_stability):
    tmp_str = ''
    for i in preds:
        tmp_str+= str(round(i[0], 3)) + ' : '
    with open(filename, 'a') as f:
        f.write(
            '{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8} & {9} \\\\'.format(key,
                                                                                    str(minority),
                                                                                    str(sex),
                                                                                    str(education),
                                                                                    str(age),
                                                                                    str(income),
                                                                                    str(loan_size),
                                                                                    str(payment_timing),
                                                                                    str(job_stability),
                                                                                    str(tmp_str)
                                                                                    )
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
        for education in data_education:
            for age in data_age:
                for income in data_income:
                    for loan_size in data_loan_size:
                        for payment_timing in data_payment_timing:
                            for job_stab in data_job_stability:

                                for model_info in models:
                                    model = model_info['model']

                                    data = get_test_data()

                                    print('##########')
                                    for key, value in data.items():
                                        print(key)
                                        value = set_sex(value, gender)
                                        value = set_minority(value, minority)
                                        value = set_education(value, education)
                                        value = set_age(value, age)
                                        value = set_income(value, income)
                                        value = set_loan_size(value, loan_size)
                                        value = set_payment_timing(value, payment_timing)
                                        value = set_job_stab(value, job_stab)
                                        print(value)
                                        predictions = model.predict(value)
                                        log_predictions(fn, predictions, key, gender, minority, education, age, income, loan_size, payment_timing, job_stab)
                                        print(model.predict(value))
                                    print('##########')

print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
