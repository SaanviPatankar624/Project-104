import pandas as pd
import csv

with open("height-weight.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0) 
newdata = []
for i in range(len (filedata) ):
    num = filedata[i][2]
    newdata.append(float(num))

n = len(newdata)
total = 0 
for j in newdata:
    total = total + j

mean = total/n 

print("this is the mean weight of the students", mean)

