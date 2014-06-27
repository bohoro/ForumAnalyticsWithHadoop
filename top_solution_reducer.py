#!/usr/bin/python

##########################################################################################
# Additional Questions: Top 10 Solution Providers
#
# One interesting thing I would like to know is who are the top 10 answerers of questions 
# (Solution Providers) on the forum.  This could be derived using a summarization and 
# filtering pattern to aggregate counts for answers based on userid and then compute the 
# 10 tens answerers.
#
# <author>
#
##########################################################################################

import sys
import csv

# global to store the top 10
TopTenList = []

##########################################################################################
# proposeForTopN 
#
# Function to keep track of top 10 so far
##########################################################################################
def proposeForTopN(word, count):
    global TopTenList
    TopTenList.append((count,word))
    # only keep the top 10 results
    TopTenList = sorted(TopTenList, reverse=True)[:10]

##########################################################################################
# Reducer 
#
# Reduces the set of intermediate values which share a key to a smaller set of values.
##########################################################################################
def reducer():
    # stats for word count
    countTotal = 0
    oldKey = None
    # read all records
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 2:
            # parse the line
            thisKey, thisCount = line
        if len(line) != 2:
            # Something has gone wrong. Skip this line.
            continue
            
        if oldKey and oldKey != thisKey:
            proposeForTopN(oldKey, countTotal)
            oldKey = thisKey;
            countTotal = 0

        oldKey = thisKey
        countTotal += int(thisCount)

    if oldKey != None:
        proposeForTopN(oldKey, countTotal)
        
    for item in TopTenList:
        print "{0}\t{1}".format(item[1], item[0])


# Define a main function, simply calls our reducer
def main():
    reducer()

# Call the main function for use with Hadoop Streaming
main()
