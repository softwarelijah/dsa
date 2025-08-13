# Create
nums = [1, 2, 3]
import array
arr = array.array('i', [1, 2, 3])  # fixed-type array

# Append & Extend
nums.append(4)            # [1, 2, 3, 4]
nums.extend([5, 6])       # [1, 2, 3, 4, 5, 6]

# Insert
nums.insert(2, 99)        # Insert 99 at index 2

# Access
x = nums[0]               # First element
y = nums[-1]              # Last element

# Search
3 in nums                 # True
nums.index(3)             # Index of value 3

# Traverse
for num in nums:
    print(num)

# Delete
nums.remove(99)           # Remove by value
nums.pop(1)               # Remove by index
del nums[0]               # Delete index 0
nums.clear()              # Empty list

# Slicing
sub = nums[1:4]           # Elements from index 1 to 3

# Reverse
nums.reverse()

# Sort
nums.sort()

# Length
len(nums)



# Practice Problems

# =========================
# CREATE
# =========================
nums_create = [1, 2, 3]
import array
arr_fixed = array.array('i', [1, 2, 3])  # fixed-type array
print(nums_create)
print(arr_fixed)


# =========================
# APPEND & EXTEND
# =========================
nums_append_extend = [1, 2, 3]
nums_append_extend.append(4)              # [1, 2, 3, 4]
nums_append_extend.extend([5, 6])         # [1, 2, 3, 4, 5, 6]
print(nums_append_extend)


# =========================
# INSERT
# =========================
nums_insert = [1, 2, 3, 4]
nums_insert.insert(2, 99)  # Insert 99 at index 2
print(nums_insert)


# =========================
# ACCESS
# =========================
nums_access = [10, 20, 30]
x = nums_access[0]   # First element
y = nums_access[-1]  # Last element
print(x, y)


# =========================
# SEARCH
# =========================
nums_search = [1, 2, 3, 4, 5]
print(3 in nums_search)        # True
print(nums_search.index(3))    # Index of value 3


# =========================
# TRAVERSE
# =========================
nums_traverse = [2, 4, 6, 8]
for num in nums_traverse:
    print(num * 3)


# =========================
# DELETE
# =========================
nums_delete = [1, 2, 3, 4, 5]
nums_delete.remove(3)  # Remove by value
nums_delete.pop(0)     # Remove by index
print(nums_delete)


# =========================
# APPEND vs EXTEND
# =========================
nums_append_vs_extend = [1, 2, 3]
nums_append_vs_extend.append([4, 5])  # Appends list as one element
print(nums_append_vs_extend)

nums_append_vs_extend = [1, 2, 3]
nums_append_vs_extend.extend([4, 5])  # Adds each element individually
print(nums_append_vs_extend)


# =========================
# SLICING
# =========================
nums_slice = [0, 1, 2, 3, 4, 5]
sub_slice = nums_slice[1:4]  # Elements from index 1 to 3
print(sub_slice)


# =========================
# REVERSE
# =========================
nums_reverse = [1, 2, 3]
nums_reverse.reverse()
print(nums_reverse)


# =========================
# SORT
# =========================
nums_sort = [5, 2, 9, 1]
nums_sort.sort()
print(nums_sort)


# =========================
# LENGTH
# =========================
nums_length = [7, 8, 9]
print(len(nums_length))


# =========================
# PRACTICE PROBLEM: CREATION & ACCESS
# =========================
nums_ca = [1, 2, 3, 4, 5]
print(nums_ca[0])   # First element
print(nums_ca[-1])  # Last element
print(len(nums_ca)) # Length


# =========================
# PRACTICE PROBLEM: INSERTION
# =========================
nums_insertion = [10, 20, 30, 40]
nums_insertion.append(50)
nums_insertion.insert(1, 25)
print(nums_insertion)


# =========================
# PRACTICE PROBLEM: SEARCH FUNCTION
# =========================
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

arr_search = [1, 2, 3, 4, 5]
print(find_index(arr_search, 4))   # Found
print(find_index(arr_search, 10))  # Not found


# =========================
# PRACTICE PROBLEM: REMOVE EVENS
# =========================
def remove_evens(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] % 2 == 0:
            nums.pop(i)
    return nums

print(remove_evens([1, 2, 3, 4, 5, 6]))


# =========================
# PRACTICE PROBLEM: REVERSE SEARCH
# =========================
def reverse_search(nums, target):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            return i
    return -1

arr_rev_search = [5, 3, 7, 3, 9]
print(reverse_search(arr_rev_search, 3))   # 3
print(reverse_search(arr_rev_search, 10))  # -1


