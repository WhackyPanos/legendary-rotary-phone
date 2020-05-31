import pandas as pd

# Import data
Data = pd.read_excel(r'fixedPointAlts.xlsx', index_col=0)

# Convert point column to list
Points = Data['points'].tolist()

# Calculate total points
total = 0
for point in Points:
    total += point

# Normalize points
Weight = []
for point in Points:
    Weight.append(point / total)

# TODO make it more pretty
print(Weight)
