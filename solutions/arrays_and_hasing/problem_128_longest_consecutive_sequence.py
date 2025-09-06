class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash set approach

        longest_streak = 0 # return variable
        num_set = set(nums) # declaring a set of numbers (no duplicates)

        # looping through each number in the set
        for i in num_set:

            # only start counting if 'i' is the start of a sequence
            # that happens when there is no number just before it (i-1 not in set)
            if i -1 not in num_set:
                current_num = i # starting number of the sequence
                current_streak = 1 # every sequence starts with at least length 1

                # keep moving forward while the next number exists in the set
                while current_num + 1 in num_set:
                    current_num += 1 # goes to the next number
                    current_streak += 1 # extends the streak length

                # update the longest streak if this sequence was longer
                longest_streak = max(longest_streak, current_streak)

        return longest_streak # return value