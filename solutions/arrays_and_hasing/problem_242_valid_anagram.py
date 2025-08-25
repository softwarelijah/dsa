class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if the lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False


        count = {} # creating a dictionary to keep track of character counts in s

        # counting the frequency of each character in s
        for char in s:
            # if char exist, increment count, otherwise start at 0
            count[char] = count.get(char, 0) + 1

        # subtract frequency using characters from t
        for char in t:
            # if char not found in dictionary: t has an extra character so not an anagram
            if char not in count:
                return False

            # decrease the counter for this char
            count[char] -= 1

            # if the count goes below 0, t has too many of this char, not an anagram
            if count[char] < 0:
                return False

            # if all counts balance out, strings are anagrams
        return True


# O(N) space and time complexity for this solution