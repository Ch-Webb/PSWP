#Problem Solving With Python - Charlie Webb - 1823045
import csv
import matplotlib.pyplot as plt
#1A
def series_score(sailor, x=1):
    total = 0
    new = sorted(sailor[1])[:-x]
    for item in new:
        total += item
    return total

#1B
def sort_series(sailors):
    return sorted(sailors, key= lambda x: (series_score(x), x[1][0]))

#1C        
def read_sailor_data(file):
    dictout = {}
    with open(file) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != "name":
                dictout[row[0]] = (float(row[1]), float(row[2]))
    return dictout
        
#1D
def generate_performances(dictionary):
    dictout = {}
    return numpy.random.normal(100, 0)

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
