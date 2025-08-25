class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {} # create an empty dictionary to store counts of each number
        # looping through each number in the input list
        for num in nums:
            # for each number, update its frequency
            # - count.get(num, 0) returns the current count if it exists, otherwise 0
            # add 1 to increment the count
            count[num] = 1 + count.get(num, 0)

        # create an empty list to hold [frequency, number] pairs
        arr =[]

        #iterate through each (num, cnt) pair from the dictionary
        for num, cnt in count.items():
            # append the pair as [count, num] so we can sort by count
            arr.append([cnt, num])
            # sort the list of count [count, num] pairs in ascending order by default
            # after sorting, elements with smaller counts are at the front
        arr.sort()

        # prepare a result list to collect the top k frequent elements
        res = []

        # keep adding the frequent elements until we have k of them
        while len(res) < k:

            # arr.pop() removes the last element in arr (largest count, since arr is sorted ascending)
            # [1] selects the number part (not the count)
            res.append(arr.pop()[1])

            # return final list of top k frequent numbers
        return res