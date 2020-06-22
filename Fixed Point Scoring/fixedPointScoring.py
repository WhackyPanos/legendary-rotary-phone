import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Import data
Data = pd.read_excel(r'fixedPointAlts.xlsx', index_col=0)

# Convert point column to list, save alt names to list
Points = Data['points'].tolist()
Alts = Data.index.tolist()

# Calculate total points
total = 0
for point in Points:
    total += point

# Normalize points
Weight = []
for point in Points:
    Weight.append(point / total)

# Plot results
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.barh(Alts,Weight)
ax.set_ylabel('Alternatives')
ax.set_xlabel('Weights')

# Get date+time for filename
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%m-%Y_%H:%M:%S")

# Save to png
plt.savefig('plot_' + timestampStr + '.png',bbox_inches='tight')

# Save weights to Excel && print results
print(pd.DataFrame(Weight,Alts))
pd.DataFrame(Weight,Alts).to_excel("output_" + timestampStr + '.xlsx', header=False)
