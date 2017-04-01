import numpy as np
import pandas as pd

import sys
directory = '/Users/warren/Data_Science/metis/github/prework/dsp/python/'
sys.path.append(directory)

# Read and format data
df = pd.read_csv(directory + 'faculty.csv')

df.columns = ['name', 'degree', 'title', 'email']

df.degree = df.degree.str.replace('.','').str.strip()

df.title = df.title.str.replace(' is ',' of ')


# Q1
degs = []

for deg in df.degree.unique():
    deg = deg.split()
    
    for d in deg:
        if d not in degs:
            degs.append(d)

degs2 = dict(zip(degs, [0]*len(degs)))

for deg in df.degree:
    for key in degs2.keys():
        if key in deg:
            degs2[key] += 1


# Q2
df.groupby('title')['name'].count()


# Q3
sorted(list(df.email))


# Q4
df['domain'] = df['email'].apply(lambda x: x[(x.find('@')+1):])

sorted(list(df['domain'].unique()))


