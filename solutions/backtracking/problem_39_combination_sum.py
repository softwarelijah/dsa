from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # Holds all valid combinations that add up to target

        def dfs(i, cur, total):
            # i: current index in candidates we are considering
            # cur: current combination we are building
            # total: sum of numbers currently in cur

            if total == target:
                # Found a valid combination; make a copy and store it
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                # Went past the list OR sum already too large; stop exploring this path
                return

            # Choice 1: include candidates[i] again (can reuse same number)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])  # Stay on same index to allow reuse
            cur.pop()  # Undo the choice (backtrack)

            # Choice 2: skip this number and move to the next one
            dfs(i + 1, cur, total)

        # Start depth-first search from index 0 with empty combination and sum 0
        dfs(0, [], 0)
        return res  # Return all found combinations
