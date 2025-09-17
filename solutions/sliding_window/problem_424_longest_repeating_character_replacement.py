class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store character counts in the current window
        count = {}
        
        # Result variable to store the maximum length of a valid substring
        res = 0
        
        # Left pointer for the sliding window
        l = 0
        
        # Iterate with the right pointer over each character in the string
        for r in range(len(s)):
          
            # Add the current character to the count dictionary (or increment if already present)
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # If the number of characters we need to change to make the
            # window uniform is greater than k, shrink the window from the left
            while (r - l + 1) - max(count.values()) > k:
                # Decrease the count of the character that is leaving the window
                count[s[l]] -= 1
                # Move the left pointer to shrink the window
                l += 1
            
            # Update the result with the maximum window size seen so far
            res = max(res, r - l + 1)
        
        # Return the length of the longest valid substring
        return res
