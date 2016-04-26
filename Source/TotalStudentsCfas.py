
# Iman Rezaei
# TotalStudentsCfas.py
# 4/22/16


# Create a CSV file with unique students and their total CFAs


import numpy as np
import pandas as pd
import csv


# **************************************************************************

# import data file
dataFile = pd.read_csv("traindataFilteredByView20.csv", header=0)

studentId = dataFile["Anon Student Id"]
cfa = dataFile["Correct First Attempt"]
rowNum = dataFile["Row"]

uniqueStudentIdArray = []
totalCfas = [0]

# **************************************************************************

# Check if the current student us the same as the previous student
# Then check to see if there is a CFA
# if yes add it to the total CFA of the previous student.
# If the student is a new student add it to uniqueStudentIdArray
# and its CFA to totalCfas for that unique student
# Remember in Python array[-1] is the last element!

for i in range(len(studentId)):
    if cfa[i]:
        if studentId[i] == studentId[i - 1]:
            totalCfas[-1] = totalCfas[-1] + cfa[i]
            print("Student in row {:d} = student in row  {:d}".format(i, i - 1))

        else:
            uniqueStudentIdArray = np.append(uniqueStudentIdArray, studentId[i])
            totalCfas = np.append(totalCfas, cfa[i])
            print("New unique student in row {:d} added".format(i))


# **************************************************************************

with open('totalStudentCfas.csv', 'w') as csvfile:
    fieldnames = ['Row', 'Anon Student Id', 'Total Correct First Attempts']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(len(uniqueStudentIdArray)):
        writer.writerow(
            {'Row': rowNum[x], 'Anon Student Id': uniqueStudentIdArray[x],
             'Total Correct First Attempts': totalCfas[x]})


# **************************************************************************