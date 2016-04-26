# Iman Rezaei
# UniqueProbsTotalViews.py
# 4/24/16


# Create a CSV file with unique problems, their total Views and total CFA's
# for all steps in this problem.




import numpy as np
import pandas as pd
import csv
import time

# **************************************************************************

start_time = time.time()

def main():

    # import data file
    dataFile = pd.read_csv("traindataFilteredByView20.csv", header=0)

    problemHierarchy = dataFile["Problem Hierarchy"]
    stepName = dataFile["Step Name"]
    problemName = dataFile["Problem Name"]
    problemView = dataFile["Problem View"]
    studentId = dataFile["Anon Student Id"]
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

        if problemHierarchy[i] + ";" + problemName[i] in uniqueProblems:

            uniqueProblemsList = uniqueProblems.tolist()
            j = uniqueProblemsList.index(problemHierarchy[i] + ";" + problemName[i])
            totalCfas[j] = totalCfas[j] + cfa[i]
            # if its the same student
            if studentId[i] == studentId[i - 1]:
                # if its not the same prob view count as the previous row
                if problemView[i] != problemView[i - 1]:
                    totalProblemViews[j] = totalProblemViews[j] + 1
                print("Problem in row {:d} = Problem in row  {:d}".format(i, j))

            else:
                totalProblemViews[j] = totalProblemViews[j] + problemView[i]

        else:
            uniqueProblems = np.append(uniqueProblems, problemHierarchy[i]
                                              + ";" + problemName[i])
            totalCfas = np.append(totalCfas, cfa[i])
            totalProblemViews = np.append(totalProblemViews, problemView[i])
            print("New unique problem & prob view in row {:d} added".format(i))


    # **************************************************************************

    with open('uniqueProbsTotalViews.csv', 'w') as csvfile:
        fieldnames = ['Row', 'Unique Problem', 'Problem View']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(uniqueProblems)):
            writer.writerow(
                {'Row': rowNum[x], 'Unique Problem': uniqueProblems[x],
                 'Problem View': totalProblemViews[x]})



    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()

# **************************************************************************