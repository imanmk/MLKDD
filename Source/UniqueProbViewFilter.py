
# Iman Rezaei
# UniqueProbViewFilter
# 4/25/16

# Produce a CSV with unique problems that have total views < 20

import csv
import time

# **************************************************************************

start_time = time.time()

viewThreshold = 20
problemViewColumnIndex = 2


# **************************************************************************


with open('uniqueProbsTotalViews_v2.csv', 'r') as inp, open('filteredProbByView20.csv', 'w') as out:
    writer = csv.writer(out)
    i = 0
    for row in csv.reader(inp):
        # firstRow
        if i == 0:
            writer.writerow(row)
            i = i + 1
        else:
            i = i + 1
            print(i)
            totalView = row[problemViewColumnIndex]
            if not totalView:
                continue
            if float(totalView) < viewThreshold:
                writer.writerow(row)

# **************************************************************************

print("--- %s seconds ---" % (time.time() - start_time))

# **************************************************************************