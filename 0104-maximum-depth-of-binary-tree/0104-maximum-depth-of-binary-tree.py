# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: #base case
            return 0
        left = self.maxDepth(root.left) #search all left nodes for height
        right = self.maxDepth(root.right) #search all right nodes for height
        return max(left,right)+1


    
    