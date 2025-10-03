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


class Solution:
    def count_repetitions(self, paragraph: str)  -> int:

        # creating a empty dictionary to map each normalized word -> occurrence count
        # will look like {'the': 3, 'lion': 2 etc..} | KV = {'word': '# of repetitions}
        word_count = {}

        # this is a buffer string where we accumulate characters that belong to the current word
        # as we scan the paragraph character by character
        current_word = ""

        # iterate over the paragraph one character at a time.
        # this will let us precisely control what counts as part of a word and what is a delimeter ("." or "," or " "
        for char in paragraph:

            # we are checking if the character is an alphabetic character (edge case, this function finds most characters for other languages too and different fonts)
            # if it is a "." or "," or something along those lines it will not fall into this statement
            if char.isalpha():
                # if the character is a letter
                # we are going to convert it to lowercase, so "the" "THE" or "The" will all be treated the same
                # append it to current_word, were still building the same word
                # this is where we normalize it
                current_word += char.lower()

            # if it is NOT a letter (e.g space, comma, period, emoji) that means the current word just ended
            # right now cw = "the"
            else:
                # as long as there is some value still in current word (we havent reached the end yet)
                # also avoids counting multiple delimiters in a row
                if current_word:

                    # if current_word exists in the dictionary, it returns its current count
                    # if current_word does not exist yet, it returns 0
                    # basically checks if the word is in the map
                    # if it hasn't been found yet it will add it to the map
                    # if it has already been found before it will just increment the value
                    word_count[current_word] = word_count.get(current_word, 0) + 1 # .get() retrieves the value (int) for the key current_word

                    # reset the buffer string to find the next word in our paragraph
                    # there will never be more than one word in this string
                    current_word = ""

        # if there is no delimiter at the end, we will come here, this is the final word check
        # this will ONLY find the last word if there is no delimiter to not jump into the else above
        if current_word:
            # exact same sentence at the end, just processes the last word if there is no delimiter to end the sentence
            word_count[current_word] = word_count.get(current_word, 0) + 1

        # the count - 1 here is so that we do not include the first word
        # if we want to include the first word here all we need to do is remove that -1
        return sum(count - 1 for count in word_count.values() if count > 1)

        # word_count.values() this gets all the counts from the dictionary, ignoring the words themselves
        # If word_count = {'the': 3, 'lion': 2, 'sleeps': 1}, then word_count.values() gives us [3, 2, 1]
        # [3, 2, 1], for count in word_count.values(), were iterating through [3,2,1]
        # we only care about words that appeared more than once (i.e they were repeated) so if a word
        # only repeated 1 time we skip it
        # so 3 and 2 pass
        # then -1 from 3 and 2 because we dont want to count the first occurrence so it will be [2, 1]
        # then just find the sum(2,1)
example = "the lion eats other sheep and the lion then sleeps while the sheep eats"
sol = Solution()
print(sol.count_repetitions(example))



























# count the words that repeat in a paragraph
# don't count the first occurrence of the word
# so if we have "the the the" we only want to return 2

class Solution2():
    def count_words(self, paragraph2: str) -> int:

        word_count = {}
        current_word = ""
        for char in paragraph2:
            if char.isalpha():
                current_word += char.lower()
            else:
                if current_word:
                    word_count[current_word] = word_count.get(current_word, 0) + 1
                    current_word = ""
        if current_word:
            word_count[current_word] = word_count.get(current_word, 0) + 1
        return sum(count - 1 for count in word_count.values() if count > 1)



example = "the the the the the"
sol = Solution2()
print(sol.count_words(example))
