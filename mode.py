import pandas as pd
import csv
from collections import Counter

with open("height-weight.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0) 
newdata = []
for i in range(len (filedata) ):
    num = filedata[i][2]
    newdata.append(float(num))

data = Counter(newdata)
mode = {"120-130":0, "130-140":0, "140-150":0}

for height, occurence in data.items():
    if 120 < float(height) < 130:
        mode["120-130"] += occurence
    elif 130 < float(height) < 140:
        mode["130-140"] += occurence
    elif 140 < float(height) < 150:
        mode["140-150"] += occurence

moderange, modeoccurence = 0,0

for range, occurence in mode.items():
    if occurence > modeoccurence:
        moderange, modeoccurence = [int (range.split("-")[0]),int(range.split("-")[1])], occurence

finalmode = float((moderange[0] + moderange[1])/2)

print("the mode of the weight of the students is", finalmode)
