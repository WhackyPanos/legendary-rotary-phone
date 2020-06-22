import pandas as pd
import xlwt
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

# TODO make it more pretty
print(Alts)
print(Weight)

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

# Save weights to Excel
wb = xlwt.Workbook()
ws = wb.add_sheet('Weights')
for i in range(0,len(Weight)-1):
    ws.write(i,Weight[i])


wb.save('output.xls')