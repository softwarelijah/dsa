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

def bucket_partition(latencies, numBuckets, bucketWidth):
    # Initialize result array with 0 counts
    ans = [0] * numBuckets
    
    for latency in latencies:
        # Find the index of the bucket
        idx = latency // bucketWidth
        
        # If latency exceeds last bucket, cap it to the last one
        if idx >= numBuckets:
            idx = numBuckets - 1
        
        ans[idx] += 1
    
    return ans


# Example usage
latencies = [6, 7, 50, 100, 110]
numBuckets = 8
bucketWidth = 10
print(bucket_partition(latencies, numBuckets, bucketWidth))
# Output: [2, 0, 0, 0, 0, 1, 0, 2]



def bucket_partition_no_comments(latencies, numBuckets, bucketWidth):
    ans = [0] * numBuckets
    for latency in latencies:
        idx = latency // bucketWidth
        if idx >= numBuckets:
            idx = numBuckets - 1
        ans[idx]
    return ans
