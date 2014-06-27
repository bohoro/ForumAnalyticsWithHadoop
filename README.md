Forum Analytics With Hadoop
========================

## Improving Forum Search: Inverted index examples using Hadoop Streaming and forum data.

In our initial inverted index in lesson 4 of Intro to Hadoop and MapReduce we simply created a single word index based on the body of the forum data linking back to the node(s) where the word could be found.  This is useful like an index in a book but certainly can be improved.

The first improvement would be to create a reverse index of the tags as a special index so users can see all posts that correspond to a specific tag.  In addition, this tag based reverse index could be used by the Forum UI to show other similar posts based on the tags.

The tag_index_mapper.py mapper and the tag_index_reducer.py reducer are Python files to be used with Hadoop Streaming implementing an Improved Forum Search model. The sample forum data can be found in forum_node.tsv.

Unix pipeline testing can be run by using:

    cat forum_node.tsv | ./tag_index_mapper.py | sort | ./tag_index_reducer.py 

Running Hadoop on using my configuration is:

    hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper tag_index_mapper.py -reducer tag_index_reducer.py -file tag_index_mapper.py -file tag_index_reducer.py -input <HDFS location of forum_node.tsv>  -output <HDFS output directory>
    
## Additional Questions: Top 10 Solution Providers

One interesting thing I would like to know is who are the top 10 answerers of questions (Solution Providers) on the forum.  This could be derived using a summarization and filtering pattern to aggregate counts for answers based on userid and then compute the 10 tens answerers.

The top_solutions_mapper.py mapper and the top_solution_reducer.py reducer are Python files to be used with Hadoop Streaming implement the Top 10 Solution Providers concept.  The sample forum data can be found in forum_node.tsv.

Unix pipeline testing can be run by using:

    cat forum_node.tsv | ./top_solutions_mapper.py | sort | ./tag_index_reducer.py 

Running Hadoop on using my configuration is:

    hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper top_solutions_mapper.py -reducer tag_index_reducer.py -file top_solutions_mapper.py -file tag_index_reducer.py -input <HDFS location of forum_node.tsv>  -output <HDFS output directory>
    

