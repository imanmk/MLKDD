# Iman Rezaei
# StepNamesTotalCfas.py
# 4/22/16


# Create a CSV file with unique step names and their total CFAs


import numpy as np
import pandas as pd
import csv


# **************************************************************************

# import data file
dataFile = pd.read_csv("traindataNoDuration.csv", header=0)

stepName = dataFile["Step Name"]
cfa = dataFile["Correct First Attempt"]
rowNum = dataFile["Row"]

uniqueStepNameArray = []
totalCfas = [0]

# **************************************************************************

# Check to see if there is a CFA
# Then check if the current step name is existed in our uniqueStepNameArray
# if yes add it to the total CFA of the existed step name.
# If the step name is new add it to uniqueStepNameArray
# and its CFA to totalCfas for that unique step name
# Remember in Python array[-1] is the last element!

for i in range(len(stepName)):
    if cfa[i]:
        if stepName[i] in uniqueStepNameArray:
            uniqueStepNameList = uniqueStepNameArray.tolist()
            j = uniqueStepNameList.index(stepName[i])
            totalCfas[j] = totalCfas[j] + cfa[i]
            print("Step Name in row {:d} = Step Name in row  {:d}".format(i, j))

        else:
            uniqueStepNameArray = np.append(uniqueStepNameArray, stepName[i])
            totalCfas = np.append(totalCfas, cfa[i])
            print("New unique step name in row {:d} added".format(i))


# **************************************************************************

with open('stepNamesTotalCfas.csv', 'w') as csvfile:
    fieldnames = ['Row', 'Step Name', 'Total Correct First Attempts']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(len(uniqueStepNameArray)):
        writer.writerow(
            {'Row': rowNum[x], 'Step Name': uniqueStepNameArray[x],
             'Total Correct First Attempts': totalCfas[x]})


# **************************************************************************