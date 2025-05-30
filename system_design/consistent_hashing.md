# Consistent Hashing
Problem: When using a mod based hashing algorithm for load balancing, whenever you lose a server, your keys are remapped to different servers and that is problematic when the server caches specific user(key) information in a distributed setting. This leads to a storm of cache misses.

Consistent hashing is a special kind of hashing such that when a hash table is re-sized and consistent hashing is used, only k/n keys need to be remapped on average, where k is the number of keys, and n is the number of slots. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be
remapped.

Hash space: All possible outputs x_0, x_1, x_2, ... x_n of a hash function.
Hash ring: When you map the space into a circle.
Hash servers: Using the some hash function f, we map servers based on server IP or name onto the ring.