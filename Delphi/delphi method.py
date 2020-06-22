import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# List initiation
oldanswrs = ["nothing old yet"]
answrs = []
pinakas_diaforon = ['There is no diversity yet']

# Agreement check, if it's True the main loop stops.
agrmnt = False

# Main loop. This loop checks the data between rounds, if the data is similar the loop stops.
while agrmnt == False:

    # Importing the excel file.
    data = pd.read_excel(r'data.xlsx', index_col=0)
    Alts = list(data.index)

    # Reading the rows an columns (determines how many questions and  how many participants we have).
    r, c = data.shape

    # Init of some variables.
    diafora = 0
    sumfonia = 0

    # Analyzing data.
    for i in range(r):
        temp = 0
        # Print the current question.
        print("-------er", i+1, "-------", sep='')

        for j in range(c):
            # Print the answer of each user for the specific question.
            print('user', j+1, ': ', data.iloc[i, j], sep='')
            temp += data.iloc[i, j]

        # Average of the answers.
        motemp = temp / c
        answrs.append(motemp)

        if oldanswrs[0] != "nothing old yet":
            diafora = oldanswrs[i] - answrs[i]
            pinakas_diaforon.append(abs(round(diafora,2)))

            if pinakas_diaforon[i] < 0.05:
                sumfonia += 1


    print('----------ANSWERS----------')
    print('-The answers from this round are:', answrs)
    print('-The answers from the previous round are:', oldanswrs)
    print('-The diversity between the last two rounds is:', pinakas_diaforon)

    oldanswrs.clear()
    oldanswrs = answrs.copy()
    answrs.clear()
    pinakas_diaforon.clear()

    if sumfonia == r:
        agrmnt = True

    else:
        input('Press enter to continue...')


print("--------------------The weights are--------------------")

for i in range(r):
    print('Er', i, ': ', round(oldanswrs[i], 2), sep='')


# Plot results
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.barh(Alts,oldanswrs)
ax.set_ylabel('Criteria')
ax.set_xlabel('Weights')

# Get date+time for filename
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%m-%Y_%H:%M:%S")

# Save to png
plt.savefig('plot_' + timestampStr + '.png',bbox_inches='tight')