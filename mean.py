import pandas as pd
import csv 

with open('HeightWeight.csv') as f:
    read= csv.reader(f)
    list1= list(read)
random = list1.pop(0)

list2 = []
for i in range(len(list1)):
    temp = list1[i][1]
    list2.append(float(temp))
total=0
for i in list2:
    total=total+i
mean = total/ len(list1)
print(mean)