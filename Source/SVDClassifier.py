import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
import time

def main():
    start_time = time.time()

    # import data file
    print('Importing data file...')
    df = pd.read_csv('../CSV/train.csv')
    row_Num = df['Row']
    student_id = df['Anon Student Id']
    problem_hierarchy = df['Problem Hierarchy']
    problem_name = df['Problem Name']
    step_name = df['Step Name']
    correct_first_attempt = df['Correct First Attempt']

    numOfLines = len(student_id)

    # generate full step names​
    print('Generating full step names...')
    step_full_name = []
    for i in range(numOfLines):
        s = problem_hierarchy[i] + '/' + problem_name[i] + '/' + step_name[i]
        step_full_name.append(s)

    train_data = []
    y = []
    students=set()
    steps=set()

    print('Building dictionary...')
    for i in range(0, numOfLines):
        train_data.append({'student_id': str(student_id[i]), 'step_id': str(step_full_name[i])})
        y.append(int(correct_first_attempt[i]))
        students.add(student_id[i])
        steps.add(step_full_name[i])

    # Convert train_data to matrix
    print('Converting dictionary to matrix...')
    v = DictVectorizer()
    X = v.fit_transform(train_data)

    # set Y (labels) to be our cfa
    Y = correct_first_attempt

    # train the SVD model
    print('Training the TruncatedSVD model...')
    svd = TruncatedSVD() # use default parameters
    svd.fit(X, Y)

    print('\n\n\n')
    # show svd attributes
    print('Components:')
    print(svd.components_)

    print('SVD explained variance ratio:')
    print(svd.explained_variance_ratio_)

    print('SVD EVR Sum:')
    print(svd.explained_variance_ratio_.sum())

    # test the model
    #print('Testing SVD with test.csv...')
    #test_data = pd.read_csv('../CSV/test.csv')

    # calculate RMSE


    print("--- Total time: %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
