# Linked Lists (Singly & Doubly)

These notes are based on Greg Hogg’s lecture on **Linked Lists**.  
We’ll cover **concepts, operations, complexities, and Python implementations**.

---

## 1. Introduction to Linked Lists

- A **Linked List** is a linear data structure where elements (nodes) are connected by pointers/references.
- Unlike arrays:
    - **Arrays** → Contiguous memory, indexed access in `O(1)`.
    - **Linked Lists** → Nodes may be scattered in memory, no direct indexing.

### Types
- **Singly Linked List**: Each node points to the next node.
- **Doubly Linked List**: Each node points both to the next **and** the previous node.

---

## 2. Linked List Node Structure

### Singly Linked List Node
```python
class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


## Doubly Linked List Node
class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

```
```python
## Singly Linked List Operations


# Traversal
def traverse(head):
    curr = head
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")

# Display List Nicely
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(elements))


# Search For a Value:
def search(head, target):
    curr = head
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    return False


# Insert at Beginning:
def insert_at_beginning(head, value):
    new_node = SinglyNode(value)
    new_node.next = head
    return new_node  # new head


# Insert at Position
def insert_at_position(head, value, pos):
    new_node = SinglyNode(value)
    if pos == 0:
        new_node.next = head
        return new_node
    curr = head
    for _ in range(pos - 1):
        if not curr:
            return head
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head


# Delete at Beginning
def delete_at_beginning(head):
    if head:
        return head.next
    return None


# Delete at Position
def delete_at_position(head, pos):
    if pos == 0 and head:
        return head.next
    curr = head
    for _ in range(pos - 1):
        if not curr or not curr.next:
            return head
        curr = curr.next
    curr.next = curr.next.next
    return head
```

```python
## Doubly Linked List Operations


# Traversal (Forward)
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.value, end=" <-> ")
        curr = curr.next
    print("None")


# Traversal (Backward)
def traverse_backward(tail):
    curr = tail
    while curr:
        print(curr.value, end=" <-> ")
        curr = curr.prev
    print("None")


# Display List Nicely (Forward)
def display_forward(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" <-> ".join(elements))


# Search For a Value:
def search(head, target):
    curr = head
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    return False


# Insert at Beginning:
def insert_at_beginning(head, value):
    new_node = DoublyNode(value)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node  # new head


# Insert at Position:
def insert_at_position(head, value, pos):
    new_node = DoublyNode(value)
    if pos == 0:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node
    curr = head
    for _ in range(pos - 1):
        if not curr:
            return head
        curr = curr.next
    if not curr:
        return head
    new_node.next = curr.next
    new_node.prev = curr
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    return head


# Delete at Beginning:
def delete_at_beginning(head):
    if not head:
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head


# Delete at Position:
def delete_at_position(head, pos):
    if not head:
        return None
    if pos == 0:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    curr = head
    for _ in range(pos):
        if not curr:
            return head
        curr = curr.next
    if not curr:
        return head
    if curr.prev:
        curr.prev.next = curr.next
    if curr.next:
        curr.next.prev = curr.prev
    return head
```


