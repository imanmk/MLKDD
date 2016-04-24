# Iman Rezaei
# UniqueProbsTotalViews.py
# 4/24/16


# Create a CSV file with unique problems, their total Views and total CFA's
# for all steps in this problem.




import numpy as np
import pandas as pd
import csv


# **************************************************************************

# import data file
dataFile = pd.read_csv("traindataNoDuration.csv", header=0)

problemHierarchy = dataFile["Problem Hierarchy"]
stepName = dataFile["Step Name"]
problemName = dataFile["Problem Name"]
problemView = dataFile["Problem View"]
cfa = dataFile["Correct First Attempt"]

rowNum = dataFile["Row"]

uniqueProblems = []
totalProblemViews = [0]
totalCfas = [0]



# **************************************************************************

# Check to see if there is a CFA
# Then check if the current step name is existed in our uniqueProblems
# if yes add it to the total CFA of the existed step name.
# If the step name is new add it to uniqueProblems
# and its CFA to totalCfas for that unique step name
# Remember in Python array[-1] is the last element!

for i in range(len(problemName)):
    if cfa[i]:
        if problemHierarchy[i] + ";" + problemName[i] in uniqueProblems:
            uniqueProblemsList = uniqueProblems.tolist()
            j = uniqueProblemsList.index(problemHierarchy[i] + ";" + problemName[i])
            totalCfas[j] = totalCfas[j] + cfa[i]
            if problemView[i]:
                totalProblemViews[j] = totalProblemViews[j] + problemView[i]
            print("Problem in row {:d} = Problem in row  {:d}".format(i, j))

        else:
            uniqueProblems = np.append(uniqueProblems, problemHierarchy[i]
                                              + ";" + problemName[i])
            totalCfas = np.append(totalCfas, cfa[i])
            totalProblemViews = np.append(totalProblemViews, problemView[i])
            print("New unique problem & prob view in row {:d} added".format(i))


# **************************************************************************

with open('uniqueProbsTotalViews.csv', 'w') as csvfile:
    fieldnames = ['Row', 'Problem Hierarchy', 'Problem Name', 'Problem View', 'Total CFAs for Steps in this Problem']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(len(uniqueProblems)):
        writer.writerow(
            {'Row': rowNum[x], 'Problem Hierarchy': uniqueProblems[x].split(";")[0],
             'Problem Name': uniqueProblems[x].split(";")[1],
             'Problem View': totalProblemViews[x], 'Total Correct First Attempts': totalCfas[x]})


# **************************************************************************