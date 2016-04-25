
# Iman Rezaei
# traindataFilteredByView.py
# 4/25/16

# Filter traindataNoDuration. Get rid of the
# unique problems that are also in the given input CSV file.


import numpy as np
import pandas as pd
import csv
import time


# **************************************************************************

start_time = time.time()


def main():

    # import data file
    dataFile = pd.read_csv("filteredProbByView20.csv", header=0)

    uniqueProblems = dataFile["Unique Problem"].tolist()

    problemHierarchyColumnIndex = 2
    problemNameColumnIndex = 3

    #print(uniqueProblems)
    # **************************************************************************

    with open('traindataNoDuration.csv', 'r') as inp, open('traindataFilteredByView20.csv', 'w') as out:
        writer = csv.writer(out)
        i = 0
        for row in csv.reader(inp):
            # firstRow
            if i == 0:
                writer.writerow(row)
                i = i + 1
            else:
                i = i + 1
                # print("Row number = ", i)
                problemHierarchy = row[problemHierarchyColumnIndex]
                problemName = row[problemNameColumnIndex]

                uniqueProb = problemHierarchy + ";" + problemName


                if uniqueProb not in uniqueProblems:
                    writer.writerow(row)
                    print("unique prob wrote into csv")
                    print("Current row = ", i)
                else:
                    print("prob is in uniqueProblems")

    # **************************************************************************

    print("--- %s seconds ---" % (time.time() - start_time))

# **************************************************************************

if __name__ == '__main__':
    main()