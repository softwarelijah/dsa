# Stacks and Queues - Data Structures Guide

## Table of Contents
- [Stacks](#stacks)
    - [Concept](#stack-concept)
    - [Operations](#stack-operations)
    - [Time Complexity](#stack-time-complexity)
    - [Implementation](#stack-implementation)
- [Queues](#queues)
    - [Concept](#queue-concept)
    - [Operations](#queue-operations)
    - [Time Complexity](#queue-time-complexity)
    - [Implementation](#queue-implementation)
- [Key Differences](#key-differences)

---

## Stacks

### Stack Concept
A **stack** is a data structure that follows the **LIFO (Last In, First Out)** principle. Think of it like a stack of plates - you can only add or remove plates from the top.

**Visual representation:**
```
[5, 7, 8, 4]  # 4 is at the "top" (rightmost position)
```

### Stack Operations

#### 1. **Append/Push** - Add element to top
- Adds element to the right side of the stack
- Can store any data type (numbers, strings, complex objects)

#### 2. **Pop** - Remove element from top
- Removes and returns the rightmost element
- Always removes the most recently added item

#### 3. **Peek** - View top element without removing
- Returns the top element without modifying the stack
- Access using `stack[-1]` in Python

#### 4. **isEmpty** - Check if stack is empty
- Returns `True` if stack has no elements
- Returns `False` if stack contains elements

### Stack Time Complexity
- **Append**: O(1) average (when implemented as dynamic array)
- **Pop**: O(1) always
- **Peek**: O(1) always
- **isEmpty**: O(1) always

### Stack Implementation

#### Basic Stack Operations in Python:
```python
# Create empty stack
stack = []

# Append elements
stack.append(5)
stack.append(4)
stack.append(3)
print(stack)  # [5, 4, 3]

# Pop element
x = stack.pop()
print(x)      # 3 (returned value)
print(stack)  # [5, 4] (modified stack)

# Peek at top
if stack:
    top = stack[-1]
    print(top)  # 4

# Check if empty
if stack:
    print("Stack has elements")
else:
    print("Stack is empty")

# Safe popping
if stack:
    stack.pop()
```

---

## Queues

### Queue Concept
A **queue** is a data structure that follows the **FIFO (First In, First Out)** principle. Think of it like a line of people - the first person in line is the first to be served.

**Visual representation:**
```
[1, 2, 3, 4]  # 1 is first to come out (leftmost), 4 is last in line (rightmost)
```

### Queue Operations

#### 1. **Enqueue** - Add element to back
- Adds element to the right side of the queue
- New arrivals go to the back of the line

#### 2. **Dequeue** - Remove element from front
- Removes and returns the leftmost element
- Serves the person who has been waiting longest

#### 3. **Peek** - View front/back elements
- Front: `queue[0]` - next to be served
- Back: `queue[-1]` - last in line

### Queue Time Complexity
When implemented as **doubly linked list** (recommended):
- **Enqueue**: O(1)
- **Dequeue**: O(1)
- **Peek**: O(1)

⚠️ **Note**: If implemented as dynamic array, dequeue becomes O(n) due to shifting elements.

### Queue Implementation

#### Using collections.deque in Python:
```python
from collections import deque

# Create empty queue
q = deque()

# Enqueue elements (add to right)
q.append(5)
q.append(6)
q.append(7)
print(q)  # deque([5, 6, 7])

# Dequeue element (remove from left)
first = q.popleft()
print(first)  # 5 (returned value)
print(q)      # deque([6, 7]) (modified queue)

# Peek operations
if q:
    front = q[0]    # Next to be served
    back = q[-1]    # Last in line
    print(f"Front: {front}, Back: {back}")  # Front: 6, Back: 7

# Add more elements
q.append(8)
print(q)  # deque([6, 7, 8])
```

#### Why deque instead of list for queues?
- `deque` provides O(1) operations on both ends
- Regular list would require O(n) for removing from the front
- `deque` is implemented as doubly linked list internally

---

## Key Differences

| Aspect | Stack (LIFO) | Queue (FIFO) |
|--------|--------------|--------------|
| **Add Operation** | Append to top (right) | Enqueue to back (right) |
| **Remove Operation** | Pop from top (right) | Dequeue from front (left) |
| **Order** | Last In, First Out | First In, First Out |
| **Implementation** | Dynamic array works well | Use deque for efficiency |
| **Use Cases** | Undo operations, recursion, parsing | Task scheduling, BFS, process queues |

### Memory Visualization:
```
Stack:     [1, 2, 3, 4]
           ↑         ↑
         add/remove here

Queue:     [1, 2, 3, 4]
           ↑         ↑
         remove    add
```

### Common Applications:
- **Stacks**: Function calls, expression evaluation, backtracking, browser history
- **Queues**: Print job scheduling, breadth-first search, handling requests in web servers

---

## Important Notes:
- Both can store complex data types (tuples, lists, dictionaries)
- Always check if empty before popping/dequeuing to avoid errors
- Choose the right data structure based on whether you need LIFO or FIFO behavior