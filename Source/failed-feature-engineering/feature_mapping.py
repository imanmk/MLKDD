import csv
import pandas as pd
import re
import numpy as np
from time import time

t = time()
'''
This file is used for string type feature mapping into float
And also we have to take "scale" into consideration when we do the mapping
based on the amout
'''
# **************************
# following is fetching data
# **************************

data = pd.read_csv("rddata.csv",header = 0)
student_id = data['Anon Student Id']
problem_hierarchy = data['Problem Hierarchy']
problem_name = data['Problem Name']
step_name = data['Step Name']
correct_first_attempt = data['Correct First Attempt']

problem_name_feature = list(set(problem_name))
print(len(problem_name_feature))
#result 1084
#print(problem_name_feature)

problem_name_feature = dict.fromkeys(problem_name_feature,True)

# So far I will just keep original form ,rather than split them
#problem_hierarchy_feature = set(problem_hierarchy)

problem_hierarchy_feature = list(set(problem_hierarchy))
#print(len(problem_hierarchy_feature))
#result 138


step_name_feature = list(set(step_name))
#print(len(step_name_feature))
#result 174655

# append different column can 'create' different features
# In order to scale the feature into (-2,2), use the method (x-mean.x)/ (range/4)

constant_problem_name_feature = []

for i in range(1,896):
    cpn = (i-37/2)/ (37/4)
    constant_problem_name_feature.append(cpn)

#print(constant_problem_name_feature)
#print(len(constant_problem_name_feature))

problem_name_mapping = list(problem_name)


# after this loop ,the string will be replaced by float.
# It takes round 170s to execute.
# Because it should do the calculation round 0.8m * 1k times.
# I am looking for a better algorithm or existing sitepackage
'''
for i,item in enumerate(problem_name_mapping):
    for j,item in enumerate(problem_name_feature):
        if problem_name_mapping[i] == problem_name_feature[j]:
            problem_name_mapping[i] = constant_problem_name_feature[j]

#print(problem_name_mapping)
'''

constant_problem_hierarchy_feature = []

for i in range(1,139):
	cph = (1 - 139/2) / (139/4)
	constant_problem_hierarchy_feature.append(cph)

problem_hierarchy_mapping = list(problem_hierarchy)


# not sure how to deal with "step_name_feature"


# *********************
# following is function
# *********************

def mapping(columnname,column_feature,column_constant):
	for i,item in enumerate(columnname):
		for j,item in enumerate(column_feature):
			if columnname[i] == column_feature[j]:
				columnname[i] = column_constant[j]


mapping(problem_name_mapping,problem_name_feature,constant_problem_name_feature)
#print(problem_name_mapping)

h = open('1.txt','w')
for item in problem_name_mapping:
    o = str(item) + '\n'
    h.write(o)

print(time()-t)



# ************
# ****Main****
# ************

if __name__ == '__main__':
    1
