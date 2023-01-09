import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

print("TensorFlow version:", tf.__version__)

#df = pd.read_csv('./data/clean_data.csv')
#df = pd.read_csv('./data/propublica_data_for_fairml.csv')
df = pd.read_csv('../data/propublic_double.csv')
print(df.head())
print(df.dtypes)

# African_American,Asian,Hispanic,Native_American,Other
df = df.drop('Female', axis=1)
y = df.pop('Two_yr_Recidivism')
X = df

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=129)


#tensor = tf.convert_to_tensor(df)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(11, activation='relu', input_shape=(10,)))

model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))

model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.Recall()])

val_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
val_dataset = val_dataset.batch(64)


model.fit(X_train, y_train, epochs=33, batch_size=10, validation_data=val_dataset)
results_first = model.evaluate(X_test,  y_test, verbose=2)
print(results_first)

model.save('./models/nogender')



print('Done No Gender')