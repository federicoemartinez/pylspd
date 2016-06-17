# pylspd
A python implementation of a "long strings probabilistic dictionaries"
This module provides two kind of dictionaries optimized to work with *very* long string keys

An LSPD can be created with a set of hasher functions so as when you define a key, the concatenation of all the hashes of that key is stored

An LSPSSDD is like a LSPD but if the key is shorter than the one generated by the hashers, the original key is stored. Hence it is deterministic for short keys.

Usage:

```python
d = LSPSSDD()
d["a"] = 23
d["what a string"*100000] = 54
print d["a"]
print "what a string"*100000 in d
print len(d.keys()[1])
```