#!/usr/bin/python

##########################################################################################
# Tag Based Inverted Index
#
# Create a reverse index of the tags as a special index so users can see all posts that 
# correspond to a specific tag. In addition, this tag based reverse index could be used 
# by the Forum UI to show other similar posts based on the tags.
#
# Output from mapper will be:
#
# <tag>   <question node id>
#
##########################################################################################

import sys
import csv

##########################################################################################
# Reducer 
#
# Reduces the set of intermediate values which share a key to a smaller set of values.
#   See tag_index_mapper.py for inputs
##########################################################################################
def reducer():
    # stats for past key we are accumulating
    nodeList = []   # here we gather all the nodes for a given tag
    oldKey = None   # last tag we saw
    
    # read all records
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 2:  # parse the line
            thisKey, node = line
        else:   # Input is not what we expected. Skip this line.
            continue 
        if oldKey and oldKey != thisKey:
            # we have switched to a new key, emit the last key 
            print "{0}\t{1}".format(oldKey, nodeList)
            # reset key data
            oldKey = thisKey;
            nodeList = []

        # process this record
        oldKey = thisKey
        nodeList.append(int(node))

    # print the last key
    if oldKey != None:
        print "{0}\t{1}".format(oldKey, nodeList)

    

# Define a main function, simply calls our reducer
def main():
    reducer()

# Call the main function for use with Hadoop Streaming
main()
