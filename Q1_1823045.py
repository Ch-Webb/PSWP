#Problem Solving With Python - Charlie Webb - 1823045
import csv
import random
import numpy as np

#1A
def series_score(sailor, crop=1):
    #Sort list in ascending order. Final item will be worst race. Crop with default variable "crop"
    #Return sum of all items in list
    return sum(sorted(sailor[1])[:-crop])

#1B
def sort_series(sailors, crop=1):
    #Return sorted list, sorted by key of their series_score, ties broken with the first element of the list
    #Give option to user to change number of cropped races - will be useful during report
    return sorted(sailors, key= lambda x: (series_score(x, crop), x[1][0]))

#1C        
def read_sailor_data(file):
    dictout = {}
    with open(file) as file:
        for row in csv.reader(file):
            #Ignore titles for columns
            if row[0] != "name":
                dictout[row[0]] = (float(row[1]), float(row[2]))
    return dictout
        
#1D
def generate_performances(dictionary):
    dictout = {}
    for key in dictionary:
        #Normalvariate function with mu and sigma
        dictout[key] = np.random.normal(dictionary[key][0], dictionary[key][1])
    return dictout

#1E
def calculate_finishing_order(dictionary):
    #Sort input dictionary according to the simulated scores of each in descending order
    return sorted(dictionary, key = lambda x: dictionary[x], reverse=True)

#1F
results = {}
#Below code extracts names from csv file, allowing names to be changed without editing raw code - no hardcoding!
with open('sailordata.csv') as file:
    for row in csv.reader(file):
        #Ignore column headers
        if row[0] != "name":
            results[row[0]] = []
#Simulate a race 6 times
for i in range(0, 6):
    simulate = calculate_finishing_order(generate_performances(read_sailor_data('sailordata.csv')))
    for item in simulate:
        #Returning index but as arrays start at 0 index will be 1 less than finishing position - add 1 to account
        results[item].append((simulate.index(item) + 1))
#Seriesinput acts as an intermediary, allowing names and results to be linked 
seriesinput = []
finaloutput = []
for key in results:
    scorein = (key, results[key])
    seriesinput.append(scorein)
sortedseries = sort_series(seriesinput)
for item in sortedseries:
    finaloutput.append(item[0])
print(finaloutput)


