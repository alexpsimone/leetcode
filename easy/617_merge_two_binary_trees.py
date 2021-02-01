# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
                
        # if the node is None on both trees
        if t1 == None and t2 == None:
            # then the node is None on the new tree
            return None
        
        # if the node only exists on one tree
        # then the value of the new node is the value of the existing node
        if t1 == None and t2 != None:
            return t2
        
        elif t1 != None and t2 == None:
            return t1
            
        # if the node exists on both trees
        else:
            # then the value of the new node is their sum
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        
        
        
