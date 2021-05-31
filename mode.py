import csv
from collections import Counter

with open('HeightWeight.csv') as f:
    read= csv.reader(f)
    list1= list(read)
random = list1.pop(0)

list2 = []
for i in range(len(list1)):
    temp = list1[i][1]
    list2.append(float(temp))
data = Counter(list2)
print(data)