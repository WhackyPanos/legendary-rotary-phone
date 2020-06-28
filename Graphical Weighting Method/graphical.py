import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# import data
Data = pd.read_excel(r'graphicalWeightingData.xlsx', index_col=False)
Criteria = Data.iloc[:,0].tolist()

# read graphical weights
Values = []
for criterion in Criteria:
    print("\n\nDraw with '=' the value of "+ criterion+":")
    if not Values == []:
        print("Previous criteria:")
    for i in range(len(Values)):
        print("\n"+Criteria[i] + ": ", end = '')
        for j in range(Values[i]):
            print("=", end = '')

    temp = input("\n"+criterion + ": ")
    Values.append(len(temp))

# Normalize weights
total =0
for value in Values:
    total += value

Weights =[]
for value in Values:
    Weights.append(value/total)

# Plot results
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.barh(Criteria,Weights)
ax.set_ylabel('Criteria')
ax.set_xlabel('Weights')

# Get date+time for filename
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%m-%Y_%H:%M:%S")

# Save to png
plt.savefig('plot_' + timestampStr + '.png',bbox_inches='tight')

# Save to excel && print resutls
print(pd.DataFrame(Weights,Criteria))
pd.DataFrame(Weights,Criteria).to_excel("output_" + timestampStr + '.xlsx', header=False)
