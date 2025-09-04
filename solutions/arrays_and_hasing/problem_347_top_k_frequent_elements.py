class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count each element with hashmap(counter)
        # use a heap to find the k elements with the highest frequency
        # then return them


        if k == len(nums): # if the frequent element is the length of the array, all of the array are the same integer?
            return nums

        # build hashmap: character and how often it appears
        # counts how many times each element appears
        count = Counter(nums)

        # build heap of top k frequent elements and convert it to output array
        # the heap keeps the smallest or largest element at the top
        # heap.nlargest builds temporary max-heap internally to find k largest elements
        return heapq.nlargest(k, count.keys(), key=count.get)