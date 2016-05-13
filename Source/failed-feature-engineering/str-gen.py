'''
import string
import random
def id_generator(size=3, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))


a = id_generator()

print(a)
'''
import csv
import pandas as pd
import re
import numpy as np


data = pd.read_csv("traindata.csv",header = 0)
h = open('step_name.txt','w')

sn = data['Step Name']

ck = []

for item in sn:
	value = len(re.findall(r'([a-z])', item)) + len(re.findall(r'([A-Z])', item)) + item.count('+') \
	+ item.count('-') + 2*item.count('*') + 2*item.count('(') + 2*item.count('/') + item.count('.') \
	+ 3*item.count('^') + item.count('=') + len(re.findall(r'([0-9])', item))
	ck.append(value)
	g = str(value) + '\n'
	h.write(g)

print(len(set(ck)))
    





