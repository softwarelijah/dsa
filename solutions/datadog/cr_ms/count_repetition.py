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
"""""

def count_repetitions(paragraph: str) -> int:

  word_count = {}
  current_word = ""
  for char in paragraph:
    if char.isalpha():
      current_word += char.lower()
    else:
      if current_word:
        word_count[current_word] = word_count.get(current_word, 0) + 1
        current_word = ""
  if current_word:
    word_count[current_word] = word_count.get(current_word, 0) + 1
  return sum(count - 1 for count in word_count.values() if count > 1)


def test_count_repetitions():

  assert count_repetitions("") == 0, "empty string should return 0"
  assert count_repetitions("hello HELLO Hello") == 2, "capitalization, should return 2"
  assert count_repetitions("    ") == 0, "empty spaces should return 0"
  assert count_repetitions("hello my name is Elijah") == 0, "all different words"
  print("test passed")

test_count_repetitions()

"""
DATA STRUCTURES:
- Hash Map (Dictionary): word_count dictionary maps each word to its frequency count
  - Provides O(1) average-case lookup, insertion, and update operations
  - Key: word (string), Value: count (integer)
- String: Used for current_word to build words character by character
  - Mutable accumulation of characters until a word boundary is found

ALGORITHMS:
- Single Pass Iteration: Traverse the input paragraph once, character by character
- Word Parsing: Build words by accumulating alphabetic characters and reset on non-alphabetic characters
- Frequency Counting: Use hash map to track occurrences of each word (case-insensitive)
- Aggregation: Sum up (count - 1) for all words that appear more than once

TIME COMPLEXITY: O(n + w)
- Where n is the length of the paragraph and w is the number of unique words
- We iterate through every character in the paragraph once: O(n)
- We iterate through the word_count dictionary at the end to compute the sum: O(w)
- Since w <= n (number of unique words can't exceed total characters), overall time is O(n)

SPACE COMPLEXITY: O(n)
- word_count dictionary stores at most w unique words, where w is the number of unique words
- In the worst case (all single-character words with spaces), w approaches n/2
- current_word can grow up to the length of the longest word, which is at most n
- Therefore, space complexity is O(n) in the worst case

Note: String concatenation (current_word += char) technically creates a new string each time,
which could make the time complexity O(n²) in the worst case for a single very long word.
For better performance with very long words, you could use a list and join at the end:
current_word = []
current_word.append(char.lower())
word = ''.join(current_word)
However, for typical paragraph inputs with reasonably-sized words, the current approach is fine.
"""