import csv

with open('HeightWeight.csv') as f:
    read = csv.reader(f)
    list1 = list(read)
random = list1.pop(0)

list2 = []

for i in range(len(list1)):
    temp=list1[i][2]
    list2.append(float(temp))

list2.sort()
length = len(list2)
if(length%2 == 0):
    median1 = float(list2[length//2])
    median2 = float(list2[length//2 - 1])
    finalmedian = (median2)
    print(finalmedian)
else:
    finalmedian = list2[length//2]
    print(finalmedian)
