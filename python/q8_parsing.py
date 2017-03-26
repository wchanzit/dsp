# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

df = pd.read_csv('football.csv')

df['Goal_Diff'] = df['Goals'] - df['Goals Allowed']

min_goal_diff = df.Goal_Diff.abs() == df.Goal_Diff.abs().min()

print(df[min_goal_diff])

