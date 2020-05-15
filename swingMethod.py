import json

alts = []

with open("swingAlts.json", "r") as read_file:
    data = json.load(read_file)
    N = data['criteria']
    for i in range(1,N+1):
        for alt in data['Alt'+str(i)]:
            list = [alt['cost'], alt['reliability'], alt['time']]
        alts.append(list)

benchmark = [alts[0][0], alts[0][1], alts[0][2]]

for alt in alts:
    for i in range(N):
        if benchmark[i] < alt[i]:
            benchmark[i] = alt[i]



