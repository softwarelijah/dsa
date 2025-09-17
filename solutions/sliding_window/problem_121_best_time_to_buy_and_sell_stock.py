class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize two pointers:
        # 'left' represents the day we buy
        # 'right' represents the day we sell
        left, right = 0, 1

        # Variable to track the maximum profit we can achieve
        maxP = 0

        # Loop while the right pointer has not reached the end of the prices list
        while right < len(prices):

            # If the current selling price is greater than the buying price,
            # then we can make a profit
            if prices[left] < prices[right]:
                # Calculate the profit if we buy at 'left' and sell at 'right'
                profit = prices[right] - prices[left]

                # Update maxP to be the maximum of the current maxP and this new profit
                maxP = max(maxP, profit)
            else:
                # If the selling price is less than or equal to the buying price,
                # it means this 'right' day could be a better day to buy.
                # So, we move 'left' up to 'right'.
                left = right

            # Move the right pointer forward to check the next day
            right += 1

        # After checking all pairs, return the maximum profit found
        return maxP
