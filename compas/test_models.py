import tensorflow as tf

# Two_yr_Recidivism,Number_of_Priors,score_factor, == 3
# Age_Above_FourtyFive,Age_Below_TwentyFive, == 3 possible configs
# African_American,Asian,Hispanic,Native_American,Other, == 6 possible configs
# Female,Misdemeanor == 2
def get_test_data():
    data = {}
    data['caucasian'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 0, 0,    0, 0]
    ]

    data['african_american'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    1, 0, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    1, 0, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    1, 0, 0, 0, 0,    0, 0]
    ]

    data['asian'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 1, 0, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 1, 0, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 1, 0, 0, 0,    0, 0]
    ]

    data['hispanic'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 1, 0, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 1, 0, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 1, 0, 0,    0, 0]
    ]

    data['native_american'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 1, 0,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 1, 0,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 1, 0,    0, 0]
    ]

    data['other'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0, 0,       0, 0,    0, 0, 0, 0, 1,    0, 0],
        [0, 0,       1, 0,    0, 0, 0, 0, 1,    0, 0],
        [0, 0,       0, 1,    0, 0, 0, 0, 1,    0, 0]
    ]




    return data

#model = tf.keras.models.load_model('./models/baseline')
#model = tf.keras.models.load_model('./models/norace')
#model_type = 'norace'
model = tf.keras.models.load_model('./models/nogender')
model_type = 'nogender'

data = get_test_data()

for key, value in data.items():
    print(key)
    if model_type == 'norace':
        for v in value:
            v.pop(4)
            v.pop(4)
            v.pop(4)
            v.pop(4)
            v.pop(4)
    if model_type == 'nogender':
        for v in value:
            v.pop(9)
    print(model.predict(value))

print('Done analysis')