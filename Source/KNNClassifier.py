
# Iman Rezaei
# KNN classifier for KDD term project - Phase 2
# KNNClassifier.py
# 4/27/16


import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn import preprocessing, datasets
from sklearn.metrics import mean_squared_error
import math
import csv
import time

# **************************************************************************

start_time = time.time()

print("Welcome to KDD KNN Classifier! :) ")

# import data file
dataFile = pd.read_csv("train.csv", header=0)

# CFA is our Y
cfa = dataFile['Correct First Attempt'].ravel(order='C')

# Student ID and Step ID will be our X   (input for prediction)
studentId = dataFile['Anon Student Id'].ravel(order='C')
stepName = dataFile['Step Name'].ravel(order='C')

# **************************************************************************

# Generate label encoders
le_studentId = preprocessing.LabelEncoder()
le_stepName = preprocessing.LabelEncoder()

# Encode student id and step name values
encoded_studentId = le_studentId.fit_transform(studentId)
encoded_stepName = le_stepName.fit_transform(stepName)

# **************************************************************************

# create dictionaries for encoded_studentId and encoded_stepName with keys being studentId & stepName


studentId_dict = dict(zip(studentId, encoded_studentId))
stepName_dict = dict(zip(stepName, encoded_stepName))

# print("studentId_dict: ", studentId_dict)
# print("stepName_dict: ", stepName_dict)


# **************************************************************************


# we need a matrix like this for our X in fit():
# [ [6  103432]
#   [6  162908]
#   [6  93298]
#    ... ]
# each row consists of an element from encoded_studentId and one element from encoded_stepName.
# dimensions = 809694 x 2



x_array = []

for i in range(len(encoded_studentId)):
    x_array.append([encoded_studentId[i], encoded_stepName[i]])

# Convert x_array to np matrix
X = np.matrix(x_array)

# set Y (labels) to be our cfa
Y = cfa




# **************************************************************************

# # Testing:
# print("CFA: ", cfa)
# print("encoded_stepName: ", encoded_stepName)
# print("encoded_studentId:, ", encoded_studentId)
# print(le_studentId.inverse_transform([encoded_studentId[2]]))

# **************************************************************************


# # Testing:
# print(len(encoded_studentId))
# print(len(encoded_stepName))


# **************************************************************************

# print("X: ", X)
# print("X Shape: ", X.shape)
# print("Y: ", Y)
# print("Y Shape: ", Y.shape)

# Sample dataset to do experiments with:
# iris = datasets.load_iris()
# print("iris target: ", iris.target)
# print("iris data: ", iris.data)


# **************************************************************************

# KNN function:


# define a func as a wrapper for KNN.
# @param studentId, stepName
# @return prediction value

# looks up the keys for input from dict
# passes the values to KNN function

knn = neighbors.KNeighborsClassifier(n_neighbors=41, weights='distance', algorithm='auto')
knn.fit(X, Y)


# **************************************************************************

def predict_single_cfa(studentId, stepName):
    encoded_student_id = studentId_dict.get(studentId)
    print("encoded_student_id: ", encoded_student_id)
    encoded_step_name = stepName_dict.get(stepName)
    print("encoded_step_name: ", encoded_step_name)
    prediction = knn.predict([[encoded_student_id, encoded_step_name]])
    print("prediction: ", prediction[0])




# Testing:
# predict_single_cfa("0BrbPbwCMz", "3(x+2) = 15")

# **************************************************************************




# get 2 arrays of encoded_studentId and encoded_stepName as inputs
# return prediction array and RMSE

def predict(encoded_studentId, encoded_stepName):

    prediction_array = np.array([])

    for row in range(len(encoded_studentId)):
        prediction = knn.predict_proba([[encoded_studentId[row], encoded_stepName[row]]])
        prediction_array = np.append(prediction_array, prediction[0, 1])
        print("Prediction for row {:d} = {:f}".format(row, prediction[0, 1]))

    print("prediction_array: ", prediction_array)

    return prediction_array


# **************************************************************************

#  calculate RMSE:

def calculate_rmse(prediction_array, ground_truth_array):
    rmse = math.sqrt(mean_squared_error(ground_truth_array, prediction_array))
    print("RMSE = ", rmse)

# **************************************************************************


def main():

    testFileName = input("Please enter your test file name: ")
    testFile = pd.read_csv(testFileName, header=0)

    print("Loading... :) ")

    # CFA is our ground_truth
    ground_truth_array = testFile['Correct First Attempt'].ravel(order='C')

    # Student ID and Step ID will be our X   (input for prediction)
    test_studentId = testFile['Anon Student Id'].ravel(order='C')
    test_stepName = testFile['Step Name'].ravel(order='C')
    test_row = testFile['Row'].ravel(order='C')
    # Generate label encoders
    le_test_studentId = preprocessing.LabelEncoder()
    le_test_stepName = preprocessing.LabelEncoder()

    # Encode student id and step name values
    encoded_test_studentId = le_test_studentId.fit_transform(test_studentId)
    encoded_test_stepName = le_test_stepName.fit_transform(test_stepName)

    prediction_array = predict(encoded_test_studentId, encoded_test_stepName)

    calculate_rmse(prediction_array, ground_truth_array)

    # Save results in a CSV:

    # with open('test_result_k107.csv', 'w') as csvfile:
    #     fieldnames = ['Row', 'Student ID', 'Correct First Attempt', 'Ground Truth']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for x in range(len(test_studentId)):
    #         writer.writerow(
    #             {'Row': test_row[x], 'Student ID': test_studentId[x], 'Correct First Attempt': prediction_array[x],
    #             'Ground Truth': ground_truth_array[x]})

# **************************************************************************

if __name__ == '__main__':
    main()


print("--- Total time: %s seconds ---" % (time.time() - start_time))

# **************************************************************************

# Leaderboard:




# 1) k = , weight = distance : RMSE =  0.2998780623475022  in ~ 2 mins
# 2) k = 41, weight = distance : RMSE =  0.29987957958841266



# 3) k = 127, weight = distance : RMSE =  0.2999427984559147 in ~ 20 mins
# 4) k = 101, weight = distance : RMSE =  0.30005410539677935
# 5) k = 77, weight = distance : RMSE =  0.3002922082536437 in ~ 12 mins      ***
# 6) k = 41, weight = distance : RMSE =  0.3016025310594197      ***
# 7) k = 22, weight = distance : RMSE =  0.3042848486883858 in ~ 12 mins
# 8) k = 11, weight = distance : RMSE =  0.3105935693719608
# 9) k = 5, weight = distance : RMSE =  0.32554845858234405
# 10) k = 11, weight = uniform : RMSE =  0.3832467437542604
# 11) k = 5, weight = uniform : RMSE =  0.3845757273240957
# 12) k = 22, weight = uniform : RMSE =  0.38497311222482195
# 13) k = 41, weight = uniform : RMSE =  0.388534928948569
# 14) k = 77, weight = uniform : RMSE =  0.39263912353244396
# 15) k = 101, weight = uniform : RMSE =  0.39454656356815926








# **************************************************************************



