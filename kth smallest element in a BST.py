# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # number of elements visited
        stack = []
        ptn = root

        while ptn and stack:
            while pth:
                stack.append(ptn)
                ptn = ptn.left
            ptn = stack.pop()
            n += 1
            if n==k:
                return ptn.val
            ptn = ptn.right
            