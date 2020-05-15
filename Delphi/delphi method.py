import pandas as pd

data = pd.read_excel (r'C:\Users\Hristos Birbou\PycharmProjects\legendary-rotary-phone\Delphi\data.xlsx',index_col=0)

r, c = data.shape
agrmnt = 0

for i in range(r):

    votes = 0
    print("er", i+1, ':', sep='')

    for j in range(c):
        #print("user",j+1,": ",data.iloc[i, j], sep='')
        votes += int(data.iloc[i,j])
    print("the positive votes are:", votes)

    mo = votes / c
    percent = (1 - mo)/1
    print(percent)

    if mo == 1 or mo == 0:
        print("We have consensus")
        agrmnt += 1

    elif percent > 0.8 or percent < 0.2 :
        print("getting there")
        agrmnt += 1

agrmnt_percent = ((r - agrmnt)/r)*100
if agrmnt == r:
    print("Finished successfully")
else:

    print("Do again the survey and then run again the program because we had ", round(agrmnt_percent,1),"% agreement", sep='')