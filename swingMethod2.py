import pandas as pd
import sys

# Import file "swingAlts.xlsx"
Data = pd.read_excel(r'swingAlts.xlsx', index_col=0)
print('Imported file swingAlts.xlsx!')
print(Data)
r, c = Data.shape

Criteria = list(Data.columns)
Alts = list(Data.index)
#print(Alts, Criteria)

# Build benchmark alternative (the alternative with the worst of each alternative)
benchmark = []
Swings = []

for x in Data.columns:
    benchmark.append(Data[x].max())
    Swings.append(Data[x].min())

# Build swing's fictional alts
Matrix = [[benchmark[i] for i in range(c)] for j in range(r)]
for x in range(c):
    Matrix[x][x] = Swings[x]

# Build swing matrix
SwingData = pd.DataFrame(Matrix, index=Criteria)
print("Our Swing Matrix is:")
print(SwingData)

# Determine most valued criterion
try:
    choice = int(input("Please pick the criteria that you value most (Enter number 1,2,..): "))
except ValueError:
    print("Error 100: NaN")
    sys.exit(100)
print("You value " + Criteria[choice] + " most.\n")

# Determine the value of swing from one criterion to another
Value = [0 for i in Criteria]
Value[choice] = 1

for criterion in Criteria:
    if criterion != Criteria[choice]:
        try:
            Value[Criteria.index(criterion)] = float(input("How much to you value " + criterion + " over " + Criteria[choice] + "? (Enter decimal from 0 to 1) "))
        except ValueError:
            print("Error 100: NaN")
            sys.exit(100)

# Normalize weights
total = 0
for value in Value:
    total += value*100

Weight = []
# Calculate weights
for i in range(r):
    Weight.append(Value[i]*100/total)

print(Weight)