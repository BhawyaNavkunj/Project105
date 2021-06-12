import math
import csv

with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def find_mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)

    mean = total/n
    return mean

squared_list = []
for x in data:
    num = int(x) - find_mean(data)
    num = num**2
    squared_list.append(num)

sum = 0
for k in squared_list:
    sum += k

result = sum/(len(data)-1)

sd = math.sqrt(result)
print("Standard deviation : " + str(sd))
