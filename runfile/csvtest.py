import csv

# TEST 1 
"""
with open("testnames.csv", "r") as f:
    reader = csv.reader(f)
    your_list = [e[0].strip().split(",") for e in reader if e]
"""

with open('testnames.csv') as file:
     data = csv.reader(file)
     for row in data:
         x = row
         #print(x)


# TEST 2 

results = []
with open('testnames.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])

print(results)