"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.

"""


"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
"""


"""
Problem 2: Total Size of File System, you are given the root of a file system represented as a tree. Each node has the following properties:
name: a string representing the name of the file or directory
size: an integer representing the size of the file (0 for directories)
children: a list of child nodes (empty if it is a file)
Return the total size of the file system rooted at the given node.
If the node is a file, return its size.
If the node is a directory, recursively sum the sizes of all its children.


Input 1:
root = {
  "name": "root", 
  "size": 0,
  "children": [
    {"name": "file1.txt", "size": 10, "children": []},
    {"name": "file2.txt", "size": 20, "children": []},
    {"name": "subfolder", "size": 0,
      "children": [
        {"name": "subfile1.txt", "size": 5, "children": []},
        {"name": "subfile2.txt", "size": 15, "children": []}
      ]
    }
  ]
}

Output: 50
"""


"""
Problem Statement: US Coin Change

You are given an integer array coins representing US coin denominations 
[1, 5, 10, 25] (penny, nickel, dime, quarter) and an integer amount 
representing a total amount of money in cents.

Return the fewest number of coins that you need to make up that amount 
using a greedy algorithm.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 5, 10, 25], amount = 63
Output: 6
Explanation: 63 = 25 + 25 + 10 + 1 + 1 + 1

Example 2:
Input: coins = [1, 5, 10, 25], amount = 41
Output: 4
Explanation: 41 = 25 + 10 + 5 + 1

Example 3:
Input: coins = [1, 5, 10, 25], amount = 0
Output: 0
"""


"""
Problem: Bucket Partition
-------------------------
Given an array of latencies, numBuckets, and bucketWidth:
- Create `numBuckets` number of buckets of length `bucketWidth`, starting at 0.
- Place each latency into its corresponding bucket based on its value.
- Any latency higher than the last bucket should be placed into the last bucket.
- Return an array `ans` of size numBuckets where ans[i] is the number of latencies in bucket i.

Example:
Input:
  latencies = [6, 7, 50, 100, 110]
  numBuckets = 8
  bucketWidth = 10
Output:
  [2, 0, 0, 0, 0, 1, 0, 2]
"""


"""
Given a paragraph (string), determine the total number of repeated words.
A word counts as repeated if it appears more than once. For each word,
the number of repetitions is (count - 1). Return the total repetitions. (IMPORTANT) 

Example 1:
Input: paragraph = "the lion eats other sheep and the lion then sleeps while the sheep eats"
Output: 5
Explanation:
- "the" appears 3 times → 2 repetitions
- "lion" appears 2 times → 1 repetition
- "eats" appears 2 times → 1 repetition
- "sheep" appears 2 times → 1 repetition
Total repetitions = 2 + 1 + 1 + 1 = 5

Constraints:
- 1 <= len(paragraph) <= 10^5
- Paragraph consists of lowercase and uppercase letters and spaces.
"""


"""
Maximum Path Sum in an N-ary Tree

Problem Statement
Given an N-ary tree where each node contains an integer value and can have any number of children (0 or more), find the **maximum path sum** in the tree.

A path is defined as any sequence of nodes in the tree where each pair of adjacent nodes has a **direct parent-child relationship**.  
The path must contain **at least one node** and **does not need to pass through the root**.

The path sum is the sum of all node values in the path.

The root of an N-ary tree represented by a `Node` class with the following structure:

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
"""