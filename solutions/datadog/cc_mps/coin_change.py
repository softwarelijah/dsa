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

def coin_change(coins: List[int], amount: int) -> int:

  # [25, 10, 5, 1]
  coins.sort(reverse=True)
  count = 0 
  remaining = amount 

  for coin in coins:
    if remaining == 0: 
      break

    
    num_coins = remaining // coin 
    count += num_coins 
    remaining -= num_coins * coin 
  return count


def coin_change_test():
  result = coin_change([1, 5, 10, 25], 63)
  assert result == 6, "test input 1"
  print("input 1 passed")


  result = coin_change([1, 5, 10, 25], 41)
  assert result == 4, "test input 2"
  print("input 2 passed")

  result = coin_change([1, 5, 10, 25], 0)
  assert result == 0, "test input 3"
  print("input 3 passed")


coin_change_test()