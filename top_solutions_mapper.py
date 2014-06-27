#!/usr/bin/python

##########################################################################################
# Additional Questions: Top 10 Solution Providers
#
# One interesting thing I would like to know is who are the top 10 answerers of questions 
# (Solution Providers) on the forum.  This could be derived using a summarization and 
# filtering pattern to aggregate counts for answers based on userid and then compute the 
# 10 tens answerers.
#
# <author>   <answer_count>
#
##########################################################################################

import sys
import csv

##########################################################################################
# Mapper
#
# Maps input key/value pairs to a set of intermediate key/value pairs.
# Maps are the individual tasks which transform input records into a intermediate records. 
# The transformed intermediate records need not be of the same type as the input records. 
# A given input pair may map to zero or many output pairs.
##########################################################################################
def mapper():
    debug = False
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 19:
            # parse the line
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, \
            score, state_string, last_edited_id, last_activity_by_id, last_activity_at, \
            active_revision_id, extra, extra_ref_id, extra_count, marked = line
            # ignore the header line
            if (id == "id"): continue
            # In order to find the hour posted, please use the date_added field and NOT 
            #  the last_activity_at field
            if node_type=="answer":
                print "{0}\t{1}".format(author_id.strip(), 1 )
        else:
            # for debug only print the line we rejected for not being of length 19
            if debug: print "BMOERROR: " + line

# Define a main function, simply calls our mapper
def main():
    mapper()

# Call the main function for use with Hadoop Streaming
main()
