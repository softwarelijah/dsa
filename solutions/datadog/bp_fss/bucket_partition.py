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

def bucket_partition(latencies: List[int], numBuckets: int, bucketWidth: int) -> List[int]:

  ans = [0] * numBuckets
  for latency in latencies:
    idx  = latency // bucketWidth
    if idx >= numBuckets:
      idx = numBuckets - 1
    ans[idx] += 1
  return ans

def test_bucket_partition():
  # empty latency test passed
  result = bucket_partition([], 5, 10)
  assert result == [0, 0, 0, 0, 0], "Empty array should return all zeroes"
  print("empty latency test passed")


  # example input passed 
  result = bucket_partition([6, 7, 50, 100, 110], 8, 10)
  assert result == [2,0,0,0,0,1,0,2], "example input"
  print("example input passed") 

test_bucket_partition()