"""
LeetCode-style Problem:

Given a paragraph (string), determine the total number of repeated words.
A word counts as repeated if it appears more than once. For each word,
the number of repetitions is (count - 1). Return the total repetitions.

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

# from collections import Counter
#
# class Solution:
#     def countRepetitions(self, paragraph: str) -> int:
#         # Normalize to lowercase and split words
#         words = paragraph.lower().split()
#
#         # Count occurrences
#         word_counts = Counter(words)
#
#         # Sum (count - 1) for words with count > 1
#         return sum(count - 1 for count in word_counts.values() if count > 1)
#
#
# # Example usage:
# paragraph = "the lion eats other sheep and the lion then sleeps while the sheep eats"
# sol = Solution()
# print(sol.countRepetitions(paragraph))  # Output: 5




class Solution2:
    def countRepitions2(self, paragragh2: str)  -> int:
        word_count = {}
        current_word = ""
        for char in paragragh2:
            if char.isalpha():
                current_word += char.lower()
            else:
                if current_word:
                    word_count[current_word] = word_count.get(current_word, 0) + 1
                    current_word = ""
        if current_word:
            word_count[current_word] = word_count.get(current_word, 0) + 1

            # the count - 1 here is so that we do not include the first word
            # if we want to incldue the first word here all we need to do is remove that -1
        return sum(count - 1 for count in word_count.values() if count > 1)

paragraph2 = "The quick brown fox jumps over the lazy dog. The dog barks at the fox. The fox runs away quickly."
sol2 = Solution2()
print(sol2.countRepitions2(paragraph2))