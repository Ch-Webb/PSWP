import matplotlib.pyplot as plt
import numpy as np
from coursework import *

alice = []
bob = []
clare = []
dennis = []
eva = []

for x in range(0, 40):
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
