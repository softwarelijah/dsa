class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If the strings are not the same length, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Use two hashmaps (dictionaries) to count character frequencies
        countS, countT = {}, {}

        # Iterate through both strings simultaneously
        for i in range(len(s)):
            # For each character in s, increment its count in countS
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # For each character in t, increment its count in countT
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Two strings are anagrams if their frequency dictionaries match
        return countS == countT


# -------------------------------
# Time Complexity: O(n)
#   - One pass through the strings of length n to build the dictionaries
#   - Dictionary comparison is O(1) if alphabet is fixed (e.g., 26 letters)
#
# Space Complexity: O(1) for fixed alphabet, O(k) in general
#   - At most 26 entries per dictionary if only lowercase English letters
#   - In general, O(k) where k = number of unique characters
# -------------------------------
