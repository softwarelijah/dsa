# Hash Tables in Python (DSA Notes)

## What is a Hash Table?
- A data structure that stores data in **buckets** (array-like)
- Uses a **hash function** to map inputs (keys) → indices (bucket positions)
- Supports **fast average-time lookups, insertions, and deletions**

## Hash Functions
- Take input (e.g., string, int) → output an index
- Example: Sum alphabetical values of characters → mod by number of buckets
    - "Greg" → G(7) + R(18) + E(5) + G(7) = 37
    - 37 mod 5 = 2 → index 2

Important properties:
- **Deterministic**: same input → same output
- **Distributes values** evenly to reduce collisions

## Collisions
Occur when multiple keys hash to the same index. Two main strategies:

### 1. Separate Chaining
- Each bucket holds a **linked list** (chain)
- Multiple items can occupy the same index
- Lookup worst-case: `O(n)` if all items in one bucket
- Average case (good hash function): `O(1)`

### 2. Linear Probing
- If a bucket is occupied → probe forward until empty spot found
- Requires marking **deleted positions** with a special value (e.g., `-1`)
- Average case: `O(1)`, worst case: `O(n)`

## Hash Sets
A **collection of unique items** backed by a hash table.

Operations:
- **Insert**: O(1) average
- **Lookup**: O(1) average
- **Delete**: O(1) average

### Python Example
```python
# Create a set
s = set()

# Add elements
s.add(1)
s.add(2)
s.add(3)

# Lookup
if 1 in s:
    print("1 is in the set")

# Remove
s.remove(3)
```

Construction from a string (removes duplicates):
```python
s = set("aabbcde")
print(s)  # {'a', 'b', 'c', 'd', 'e'}
```

## Hash Maps (Dictionaries in Python)
- Store key-value pairs
- Keys must be hashable
- Values can be any data type

### Operations

**Insert/Update:**
```python
d = {}
d["Greg"] = 7
```

**Lookup:**
```python
print(d["Greg"])  # 7
```

**Check if key exists:**
```python
if "Greg" in d:
    print("Key exists")
```

**Remove:**
```python
del d["Greg"]
```

## Hashable vs Non-Hashable Types

**Hashable (Immutable):**
- `str`, `int`, `tuple`, etc.

**Not Hashable (Mutable):**
- `list`, `dict`, etc.

**Reason:** Mutability would break consistency of the hash.

## Special Dictionary Variants
Python's `collections` module provides useful tools:

### 1. defaultdict
Automatically assigns default values to missing keys.

```python
from collections import defaultdict

d = defaultdict(int)
print(d[2])  # 0 (default int)
```

### 2. Counter
Counts frequency of elements.

```python
from collections import Counter

s = "aabbcde"
counter = Counter(s)
print(counter)  # {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1}
```

## Complexity Summary

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Lookup    | O(1)         | O(n)       |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

## Key Takeaways
- Hash tables power sets and dictionaries in Python
- Average-case operations are constant time due to hashing
- Collisions must be handled (separate chaining / linear probing)
- Keys must be immutable (hashable)
- Python provides powerful built-ins: `set`, `dict`, `defaultdict`, and `Counter`