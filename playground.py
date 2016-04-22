
#
# playground.py
# 4/22/16

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn import preprocessing, datasets
from sklearn.metrics import mean_squared_error
import math
import csv


dataFile = pd.read_csv("traindata.csv", header=0)

# CFA is our Y
cfa = dataFile['Correct First Attempt'].ravel(order='C')

# Student ID and Step ID will be our X
studentId = dataFile['Anon Student Id'].ravel(order='C')
stepName = dataFile['Step Name'].ravel(order='C')


# Generate label encoders
le_studentId = preprocessing.LabelEncoder()
le_stepName = preprocessing.LabelEncoder()

# Encode student id and step name values
encoded_studentId = le_studentId.fit_transform(studentId)
encoded_stepName = le_stepName.fit_transform(stepName)


# Plot input data points
# plt.scatter(cfa, encoded_studentId, marker='o', c='b', label='Training data')
plt.title("Profit With Respect to Population")
plt.xlabel("Population")
plt.ylabel("Profit")

# Plot the linear regression
# plt.plot(studentId, cfa, c='r', label='Current hypothesis')
plt.legend(loc=4)

# plt.show()

