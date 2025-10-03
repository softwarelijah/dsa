from typing import List  # Import for type hinting of list elements

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