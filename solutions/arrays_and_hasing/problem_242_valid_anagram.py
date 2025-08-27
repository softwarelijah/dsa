class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time Complexity:
            - O(n), where n = length of s (or t). We loop through the strings once.
        Space Complexity:
            - O(1) if we assume only lowercase English letters (since at most 26 keys in the hashmaps).
            - O(n) in the general case (if the alphabet of possible characters can be very large).
        """

        # If the strings are not the same length, they cannot be anagrams
        if len(s) != len(t):
            return False  # changed from None to False for correctness
        
        # Declare two hashmaps (dictionaries in Python) to store character counts
        countS, countT = {}, {}

        # Loop through every character in both strings simultaneously
        for i in range(len(s)):
            # countS[s[i]] = 1 + countS.get(s[i], 0)
            # If s[i] already exists in countS, increment its count
            # If not, .get() returns 0 and we add 1 → first occurrence
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # Do the same for string t at index i
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Finally, compare the two hashmaps
        # If both have the exact same counts for each character, return True
        # Otherwise return False
        return countS == countT
