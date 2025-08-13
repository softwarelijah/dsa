from array import array

# 1. Create an array and traverse it
my_array = array('i', [1, 2, 3, 4, 5])  # 'i' means signed integer type
print("Initial array:", my_array)

# 2. Access individual elements through indexes
print("First element:", my_array[0])
print("Third element:", my_array[2])

# 3. Append a value to the array
my_array.append(6)  # Adds element to the end
print("After append:", my_array)

# 4. Insert value in an array
my_array.insert(1, 10)  # Inserts 10 at index 1
print("After insert at index 1:", my_array)

# 5. Extend python array with multiple elements
my_array.extend([7, 8, 9])  # Extends array by adding elements from iterable
print("After extend:", my_array)

# 6. Add items from a list into array
temp_list = [11, 12]
my_array.fromlist(temp_list)  # Adds all elements from the list to array
print("After fromlist:", my_array)

# 7. Remove a specific element
my_array.remove(10)  # Removes first occurrence of 10
print("After remove(10):", my_array)

# 8. Remove last element
last_element = my_array.pop()  # Removes and returns last element
print(f"Removed last element: {last_element}")
print("After pop:", my_array)

# 9. Fetch element index
index_of_3 = my_array.index(3)  # Returns first index of value 3
print("Index of value 3:", index_of_3)

# 10. Reverse the array
my_array.reverse()
print("After reverse:", my_array)

# 11. Get buffer info
print("Buffer info (address, length):", my_array.buffer_info())

# 12. Count occurrences of a value
count_2 = my_array.count(2)
print("Occurrences of value 2:", count_2)

# 13. Convert array to bytes string
bytes_string = my_array.tobytes()  # tostring() is deprecated, use tobytes()
print("Array as bytes:", bytes_string)

# 14. Convert array to a Python list
list_version = my_array.tolist()
print("Array as list:", list_version)

# 15. Append from bytes string
# fromstring() is deprecated, use frombytes()
my_array.frombytes(bytes(array('i', [13, 14])))
print("After frombytes:", my_array)

# 16. Slice elements from array
slice_example = my_array[2:5]  # Get elements from index 2 to 4
print("Slice from index 2 to 4:", slice_example)
