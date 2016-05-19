import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
import pandas as pd
import csv


fm1 = pd.read_csv("FactorizationMachineResult2.csv",header = 0)
knn1 = pd.read_csv("knn_3_features_k127.csv",header = 0)
knn2 = pd.read_csv("knn_2_features_k723.csv",header = 0)
knn3 = pd.read_csv("knn_4_features_k1001.csv",header = 0)
s = 'Correct First Attempt'

#predicted result from different models as features
result1 = fm1[s]
result2 = knn1[s]
result3 = knn2[s]
result4 = knn3[s]
#real y as ground truth
real_y = fm1['real y']


row_Num = fm1['Row']
student_id = fm1['Student ID']
Y = np.array(real_y)
numOfLines = len(result1)

X = np.column_stack((result1, result2, result3, result4))



logreg = linear_model.LogisticRegression()
#training
logreg.fit(X, Y)



print(logreg.intercept_)
print(logreg.coef_)
#predicts
predited_prob = logreg.predict_proba(X)
#choose the prob of being 1
predicted_prob_for_1 = predited_prob[:,1]
from sklearn.metrics import mean_squared_error
#print("FM MSE: %.4f" % mean_squared_error(y_train,preds))
rmse = mean_squared_error(predicted_prob_for_1,Y)**0.5
print("RMSE: %.4f" % rmse)


with open('FinalResult.csv', 'w') as csvfile:
    fieldnames = ['Row', 'Student ID', 'Correct First Attempt', 'real y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(numOfLines):
        writer.writerow({'Row': row_Num[x], 'Student ID': student_id[x], 'Correct First Attempt': predicted_prob_for_1[x], 'real y': Y[x]})