# Graphs Data Structure - Complete Guide

## What is a Graph?

A **graph** is a data structure consisting of:
- **Vertices (Nodes)**: Places or points that store data
- **Edges**: Connections between vertices

### Key Points:
- Trees are a subclass of graphs
- Linked lists are also a subclass of graphs
- Graphs are the most general form of these data structures

### Example Graph Structure:
```
Toronto → New York → UK
   ↓         ↑       ↓
   UK    ←───┘    Egypt
                     ↓
                   India
```

## Graph Terminology

### Vertices vs Nodes
- **Vertex**: Mathematical term used in graph theory
- **Node**: Computer science term (commonly used in programming)
- Both terms refer to the same concept

### Types of Graphs

#### 1. Directed Graph
- Edges have direction (indicated by arrow heads)
- If node A connects to node B, B doesn't necessarily connect back to A
- Example: `0 → 1 → 2`

#### 2. Undirected Graph
- Edges work in both directions
- If node A connects to node B, then B also connects to A
- Example: `0 ↔ 1 ↔ 2`

#### 3. Cyclic vs Acyclic Graphs
- **Cyclic**: Contains cycles (infinite loops possible)
- **Acyclic**: No cycles present

## Graph Storage Methods

### 1. Edge List
A simple list of all edges in the graph:
```python
edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,5], [5,4]]
```

**Problems:**
- Difficult to find neighbors of a specific node
- Inefficient for most algorithms

### 2. Adjacency Matrix
A 2D array where `matrix[i][j] = 1` if there's an edge from node i to node j:

```python
# For n nodes, create n×n matrix
def create_adjacency_matrix(edges, n):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1  # Directed
        # matrix[v][u] = 1  # Uncomment for undirected
    return matrix
```

**Problems:**
- Space inefficient: O(V²) space
- Slow neighbor lookup for sparse graphs

### 3. Adjacency List (Most Common)
A dictionary/hashmap where each key is a node and value is a list of neighbors:

```python
from collections import defaultdict

def create_adjacency_list(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # Directed
        # graph[v].append(u)  # Uncomment for undirected
    return graph
```

**Advantages:**
- Space efficient: O(V + E)
- Fast neighbor lookup
- Easy to work with

### 4. Class-Based Representation
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # List of Node references
    
    def add_neighbor(self, node):
        self.neighbors.append(node)
```

## Graph Traversal Algorithms

### Depth-First Search (DFS)

DFS explores as deep as possible down each branch before backtracking.

#### Recursive DFS
```python
def dfs_recursive(graph, start):
    seen = set()
    
    def dfs(node):
        if node in seen:
            return
        
        seen.add(node)
        print(node)  # Process node
        
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start)
```

#### Iterative DFS (Using Stack)
```python
def dfs_iterative(graph, start):
    seen = set()
    stack = [start]
    seen.add(start)
    
    while stack:
        node = stack.pop()  # Pop from right (LIFO)
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
```

### Breadth-First Search (BFS)

BFS explores all neighbors at the current depth before moving to nodes at the next depth.

```python
from collections import deque

def bfs(graph, start):
    seen = set()
    queue = deque([start])
    seen.add(start)
    
    while queue:
        node = queue.popleft()  # Pop from left (FIFO)
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
```

### Key Differences: DFS vs BFS

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (or recursion) | Queue |
| Memory Usage | O(depth) | O(width) |
| Use Cases | Path finding, topological sort | Shortest path, level-order |
| Traversal Pattern | Deep first | Level by level |

## Complexity Analysis

### Time Complexity: O(V + E)
- **V**: Number of vertices (we visit each node once)
- **E**: Number of edges (we examine each edge once)

### Space Complexity: O(V + E)
- **Graph storage**: O(V + E) for adjacency list
- **Seen set**: O(V) to track visited nodes
- **Stack/Queue**: O(V) in worst case
- **Recursion**: O(V) call stack depth

## Trees as Special Graphs

### Definition
A **tree** is a special type of graph that is:
- **Connected**: You can reach any node from any other node
- **Acyclic**: Contains no cycles

### Tree Properties
- If a tree has `n` vertices, it has exactly `n-1` edges
- There's exactly one path between any two nodes
- Adding any edge creates a cycle
- Removing any edge disconnects the graph

### Examples

**Tree (Connected + Acyclic):**
```
    1
   / \
  2   3
     /
    4
```

**Not a Tree (Has Cycle):**
```
    1
   /|\
  2-3-4
```

**Not a Tree (Disconnected):**
```
1-2   3-4
```

## Important Notes

### Cycle Detection
- Use a **seen set** to track visited nodes
- If we encounter a node we've already seen, we've found a cycle
- This prevents infinite loops in traversal

### Connected vs Disconnected Graphs
- **Connected**: Can reach any node from any other node
- **Disconnected**: Some nodes are unreachable from others

### Neighbors
- **Neighbors** of a node are all nodes directly connected to it by an edge
- In adjacency list: `graph[node]` gives all neighbors

## Complete Implementation Example

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, directed=True):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)
    
    def dfs_recursive(self, start):
        seen = set()
        result = []
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            result.append(node)
            
            for neighbor in self.graph[node]:
                dfs(neighbor)
        
        dfs(start)
        return result
    
    def bfs(self, start):
        seen = set()
        queue = deque([start])
        seen.add(start)
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return result

# Usage example
g = Graph()
edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,5], [5,4]]

for u, v in edges:
    g.add_edge(u, v)

print("DFS:", g.dfs_recursive(0))
print("BFS:", g.bfs(0))
```

## Summary

Graphs are fundamental data structures that model relationships between entities. Understanding graph representation and traversal algorithms (DFS and BFS) is crucial for solving many programming problems including pathfinding, social networks, dependency resolution, and more.

The key takeaways:
- Use adjacency lists for most implementations
- Always use a seen set to avoid infinite loops
- Choose DFS for deep exploration, BFS for level-by-level exploration
- Remember that trees are just connected, acyclic graphs