# Consistency Hashing

Consistency hashing is a popular algorithm to ensure that cache misses are
minimized when cache servers are added or removed in cache clusters. This 
repository is an implementation of this algorithm. This algorithm leverages 
the power of AVL Tree (Balanced Binary Tree) to ensure insertion and deletion 
operations are optimal. Using the AVL Tree we can can construct 
a HashRing and use it to add and remove cache servers and move the 
cache data appropriately to the remaining nodes.


I have written a more detailed explination on my blog: TODO


