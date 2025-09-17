class Solution:
    def isValid(self, s: str) -> bool:
      # Stack to hold opening brackets we need to match later
        stack = []

        # Map each closing bracket to the opening bracket it requires
        # (keys are closers; values are the exact opener that must be on top of the stack)
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # Iterate over each character c in the string s
        for c in s:
            # If c is a closing bracket (one of the keys in closeToOpen)...
            if c in closeToOpen:
                # Check two things:
                # 1) The stack is not empty (there is something to match against)
                # 2) The top of the stack equals the required opening bracket for c
                if stack and stack[-1] == closeToOpen[c]:
                    # It's a correct match, so remove the matched opening bracket
                    stack.pop()
                else:
                    # Either the stack was empty (no opener), or the top didn't match the closer
                    # In both cases the string is invalid
                    return False
            else:
                # c is an opening bracket — push it so we can match it with a future closer
                stack.append(c)

        # If the stack is empty, all opens were properly matched and popped → valid
        # If not empty, there are unmatched opening brackets → invalid
        return True if not stack else False