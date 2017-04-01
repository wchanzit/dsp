import pandas as pd

import sys
directory = '/Users/warren/Data_Science/metis/github/prework/dsp/python/'
sys.path.append(directory)

# Read and format data
df = pd.read_csv(directory + 'faculty.csv')

df.columns = ['name', 'degree', 'title', 'email']

df.degree = df.degree.str.replace('.','').str.strip()

df.title = df.title.str.replace(' is ',' of ')


# Q6
def make_list(n):
    return [list(df[df['name'] == nombre][['degree', 'title', 'email']].iloc[0])
            for nombre in df['name'] if n in nombre]

surnames = df['name'].apply(lambda x: x[(x.rfind(' ')+1):])

faculty_dict = {surname: make_list(surname) for surname in surnames}

list(faculty_dict.items())[:3]


# Q7
def full_name(n):
    if n.count(' ') == 1:
        pos = n.find(' ')
        return (n[(pos+1):], n[:pos])
    else:
        pos1 = n.find(' ')
        pos2 = n.rfind(' ')
        return (n[(pos2+1):], n[:pos1])

professor_dict = {full_name(name): list(df[df['name'] == name][['degree', 'title', 'email']].iloc[0])
for name in df['name']}

list(professor_dict.items())[:3]
#professor_dict[('Bellamy', 'Scarlett')]


# Q8 ...not applicable?