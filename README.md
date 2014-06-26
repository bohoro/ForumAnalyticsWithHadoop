Forum Analytics With Hadoop
========================

Inverted index examples using Hadoop Streaming and forum data.

In our initial inverted index in lesson 4 of Intro to Hadoop and MapReduce we simply created a single word index based on the body of the forum data linking back to the node(s) where the word could be found.  This is useful like an index in a book but certainly can be improved.

The first improvement would be to create a reverse index of the tags as a special index so users can see all posts that correspond to a specific tag.  In addition, this tag based reverse index could be used by the Forum UI to show other similar posts based on the tags.

The following mapper and reducer are Python files to be used with Hadoop Streaming.  The sample forum data can be found in forum_node.tsv.

