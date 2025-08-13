class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if "++" in op:
                x += 1
            else:
                x-= 1
        return x

# O(n) time complexity
# O(1) space complexity only added one integer variable