import pandas as pd

oldanswrs = ["nothing old yet"]
answrs = []
diafora = []
agrmnt = False

while agrmnt == False:

    data = pd.read_excel(r'C:\Users\Hristos Birbou\PycharmProjects\legendary-rotary-phone\Delphi\data.xlsx', index_col=0)

    r, c = data.shape


    for i in range(r):
        temp = 0
        print("-------er", i+1, "-------", sep='')

        for j in range(c):
            print('user', j+1, ': ', data.iloc[i, j], sep='')
            temp += data.iloc[i, j]

        motemp = temp / c
        answrs.append(motemp)

        if oldanswrs[0] != "nothing old yet":
            diafora.append(oldanswrs[i] - answrs[i])


    print(len(answrs), answrs, oldanswrs)
    print(diafora)
    oldanswrs.clear()
    oldanswrs = answrs.copy()
    answrs.clear()
    diafora.clear()

    apantisi = input('ok?')

    if apantisi == 'ok':
        agrmnt = True