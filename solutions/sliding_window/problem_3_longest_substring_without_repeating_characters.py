class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # set to store characters currently in the window
        charSet = set()

        # left pointer for the sliding window
        l = 0
        # result variable that will store the length to return
        res = 0

        # right pointer of the sliding window
        for r in range(len(s)):

            # if we encounter a duplicate, we shrink the window from the left
            # until the character is removed
            while s[r] in charSet:

                # remove the character at the left pointer from the set
                # and move the left pointer to the right
                charSet.remove(s[l])
                l += 1

            # now that s[r] is no longer in the set, add it to the set
            charSet.add(s[r])

            # update the result with the maximum length found so far
            # (r - l + 1) is the current window length
            res = max(res, r - l + 1)
        return res