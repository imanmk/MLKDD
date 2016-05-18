import csv
import pandas as pd
import re
import numpy as np

h = open('step_name_string.txt','w')

'''
This file is used for string type feature mapping into float
And also we have to take "scale" into consideration when we do the mapping
based on the amout
'''
# **************************
# following is fetching data
# **************************

data = pd.read_csv("smallsizetestdata.csv",header = 0)
student_id = data['Anon Student Id']
problem_hierarchy = data['Problem Hierarchy']
problem_name = data['Problem Name']
step_name = data['Step Name']
correct_first_attempt = data['Correct First Attempt']



# if the equation is like x-1 = x + 2 ,this will be TWO variables rather than one
# the result is already scaled by x- mean/ range/4, (-2,2)

step_name_list=[]

for item in step_name:
    num = ((len(re.findall(r'([a-z])', item)) + len(re.findall(r'([A-Z])', item))) - 7.5) / (14/4)
    step_name_list.append(num)
    o = str(num) + '\n'
    h.write(o)
    #print(t)    

print(step_name_list)
#print(amount)


if __name__ == '__main__':
    1
