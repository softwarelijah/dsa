from typing import List
""""""
"""
Problem: Bucket Partition
-------------------------
Given an array of latencies, numBuckets, and bucketWidth:
- Create `numBuckets` number of buckets of length `bucketWidth`, starting at 0.
- Place each latency into its corresponding bucket based on its value.
- Any latency higher than the last bucket should be placed into the last bucket.
- Return an array `ans` of size numBuckets where ans[i] is the number of latencies in bucket i.

Example:
Input:
  latencies = [6, 7, 50, 100, 110]
  numBuckets = 8
  bucketWidth = 10
Output:
  [2, 0, 0, 0, 0, 1, 0, 2]

"""


# couple of notes:
#

class Solution():
    # def bucket_partition(self, latencies: List[int], numBuckets: int, bucketWidth: int) -> List[int]:
    #     # latencies - the input data were categorizing (list of numbers)
    #     # numBuckets - how many categories/bins were creating
    #     # bucketWidth - the size and range of each bucket
    #     # think of this question as creating a histogram, we are dividing a continous range into discrete intervals.
    #     # each bucket represents a range
    #
    #
    #     # initializing the result array
    #     # this creates a list with numBuckets elements all initialized to 0
    #     # so if numBuckets = 3, this looks like [0, 0, 0]
    #     # we are starting with zero because were counting how many latencies fall into each bucket
    #     # we start from zero and increment as we find latencies that belong in each bucket
    #     # each position in ans, represents one bucket and the value at that position will be the count
    #     # why pre allocate? its more effcient to create the array once at correct size rather than grow it dynamically with something like .append()
    #     ans = [0] * numBuckets
    #
    #     # here we are just going through each latency one by one
    #     # we will examine each latency and determine which bucket it belongs too
    #     for latency in latencies:
    #
    #         # now we are going to calculate the bucket index
    #         # uses integer division to determine which bucket the latency belongs too
    #         # using integer division is important because it naturally groups ranges
    #         # latency // bucketWidth tells us how many complete bucket widths fit into this latency
    #         # which bucket range does this fall into
    #         idx = latency // bucketWidth
    #
    #
    #         # here we will be handling the overflow
    #         # if the calculated index exceeds the number of buckets, we will force it into the last bucket
    #         if idx >= numBuckets:
    #
    #             # the - 1 will automatically place it in the last bucket since arrays are 0 indexed
    #             idx = numBuckets - 1
    #
    #
    #         # here we are incrementing the bucket count
    #         # this adds 1 to the count in the appropriate bucket
    #         # were counting the occurences and each latency adds one more item to its bucket
    #         ans[idx] += 1
    #
    #         # return the final counts
    #     return ans



    def bucket_partition2(self, latencies2: List[int], bucketWidth: int, numBuckets: int) -> List[int]:
        ans = [0] * numBuckets
        for latency in latencies2:
            idx = latency // bucketWidth
            if idx >= numBuckets:
                idx = numBuckets - 1
            ans[idx] += 1
        return ans

sol = Solution()
latencies = [6,7,50,100,110]
numBuckets = 8
bucketWidth = 10

result = sol.bucket_partition2(latencies, bucketWidth, numBuckets)
print(result)



