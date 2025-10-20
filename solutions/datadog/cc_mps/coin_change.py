from typing import List

"""
Problem StatementProblem Statement: US Coin Change

You are given an integer array coins representing US coin denominations 
[1, 5, 10, 25] (penny, nickel, dime, quarter) and an integer amount 
representing a total amount of money in cents.

Return the fewest number of coins that you need to make up that amount 
using a greedy algorithm.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 5, 10, 25], amount = 63
Output: 6
Explanation: 63 = 25 + 25 + 10 + 1 + 1 + 1

Example 2:
Input: coins = [1, 5, 10, 25], amount = 41
Output: 4
Explanation: 41 = 25 + 10 + 5 + 1

Example 3:
Input: coins = [1, 5, 10, 25], amount = 0
Output: 0
"""

def coinChange(coins: List[int], amount: int) -> int:

  # we know that the coins are [1, 5, 10, 25]
  coins.sort(reverse=True) # so we can check biggest coins first (25, 10, 5, 1)
  remaining = amount # use to check how much more money is left
  count = 0 # for how many coins we have so if amount is 50, this will be 2 (2 quarters)
  for coin in coins:
    if remaining == 0:
      break

    num_coins = remaining // coin # 50 // 25 == 2, this line is very much needed ( i tried without it and it does not work)
    count += num_coins
    remaining -= num_coins * coin
  return count



def coin_change_test():

  result = coinChange([1, 5, 10, 25], 50)
  assert result == 2, "test 1 failed: amount: 50, should return 2"
  print("test 1 passed: returned 2")

  result1 = coinChange([1, 5, 10, 25], 0)
  assert result1 == 0, "test 2 failed: amount: 0, should return 0"
  print("test 2 passed: returned 0")

coin_change_test()

"""
DATA STRUCTURES:
- Array (List): coins array stores available coin denominations
  - Sorted in descending order to enable greedy selection
  - Provides O(1) access during iteration
- Integer Variables: remaining (tracks amount left), count (accumulates total coins), num_coins (coins of current denomination)

ALGORITHMS:
- Greedy Algorithm: Make locally optimal choice at each step by selecting the largest coin that fits
  - Process coins from largest to smallest denomination
  - For each coin, use as many as possible (remaining // coin)
  - Subtract used value from remaining amount
  - Works optimally for canonical coin systems like US coins
- Sorting: Order coins in descending order to ensure largest coins are tried first
  - Uses reverse sort: coins.sort(reverse=True)
- Integer Division: Calculate maximum number of coins of each denomination that fit in remaining amount
  - Formula: num_coins = remaining // coin

TIME COMPLEXITY: O(n log n + n)
- Where n is the number of coin denominations
- Sorting the coins array: O(n log n)
- Iterating through all coins: O(n)
- Each iteration performs constant-time operations (division, addition, subtraction): O(1)
- Total: O(n log n)

However, since the problem specifies coins = [1, 5, 10, 25] (fixed set of 4 coins):
- Sorting 4 elements is effectively O(1) constant time
- Iterating through 4 coins is O(1) constant time
- Therefore, for this specific problem: O(1)

SPACE COMPLEXITY: O(1)
- Only a constant amount of extra space is used (remaining, count, num_coins variables)
- The sorting is done in-place on the input array
- No additional data structures are created that scale with input size
- Total space: O(1)

Note: This greedy approach works optimally for US coin denominations because they form
a "canonical" coin system. However, the greedy algorithm does NOT always produce the
optimal solution for arbitrary coin sets. For example, with coins = [1, 3, 4] and 
amount = 6, greedy gives 3 coins (4 + 1 + 1) but optimal is 2 coins (3 + 3).
For arbitrary coin sets, dynamic programming would be needed to guarantee optimal results.
"""