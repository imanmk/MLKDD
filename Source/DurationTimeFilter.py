import csv
with open('traindata.csv', 'r') as inp, open('traindataNoDuration.csv', 'w') as out:
    writer = csv.writer(out)
    i=0;
    for row in csv.reader(inp):
        #firstRow
        if i==0:
            writer.writerow(row)
            i=i+1
        else:
            i=i+1
            print(i)
            s = row[10]
            if not s:
                continue
            if float(s) <= 125:
                writer.writerow(row)