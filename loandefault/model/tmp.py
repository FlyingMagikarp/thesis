import tensorflow as tf
import pandas as pd
from datetime import datetime
import numpy as np
import csv


df_val = pd.read_csv('../data/test_clean.csv')
y_val = df_val.pop('target')
X_val = df_val

model = tf.keras.models.load_model('./models/baseline')

preds = model.predict(X_val)

errors_idx = []
for index, value in y_val.items():
    tmp = preds[index][0]
    if round(tmp) != value:
        errors_idx.append(index)

start_time = datetime.now()
results = []
results_big_diff = []
print(errors_idx[-1])
for idx in errors_idx:
    if int(idx) > 10000:
        break
    tmp_target = y_val.loc[[idx]].values.tolist()[0]

    tmp_arr = X_val.loc[[idx]].values.tolist()[0]
    # minority to 0
    tmp_arr[0] = 0
    pred_maj = model.predict([tmp_arr], verbose=0)

    # minority to 1
    tmp_arr[1] = 1
    pred_min = model.predict([tmp_arr], verbose=0)

    results.append([idx, pred_maj[0][0], pred_min[0][0]])
    print(idx, pred_maj, pred_min)
    if abs(pred_maj[0] - pred_min) > 0.05:
        results_big_diff.append([idx, pred_maj[0][0], pred_min[0][0], abs(pred_maj[0][0] - pred_min[0][0])])

with open("./test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(results_big_diff)

# tmp_sorted = sorted(results_big_diff, key=lambda x: x[-1])
print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
print('Done')
