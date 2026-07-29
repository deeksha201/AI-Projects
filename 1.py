import numpy as np
num=[35,56,78,12,89,23,45,67,90,34]
mean=np.mean(num)
print(mean)
max=np.max(num)
print(max)
min=np.min(num)
print(min)

import pandas as pd
data={
    "name":["Alice","Bob","Charlie","David"],
    "age":[25,30,35,40],
    "city":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
print(df)
print(df.head())

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# import tensorflow as tf
# model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
# model.compile(optimizer='sgd', loss='mean_squared_error')


import numpy as np
number=np.array([1,2,3,4,5])
print(number.mean())
print(number.max())
print(number.min())

import pandas as pd
data={
    "name":["Alice","Bob","Charlie","David"],
    "age":[25,30,35,40],
    "city":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
print(df)