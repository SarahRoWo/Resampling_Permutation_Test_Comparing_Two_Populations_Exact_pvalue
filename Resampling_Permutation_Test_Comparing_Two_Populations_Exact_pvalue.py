from itertools import combinations
from statistics import mean

#manually input experimental results for each condition. 

listA = # data for experiment (list)

listB = # data for experiment - control (list)

#combinations is a generator that can go through all combinations of data (n choose k)

listAlistB = combinations(listA+listB, len(listA)) # every combination of values of listA and listB can be generated; this is not tenable for other conditions with high n.

referencevalue = sum(listA) # test statistic; can modify depending on experiment

lessthan = 0

greaterthan = 0

equalto = 0

timesitsrun = 0

while True:

    try:

        currentlist = next(listAlistB)

        x = sum(currentlist) #sums up the combination from generator

        if x < referencevalue: # this determines whether the combination is greater than, less than, or equal to sum(listA) and keeps a counter

            lessthan += 1

        elif x > referencevalue:

            greaterthan += 1

        elif x == referencevalue:

            equalto += 1

        timesitsrun +=1

        if timesitsrun % 1000000 == 0:

            print(timesitsrun)

    except StopIteration:

        break

pvalue = (greaterthan + equalto) / (lessthan + equalto + greaterthan)

print("combinations less than {} sum of slopes = {}" .format('listA', lessthan))

print("combinations greater than {} sum of slopes = {}" .format('listA', greaterthan))

print("combinations equal to {} sum of slopes = {}" .format('listA', equalto))

print("p value = {}" .format(pvalue))
