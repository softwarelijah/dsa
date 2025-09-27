class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes - each key is a character, value is another TrieNode
        self.children = {}
        # Boolean flag to mark if this node represents the end of a complete word
        self.endOfWord = False

class Trie:
    def __init__(self):
        # Create the root node - this is the starting point of our trie tree
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the root of the trie
        curr = self.root

        # Go through each character in the word we want to insert
        for c in word:
            # If this character doesn't exist as a child of current node
            if c not in curr.children:
                # Create a new node for this character
                curr.children[c] = TrieNode()
            # Move down to the child node for this character
            curr = curr.children[c]

        # We've processed all characters, so mark this node as end of a word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # Start searching from the root
        curr = self.root

        # Try to follow the path for each character in the word
        for c in word:
            # If this character path doesn't exist, the word isn't in the trie
            if c not in curr.children:
                return False
            # Move down to the child node for this character
            curr = curr.children[c]

        # We found a path for all characters, but check if it's actually a complete word
        # (not just a prefix of another word)
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start searching from the root
        curr = self.root

        # Try to follow the path for each character in the prefix
        for c in prefix:
            # If this character path doesn't exist, no words start with this prefix
            if c not in curr.children:
                return False
            # Move down to the child node for this character
            curr = curr.children[c]

        # We successfully followed the entire prefix path
        # Return True regardless of whether it's a complete word or not
        return True

# Example walkthrough:
# If we insert "cat" and "car":
#
# Root
#  └── c
#      └── a
#          ├── t (endOfWord = True)  ← "cat" ends here
#          └── r (endOfWord = True)  ← "car" ends here
#
# search("cat") → follows c→a→t, finds endOfWord=True → returns True
# search("ca") → follows c→a, but endOfWord=False → returns False
# startsWith("ca") → follows c→a successfully → returns True


#################################################################################

# No Comments Version of Solution

class TrieNode_nocomments:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie_nocomments:
    def __init__(self):
        self.root = TrieNode_nocomments()

    def insert_nocomments(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode_nocomments()
            curr = curr.children[c]
        curr.endOfWord = True

    def search_nocomments(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith_nocomments(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True