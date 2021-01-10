""" Implements a permutation test, returning an approximate p-value.

This script implements a permutation test for comparing two
populations. This script randomly shuffles data from two
populations, then compares a test statistic (e.g. sum)
from the original data with the test statistic of the
randomly shuffled data. The test statistic for
every possible combination of the data is compared with the
test statistic of the original data.

This script was used in Woldemariam et al., Genetics 213, 59 (2019).

For additional information on permutation tests for comparing
two populations, please refer to Good (2006). Link below:
https://link.springer.com/content/pdf/10.1007/0-8176-4444-X.pdf
"""

from itertools import combinations

# Provide manually inputted data for each condition.
listA = # Input data (list or tuple) from experiment here.
listB = # Input data (list or tuple) from control experiment here.

# combinations(listA+listB, len(listA)) is a generator that can go
# through all combinations of data (n choose k).

# Every combination of values of listA and listB can be generated.
# This is not tenable for data with a high number of possible
# combinations.
listAlistB = combinations(listA+listB, len(listA))

# The referencevalue is the test statistic. Here, the sum of elements
# of listA is the test statistic.
referencevalue = sum(listA)
lessthan = 0
greaterthan = 0
equalto = 0
timesitsrun = 0

while True:
    try:
        currentlist = next(listAlistB)
        x = sum(currentlist)
        if x < referencevalue:
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

pvalue = (greaterthan+equalto) / (lessthan+equalto+greaterthan)

print("combinations less than {} sum of slopes = {}" .format('listA', lessthan))
print("combinations greater than {} sum of slopes = {}" .format('listA', greaterthan))
print("combinations equal to {} sum of slopes = {}" .format('listA', equalto))
print("p-value = {}" .format(pvalue))
