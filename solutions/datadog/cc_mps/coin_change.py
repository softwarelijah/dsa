from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int ) -> int:

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

sol = Solution()
print(sol.coinChange([1, 5, 10, 25], 100))