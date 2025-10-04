from typing import List  # Import for type hinting of list elements


# Dynamic Programming Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Return the minimum number of coins needed to make up 'amount'.
        If it is not possible, return -1.
        """
        # dp[i] will hold the fewest coins needed to make amount i
        # Initialize all as a large sentinel (amount + 1) meaning "unreachable" for now
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Build solutions for all amounts from 1 up to 'amount'
        for a in range(1, amount + 1):
            # Try every coin to see if it can help form amount 'a'
            for c in coins:
                # Only proceed if coin value does not exceed current sub-amount
                if a - c >= 0:
                    # Choose the better (smaller) count:
                    # existing best vs 1 coin (this one) + best way to make (a - c)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If still sentinel value, it's impossible; otherwise return the computed minimum
        return dp[amount] if dp[amount] != amount + 1 else -1


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

class Solution2:
    def coinChange2(self, coins: List[int], amount: int) -> int:


        # sorts the coins from largest to smallest
        # ex: [1, 5, 10, 25] becomes [25, 10, 5, 1]
        # the greedy strategy assumes using larger coins first minimizes the total count
        # this wont work for arbitrary coin systems though
        coins.sort(reverse=True)

        # count will track how many coins weve used (starts at 0)
        # remaining tracks how much money we still need to make (start at the full amount)
        # ex: count = 0
        # ex: remaining = 63
        count = 0
        remaining = amount

        # iterating through each coin denomination from largest to smallest
        # ex: 1st iteration: coin = 25, then coin = 10, then coin = 5, then coin = 1
        for coin in coins:

            # if weve already made the exact amount, stop early (optimization)
            # no need to check smaller coins if we're done
            if remaining == 0:
                break

            # calculates how many of this coin we can use (integer division)
            # ex: 63//25 = 2 (we can use two quarters),  cant use three because 3 * 25 = 75 > 63
            # TIP: explain that // is floor division
            num_coins = remaining // coin

            # this adds the number of coins we just used to our total count
            # ex from above: count = 0 + 2 = 2
            count += num_coins

            # subtracts the value we just covered from the remaining amount
            # ex: remaining = 63 - (2 * 25) = 63 - 50 = 13
            remaining -= num_coins * coin

        # returns the total number of coins used
        return count

s = Solution2()
print(s.coinChange2([1, 5, 10, 25], 63)) # expected 6
print(s.coinChange2([1,2,5], 11))
print(s.coinChange2([1], 0))
print(s.coinChange2([1], 1))
print(63//25)
print(13//10)
