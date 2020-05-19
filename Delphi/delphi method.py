import pandas as pd
import os

oldanswrs = ["nothing old yet"]
answrs = []
pinakas_diaforon = ['There is no diversity yet']
agrmnt = False

while agrmnt == False:

    data = pd.read_excel(r'C:\Users\Hristos Birbou\PycharmProjects\legendary-rotary-phone\Delphi\data.xlsx', index_col=0)

    r, c = data.shape
    diafora = 0
    sumfonia = 0


    for i in range(r):
        temp = 0
        print("-------er", i+1, "-------", sep='')

        for j in range(c):
            print('user', j+1, ': ', data.iloc[i, j], sep='')
            temp += data.iloc[i, j]

        motemp = temp / c
        answrs.append(motemp)

        if oldanswrs[0] != "nothing old yet":
            diafora = oldanswrs[i] - answrs[i]
            pinakas_diaforon.append(abs(round(diafora,2)))

            if pinakas_diaforon[i] < 0.05:
                sumfonia += 1


    #print(len(answrs), answrs, oldanswrs)
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