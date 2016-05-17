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


# **************************************************************************


def predict(encoded_studentId, encoded_stepName, encoded_problemh):

    prediction_array = np.array([])

    for row in range(len(encoded_studentId)):
        prediction = knn.predict_proba([[encoded_studentId[row], encoded_stepName[row],encoded_problemh[row]]])
        prediction_array = np.append(prediction_array, prediction[0, 1])
        #print("Prediction for row {:d} = {:f}".format(row, prediction[0, 1]))

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
    print("num =",num)

def predict_single_cfa(studentId, stepName,problemh):
    encoded_student_id = studentId_dict.get(studentId)
    print("encoded_student_id: ", encoded_student_id)
    encoded_step_name = stepName_dict.get(stepName)
    print("encoded_step_name: ", encoded_step_name)
    encoded_problemh = problemh_dict.get(problemh)
    print("encoded_problemh: ", encoded_problemh)
    prediction = knn.predict([[encoded_student_id, encoded_step_name], encoded_problemh])
    print("prediction: ", prediction[0])



testFile = pd.read_csv('20kk.csv', header=0)

print("Loading... :) ")

# CFA is our ground_truth
ground_truth_array = testFile['Correct First Attempt'].ravel(order='C')

# Student ID and Step ID will be our X   (input for prediction)
test_studentId = testFile['Anon Student Id'].ravel(order='C')
test_stepName = testFile['Step Name'].ravel(order='C')
test_problemh = testFile['Problem Hierarchy'].ravel(order='C')
test_row = testFile['Row'].ravel(order='C')
# Generate label encoders
le_test_studentId = preprocessing.LabelEncoder()
le_test_stepName = preprocessing.LabelEncoder()
le_test_problemh = preprocessing.LabelEncoder()

# Encode student id and step name values
encoded_test_studentId = le_test_studentId.fit_transform(test_studentId)
encoded_test_stepName = le_test_stepName.fit_transform(test_stepName)
encoded_test_problemh = le_test_problemh.fit_transform(test_problemh)


df1 = pd.read_csv("100k.csv", header=0)
#dataFile = pd.concat([df1,testFile], ignore_index=True)
dataFile = df1.append(testFile)

# CFA is our Y
cfa = dataFile['Correct First Attempt'].ravel(order='C')

# Student ID and Step ID will be our X   (input for prediction)
studentId = dataFile['Anon Student Id'].ravel(order='C')
stepName = dataFile['Step Name'].ravel(order='C')
problemh= dataFile['Problem Hierarchy'].ravel(order='C')
# **************************************************************************

# Generate label encoders
le_studentId = preprocessing.LabelEncoder()
le_stepName = preprocessing.LabelEncoder()
le_problemh = preprocessing.LabelEncoder()

# Encode student id and step name values
encoded_studentId = le_studentId.fit_transform(studentId)
encoded_stepName = le_stepName.fit_transform(stepName)
encoded_problemh = le_problemh.fit_transform(problemh)

# **************************************************************************

# create dictionaries for encoded_studentId and encoded_stepName with keys being studentId & stepName


studentId_dict = dict(zip(studentId, encoded_studentId))
stepName_dict = dict(zip(stepName, encoded_stepName))
problemh_dict = dict(zip(problemh,encoded_problemh))



# we need a matrix like this for our X in fit():
# [ [6  103432]
#   [6  162908]
#   [6  93298]
#    ... ]
# each row consists of an element from encoded_studentId and one element from encoded_stepName.
# dimensions = 809694 x 2



x_array = []

for i in range(len(encoded_studentId)):
    x_array.append([encoded_studentId[i], encoded_stepName[i],encoded_problemh[i]])

# Convert x_array to np matrix
X = np.matrix(x_array)

# set Y (labels) to be our cfa
Y = cfa



knn = neighbors.KNeighborsClassifier(n_neighbors=131, weights='distance', algorithm='auto')
knn.fit(X, Y)

prediction_array = predict(encoded_test_studentId, encoded_test_stepName, encoded_problemh)

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



print("--- Total time: %s seconds ---" % (time.time() - start_time))


