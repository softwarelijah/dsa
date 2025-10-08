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

    num_coins = remaining // coin # 50 // 25 == 2
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
