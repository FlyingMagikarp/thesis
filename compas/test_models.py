import tensorflow as tf

# Two_yr_Recidivism,Number_of_Priors,score_factor, == 3
# Age_Above_FourtyFive,Age_Below_TwentyFive, == 3 possible configs
# African_American,Asian,Hispanic,Native_American,Other, == 6 possible configs
# Female,Misdemeanor == 2
def get_test_data():
    data = []
    #            prio, scor  age      races             gender, misdemeanor
    data.append([0, 0,       0, 0,    0, 0, 0, 0, 0,    0, 0])
    data.append([0, 0,       1, 0,    0, 0, 0, 0, 0,    0, 0])
    data.append([0, 0,       0, 1,    0, 0, 0, 0, 0,    0, 0])

    return data

model = tf.keras.models.load_model('./models/baseline')

data = get_test_data()
print(model.predict(data))

print('Done analysis')