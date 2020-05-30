import json
import pandas

alts = []


print('Importing file swingAlts.json ...\n')
print('\n\nCriterion    Factors\n')
with open("swingAlts.json", "r") as read_file:
    data = json.load(read_file)
    Criteria = data['criteria']
    N = data['alternatives']
    print(data['Alt1'])
    for i in range(1, N + 1):
        for alt in data['Alt' + str(i)]:
            List = [alt['cost'], alt['reliability'], alt['time']]
            print(str(i) + '     ' + str(List))
        alts.append(List)

benchmark = [alts[0][0], alts[0][1], alts[0][2]]

for alt in alts:
    for i in range(N):
        if benchmark[i] < alt[i]:
            benchmark[i] = alt[i]
