import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

print("TensorFlow version:", tf.__version__)

df = pd.read_csv('../data/train_clean.csv')
print(df.head())
print(df.dtypes)
#zip0,zip1,zip2,zip3,occupation0,occupation1,occupation2
df_val = pd.read_csv('../data/test_clean.csv')


z = df_val.pop('minority')

y_val = df_val.pop('target')
X_val = df_val


z = df.pop('minority')

y = df.pop('target')
X = df

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=129)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(9, activation='relu', input_shape=(9,)))

model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))

model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))
model.add(tf.keras.layers.Dense(40, activation='relu'))

model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.Recall()])

val_dataset = tf.data.Dataset.from_tensor_slices((X_val, y_val))
val_dataset = val_dataset.batch(64)


model.fit(X, y, epochs=10, batch_size=64, validation_data=val_dataset)
results_first = model.evaluate(X_val, y_val, verbose=2)
print(results_first)

model.save('./models/nominority_noextra')



print('Done')