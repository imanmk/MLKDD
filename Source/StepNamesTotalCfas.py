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
problemName = dataFile["Problem Name"]
problemView = dataFile["Problem View"]
cfa = dataFile["Correct First Attempt"]

rowNum = dataFile["Row"]

uniqueProblemStepName = []
totalProblemViews = [0]
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
        if problemName[i] + ";" + stepName[i] in uniqueProblemStepName:
            uniqueProblemStepNameList = uniqueProblemStepName.tolist()
            j = uniqueProblemStepNameList.index(problemName[i] + ";" + stepName[i])
            totalCfas[j] = totalCfas[j] + cfa[i]
            if problemView[i]:
                totalProblemViews[j] = totalProblemViews[j] + problemView[i]
            print("Prob Step Name in row {:d} = Prob Step Name in row  {:d}".format(i, j))

        else:
            uniqueProblemStepName = np.append(uniqueProblemStepName, problemName[i]
                                              + ";" + stepName[i])
            totalCfas = np.append(totalCfas, cfa[i])
            totalProblemViews = np.append(totalProblemViews, problemView[i])
            print("New unique step name & prob view in row {:d} added".format(i))


# **************************************************************************

with open('problemStepNamesTotalCfas.csv', 'w') as csvfile:
    fieldnames = ['Row', 'Problem Name', 'Step Name', 'Problem View', 'Total Correct First Attempts']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(len(uniqueProblemStepName)):
        writer.writerow(
            {'Row': rowNum[x], 'Problem Name': uniqueProblemStepName[x].split(";")[0],
             'Step Name': uniqueProblemStepName[x].split(";")[1],
             'Problem View': totalProblemViews[x], 'Total Correct First Attempts': totalCfas[x]})


# **************************************************************************