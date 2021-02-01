# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
         
        if root == None:
            return 0
        
        # if the root node value within the range,
        if root.val >= low and root.val <= high:
            # add the value of the root node to the sum
            # check to the left
            left_sum = self.rangeSumBST(root.left, low, high)
            # check to the right
            right_sum = self.rangeSumBST(root.right, low, high)
            
            return root.val + left_sum + right_sum
        
        # if the root node value is below the range
        if root.val < low:
            # check to the right
            return self.rangeSumBST(root.right, low, high)
        
        # if the root node value is above the range
        if root.val > high:
            # check to the left
            return self.rangeSumBST(root.left, low, high)
        