import csv
import pandas as pd
import re
import numpy as np
import pprint
from pyfm import pylibfm
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
import copy
import csv
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


dataIn = pd.read_csv("traindata.csv",header = 0)
row_Num = dataIn['Row']
student_id = dataIn['Anon Student Id']
problem_hierarchy = dataIn['Problem Hierarchy']
problem_name = dataIn['Problem Name']
step_name = dataIn['Step Name']
correct_first_attempt = dataIn['Correct First Attempt']


numOfLines = len(student_id)
step_full_name = []
for i in range(numOfLines):
    s = problem_hierarchy[i] + '/'+ problem_name[i] + '/'+ step_name[i]
    step_full_name.append(s)

print("number of training")
print(len(student_id))
print(len(step_full_name))
print(len(correct_first_attempt))
print(numOfLines)






dataIn2 = pd.read_csv("test.csv",header = 0)
row_Num2 = dataIn2['Row']
student_id2 = dataIn2['Anon Student Id']
problem_hierarchy2 = dataIn2['Problem Hierarchy']
problem_name2 = dataIn2['Problem Name']
step_name2 = dataIn2['Step Name']
correct_first_attempt2 = dataIn2['Correct First Attempt']

numOfLines2 = len(student_id2)
step_full_name2 = []
for i in range(numOfLines2):
    s = problem_hierarchy2[i] + '/'+ problem_name2[i] + '/'+ step_name2[i]
    step_full_name2.append(s)


print("number of testing")
print(len(student_id2))
print(len(step_full_name2))
print(len(correct_first_attempt2))
print(numOfLines2)



def runsvd():
    data = []
    y = []
    students=set()
    steps=set()

    #training input data
    for i in range(0, numOfLines):
        data.append({"student_id": str(student_id[i]), "step_id": str(step_full_name[i])})
        y.append(int(correct_first_attempt[i]))
        #students.add(student_id[i])
        #steps.add(step_full_name[i])

    #training output data
    data2 = []
    y2 = []
    for i in range(0, numOfLines2):
        data2.append({"student_id": str(student_id2[i]), "step_id": str(step_full_name2[i])})
        y2.append(int(correct_first_attempt2[i]))
    test_data = data2
    y_test = np.array(y2)





    train_data = data
    y_train = np.array(y)


    print(len(train_data))
    print(len(y_train))
    train_data_same = copy.copy(train_data)

    v = DictVectorizer()
    X_train = v.fit_transform(train_data)
    #so far N=40 is good, iter=55
    fm = pylibfm.FM(num_factors=40, num_iter=55, verbose=True, task="classification", initial_learning_rate=0.2, learning_rate_schedule="optimal")
    fm.fit(X_train, y_train)


    # Evaluate
    train_data_same = v.transform(train_data_same)
    test_data = v.transform(test_data)
    preds = fm.predict(test_data)
    #print(y_train)
    #print(preds)
    with open('FactorizationMachineResult.csv', 'w') as csvfile:
        fieldnames = ['Row', 'Student ID', 'Correct First Attempt', 'real y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(numOfLines2):
            writer.writerow({'Row': row_Num2[x], 'Student ID': student_id2[x] ,'Correct First Attempt': preds[x], 'real y': y_test[x]})



    #print("FM MSE: %.4f" % mean_squared_error(y_train,preds))
    rmse = mean_squared_error(y_test, preds)**0.5
    print("RMSE: %.4f" % rmse)
    return


for x in range(1):
    runsvd()

#plt.plot()
#plt.ylabel('some numbers')
#plt.show()