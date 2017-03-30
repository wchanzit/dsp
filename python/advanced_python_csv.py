import numpy as np
import pandas as pd

# Read and format data (although this isn't all necessary here).
df = pd.read_csv('faculty.csv')

df.columns = ['name', 'degree', 'title', 'email']

df.degree = df.degree.str.replace('.','').str.strip()

df.title = df.title.str.replace(' is ',' of ')




# Write out result from part I, Q3 to a csv file.
df.email.to_csv('emails.csv')
