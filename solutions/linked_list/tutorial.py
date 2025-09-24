# linked_lists_minimal.py

# =========================
# Singly Linked List
# =========================

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Build: 1 -> 3 -> 4 -> 7
head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

head.next = A
A.next = B
B.next = C

# Print head node (will show the value because of __str__)
print(head)

# Traverse The List - O(n)
curr = head
while curr:
    print(curr)
    curr = curr.next


# Display Linked List - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements) if elements else '<empty>')


display(head)


# Search for a node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


print("Search 7:", search(head, 7))
print("Search 2:", search(head, 2))


# =========================
# Doubly Linked List
# =========================

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


# Start DLL with a single node
dhead = dtail = DoublyNode(1)
print(dtail)  # prints 1


def ddisplay(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements) if elements else '<empty>')


ddisplay(dhead)


# Insert at Beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head, prev=None)
    if head is not None:
        head.prev = new_node
        return new_node, tail
    else:
        # empty list case
        return new_node, new_node


dhead, dtail = insert_at_beginning(dhead, dtail, 3)
ddisplay(dhead)


# Insert at End - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, next=None, prev=tail)
    if tail is not None:
        tail.next = new_node
        return head if head is not None else new_node, new_node
    else:
        # empty list case
        return new_node, new_node


dhead, dtail = insert_at_end(dhead, dtail, 5)
ddisplay(dhead)
