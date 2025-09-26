# Arrays and Strings in Python

## Static Arrays
- **Definition**: A contiguous block of memory with a fixed size.
- **Indices**:
    - First index: `0`
    - Last index: `length - 1`
- **Operations**:
    - **Access**: `a[i]` → O(1)
    - **Modify**: `a[i] = new_val` → O(1)
    - **Search (value in array)**: `val in a` → O(n) (must scan all elements in worst case)
    - **Insert at index**:
        - Requires shifting elements → O(n)
        - May lose last element (since size is fixed)
    - **Delete at index**:
        - Requires shifting remaining elements → O(n)

> ⚠️ Limiting because size cannot change.

---

## Dynamic Arrays (Python `list`)
- **Definition**: Resizable arrays built on top of static arrays.
- **Implementation detail**: When full, a new (larger) static array is allocated (often double the previous size) and elements are copied over (O(n)).
- **Operations**:
    - **Append at end**:
        - Usually O(1) (uses extra capacity).
        - Occasionally O(n) (resizes array).
        - On average: **amortized O(1)**.
    - **Pop at end**: O(1)
    - **Insert not at end**: O(n) (shifts elements).
    - **Delete not at end**: O(n) (shifts elements).
    - **Modify at index**: O(1)
    - **Access at index**: O(1)
    - **Search (value in array)**: O(n)

### Growth Strategy
- Typically doubles in size (e.g., 2 → 4 → 8 → 16 → …).
- Ensures amortized constant-time appends.

---

## Strings
- **Definition**: Immutable sequences of characters (contiguous memory).
- **Key Property**: Cannot be modified in place.
- **Operations**:
    - **Concatenation (append)**: O(n) (creates a new string).
    - **Insert/Delete/Modify**: ❌ Not possible (must create new string).
    - **Access at index**: O(1)
    - **Search (character in string)**: O(n)

---

## Python Examples

```python
# Dynamic array (list)
a = [1, 2, 3]

# Append (average O(1))
a.append(5)  
print(a)  # [1, 2, 3, 5]

# Pop (O(1))
a.pop()
print(a)  # [1, 2, 3]

# Insert at index (O(n))
a.insert(1, 7)
print(a)  # [1, 7, 2, 3]

# Modify at index (O(1))
a[0] = 9
print(a)  # [9, 7, 2, 3]

# Access (O(1))
print(a[2])  # 2

# Search (O(n))
print(7 in a)  # True

# Length (O(1))
print(len(a))  # 4


# Strings (immutable)
s = "hello"

# Append (O(n), creates new string)
s2 = s + "z"
print(s2)  # "helloz"

# Access (O(1))
print(s[1])  # "e"

# Search (O(n))
print("e" in s)  # True
print("z" in s)  # False

# Length (O(1))
print(len(s))  # 5
