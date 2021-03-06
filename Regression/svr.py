import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Read Data
from sklearn.datasets import load_boston 
dataset = load_boston()

# Choose which features to use
x = dataset["data"][:, [9,10]] # using TAX and PRATIO features
y = dataset["target"]     # output value

# Split data into train and test dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x[:,:], y, test_size = 0.2, random_state = 42)

# Data Preprocessing
from sklearn.preprocessing import StandardScaler
sc_x    = StandardScaler()
sc_y    = StandardScaler()
x_train = sc_x.fit_transform(x_train) # Scaling the data
x_test  = sc_x.transform(x_test)

# Train Model
from sklearn.svm import SVR
regr = SVR()
regr.fit(x_train, y_train)

# Predict Results
y_pred = regr.predict(x_test)

# Measure Accuracy
from sklearn.metrics import mean_squared_error
acc = mean_squared_error(y_test, y_pred)

# Visualisation
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_test[:,0], x_test[:,1], y_test, color = 'r')
ax.scatter(x_test[:,0], x_test[:,1], y_pred, color = 'b')