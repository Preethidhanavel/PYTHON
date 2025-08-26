What happens if you try to use a list as a dictionary key? Why?
Dictionary keys in Python must be:
Immutable
A list is mutable, meaning it can change (you can append, remove, etc.).
Because of this, it cannot have a fixed hash value, which is required for a dictionary to efficiently look up keys.