#import tensorflow as tf

# Two_yr_Recidivism,Number_of_Priors,score_factor, == 3, score_factor might get removed
# Age_Above_FourtyFive,Age_Below_TwentyFive, == 3 possible configs
# African_American,Asian,Hispanic,Native_American,Other, == 6 possible configs, also 6 fields with new dataset
# Female,Misdemeanor == 2
def get_test_data(data_type):
    data = {}

    ### male
    data['caucasian_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    1, 0, 0, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    1, 0, 0, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    1, 0, 0, 0, 0, 0,    0, 0]
    ]

    data['african_american_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 1, 0, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 1, 0, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 1, 0, 0, 0, 0,    0, 0]
    ]

    data['asian_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 1, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 1, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 1, 0, 0, 0,    0, 0]
    ]

    data['hispanic_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 1, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 1, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 1, 0, 0,    0, 0]
    ]

    data['native_american_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 0, 1, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 0, 1, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 0, 1, 0,    0, 0]
    ]

    data['other_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 0, 0, 1,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 0, 0, 1,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 0, 0, 1,    0, 0]
    ]

    ### female
    data['caucasian_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   1, 0, 0, 0, 0, 0,     1, 0],
        [0, 0,        1, 0,   1, 0, 0, 0, 0, 0,     1, 0],
        [0, 0,        0, 1,   1, 0, 0, 0, 0, 0,     1, 0]
    ]

    data['african_american_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   0, 1, 0, 0, 0, 0,     1, 0],
        [0, 0,        1, 0,   0, 1, 0, 0, 0, 0,     1, 0],
        [0, 0,        0, 1,   0, 1, 0, 0, 0, 0,     1, 0]
    ]

    data['asian_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   0, 0, 1, 0, 0, 0,     1, 0],
        [0, 0,        1, 0,   0, 0, 1, 0, 0, 0,     1, 0],
        [0, 0,        0, 1,   0, 0, 1, 0, 0, 0,     1, 0]
    ]

    data['hispanic_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   0, 0, 0, 1, 0, 0,     1, 0],
        [0, 0,        1, 0,   0, 0, 0, 1, 0, 0,     1, 0],
        [0, 0,        0, 1,   0, 0, 0, 1, 0, 0,     1, 0]
    ]

    data['native_american_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   0, 0, 0, 0, 1, 0,     1, 0],
        [0, 0,        1, 0,   0, 0, 0, 0, 1, 0,     1, 0],
        [0, 0,        0, 1,   0, 0, 0, 0, 1, 0,     1, 0]
    ]

    data['other_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0, 0,        0, 0,   0, 0, 0, 0, 0, 1,     1, 0],
        [0, 0,        1, 0,   0, 0, 0, 0, 0, 1,     1, 0],
        [0, 0,        0, 1,   0, 0, 0, 0, 0, 1,     1, 0]
    ]


    if data_type == 'baseline':
        return data
    if data_type == 'norace':
        for key, value in data.items():
            for v in value:
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
        return data
    if data_type == 'nogender':
        for key, value in data.items():
            for v in value:
                v.pop(10)
        return data

    return data

models = [{'model': "tf.keras.models.load_model('./models/baseline')", 'model_type': 'baseline'},
          {'model': "tf.keras.models.load_model('./models/norace')", 'model_type': 'norace'},
          {'model': "tf.keras.models.load_model('./models/nogender')", 'model_type': 'nogender'}]

for model_info in models:
    model = model_info['model']
    type = model_info['model_type']

    data = get_test_data(type)

    print('Model: ', type)
    print('##########')
    for key, value in data.items():
        print(key)
        #print(model.predict(value))
    print('##########')

print('Done analysis')