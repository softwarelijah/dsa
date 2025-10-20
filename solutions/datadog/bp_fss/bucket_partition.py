from typing import List

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

"""""

def bucketPartition(latencies: List[int], numBucket: int, bucketWidth: int) -> List[int]:
  ans = [0] * numBucket
  for latency in latencies:
    idx = latency // bucketWidth
    if idx >= numBucket:
      idx = numBucket - 1
    ans[idx] += 1
  return ans

def bucket_partition_test():
  result = bucketPartition([6,7,50,100,110], 8, 10)
  assert result == [2, 0, 0, 0, 0, 1, 0, 2], "input 1"
  print("input 1 passed")

  result = bucketPartition([], 8, 10)
  assert result == [0, 0, 0, 0, 0, 0, 0, 0]
  print("input 2 passed: empty latencies")

bucket_partition_test()

"""
DATA STRUCTURES:
- Array (List): ans array stores the count of latencies for each bucket
  - Fixed-size array initialized with zeros
  - Provides O(1) access and update by index
  - Index represents bucket number, value represents frequency count

ALGORITHMS:
- Bucketing/Hashing: Map each latency value to a bucket index using integer division
  - Formula: bucket_index = latency // bucketWidth
  - This distributes values into ranges [0, bucketWidth), [bucketWidth, 2*bucketWidth), etc.
- Clamping: Ensure overflow values (latency >= numBucket * bucketWidth) go to the last bucket
  - Uses conditional check: if idx >= numBucket, set idx = numBucket - 1
- Frequency Counting: Increment the count in the appropriate bucket for each latency

TIME COMPLEXITY: O(n + b)
- Where n is the length of latencies and b is numBucket
- Initializing the ans array with zeros: O(b)
- Iterating through all latencies and placing them in buckets: O(n)
- Each bucket assignment is O(1) (integer division and array access)
- Total: O(n + b)

SPACE COMPLEXITY: O(b)
- Where b is numBucket
- The ans array stores exactly numBucket elements: O(b)
- Only a constant amount of additional space is used (idx, latency variables): O(1)
- Total space: O(b)

Note: This solution is optimal for the problem since we must:
1. Create an output array of size numBucket (unavoidable O(b) space)
2. Process each latency at least once (unavoidable O(n) time)
"""