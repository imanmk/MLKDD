
# KNN classifier with 3 features for KDD term project
# KNN_3_Features.py
# 5/17/16

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
dataFile = pd.read_csv("trainValid.csv", header=0)

# CFA is our Y
cfa = dataFile['Correct First Attempt'].ravel(order='C')

# Student ID and Step ID will be our X   (input for prediction)
studentId = dataFile['Anon Student Id'].ravel(order='C')
stepName = dataFile['Step Name'].ravel(order='C')
problemHierarchy = dataFile['Problem Hierarchy'].ravel(order='C')




# **************************************************************************

# Generate label encoders
le_studentId = preprocessing.LabelEncoder()
le_stepName = preprocessing.LabelEncoder()
le_problemHierarchy = preprocessing.LabelEncoder()

# Encode student id and step name values
encoded_studentId = le_studentId.fit_transform(studentId)
encoded_stepName = le_stepName.fit_transform(stepName)
encoded_problemHierarchy = le_problemHierarchy.fit_transform(problemHierarchy)

# **************************************************************************

# create dictionaries for encoded_studentId and encoded_stepName with keys being studentId & stepName


studentId_dict = dict(zip(studentId, encoded_studentId))
stepName_dict = dict(zip(stepName, encoded_stepName))
problemHierarchy_dict = dict(zip(problemHierarchy,encoded_problemHierarchy))

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
    x_array.append([encoded_studentId[i], encoded_stepName[i],encoded_problemHierarchy[i]])

# Convert x_array to np matrix
X = np.matrix(x_array)

# set Y (labels) to be our cfa
Y = cfa



# **************************************************************************

# KNN function:


# define a func as a wrapper for KNN.
# @param studentId, stepName
# @return prediction value

# looks up the keys for input from dict
# passes the values to KNN function

# num neighbors
k = 127

knn = neighbors.KNeighborsClassifier(n_neighbors=k, weights='distance', algorithm='auto',
                                     leaf_size=200)
knn.fit(X, Y)


# **************************************************************************

def predict_single_cfa(studentId, stepName,problemHierarchy):
    encoded_student_id = studentId_dict.get(studentId)
    print("encoded_student_id: ", encoded_student_id)
    encoded_step_name = stepName_dict.get(stepName)
    print("encoded_step_name: ", encoded_step_name)
    encoded_problemh = problemHierarchy_dict.get(problemHierarchy)
    print("encoded_problemHierarchy: ", encoded_problemh)
    prediction = knn.predict([[encoded_student_id, encoded_step_name, encoded_problemh]])
    print("prediction: ", prediction[0])




# Testing:
# predict_single_cfa("0BrbPbwCMz", "3(x+2) = 15")

# **************************************************************************




# get 2 arrays of encoded_studentId and encoded_stepName as inputs
# return prediction array and RMSE

def predict(encoded_studentId, encoded_stepName, encoded_problemh):

    prediction_array = np.array([])

    for row in range(len(encoded_studentId)):
        prediction = knn.predict_proba([[encoded_studentId[row], encoded_stepName[row],encoded_problemh[row]]])
        prediction_array = np.append(prediction_array, prediction[0, 1])
        print("Prediction for row {:d} = {:f}".format(row, prediction[0, 1]))

    print("prediction_array: ", prediction_array)

    return prediction_array


# **************************************************************************

#  calculate RMSE:

def calculate_rmse(prediction_array, ground_truth_array):
    rmse = math.sqrt(mean_squared_error(ground_truth_array, prediction_array))
    print("RMSE = ", rmse)
    num = 0
    for i in range(len(ground_truth_array)):
        if abs(ground_truth_array[i] - prediction_array[i]) > 0.3:
            num+=1
    print(num)

# **************************************************************************


def main():

    #testFileName = input("Please enter your test file name: ")
    testFile = pd.read_csv('test.csv', header=0)

    print("Loading... :) ")

    # CFA is our ground_truth
    ground_truth_array = testFile['Correct First Attempt'].ravel(order='C')

    # Student ID and Step ID will be our X   (input for prediction)
    test_studentId = testFile['Anon Student Id'].ravel(order='C')
    test_stepName = testFile['Step Name'].ravel(order='C')
    test_problemHierarchy = testFile['Problem Hierarchy'].ravel(order='C')
    test_row = testFile['Row'].ravel(order='C')
    # Generate label encoders
    le_test_studentId = preprocessing.LabelEncoder()
    le_test_stepName = preprocessing.LabelEncoder()
    le_test_problemHierarchy = preprocessing.LabelEncoder()

    # Encode student id and step name values
    encoded_test_studentId = le_test_studentId.fit_transform(test_studentId)
    encoded_test_stepName = le_test_stepName.fit_transform(test_stepName)
    encoded_test_problemHierarchy = le_test_problemHierarchy.fit_transform(test_problemHierarchy)

    prediction_array = predict(encoded_test_studentId, encoded_test_stepName, encoded_problemHierarchy)

    calculate_rmse(prediction_array, ground_truth_array)


    # Save results in a CSV:

    with open('knn_3_features_k127.csv', 'w') as csvfile:
        fieldnames = ['Row', 'Student ID', 'Correct First Attempt', 'Ground Truth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(test_studentId)):
            writer.writerow(
                {'Row': test_row[x], 'Student ID': test_studentId[x], 'Correct First Attempt': prediction_array[x],
                'Ground Truth': ground_truth_array[x]})

# **************************************************************************

if __name__ == '__main__':
    main()

print("K = ", k)
print("KNN Classifier with 3 Features")
print("--- Total time: %s seconds ---" % (time.time() - start_time))

