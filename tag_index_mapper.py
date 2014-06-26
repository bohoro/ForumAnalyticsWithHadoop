#!/usr/bin/python

##########################################################################################
# Tag Based Inverted Index
#
# Create a reverse index of the tags as a special index so users can see all posts that 
# correspond to a specific tag. In addition, this tag based reverse index could be used 
# by the Forum UI to show other similar posts based on the tags.
##########################################################################################

"""
Output from mapper will be:

<question node id>   <tag>

"""

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
            # parse the line of forum
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, \
            score, state_string, last_edited_id, last_activity_by_id, last_activity_at, \
            active_revision_id, extra, extra_ref_id, extra_count, marked = line
            
            # ignore the header line
            if (id == "id"): continue
            
            # process answer node
            # emit all the tags similar to word count
            # emit all tags from questions, answers, and comments
            for word in tagnames.strip().split(" "):
                if (node_type=="answer"):
                    print "{0}\t{1}".format(word, abs_parent_id)
                # process question node
                elif (node_type=="question"):
                    print "{0}\t{1}".format(word, id )
                elif (node_type=="comment"):
                    print "{0}\t{1}".format(word, abs_parent_id )
                else:  # skip comments
                    continue
        else:
            # for debug only print the line we rejected for not being of length 19
            if debug: print "MAPERROR: " + line

# Define a main function, simply calls our mapper
def main():
    mapper()

# Call the main function for use with Hadoop Streaming
main()
