# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    
    if p == None or q == None:
        return False

    # traverse tree p, one node at a time
    to_visit_p = [p]
    # also traverse tree q
    to_visit_q = [q]

    while to_visit_p and to_visit_q:
        
        # if you get to the end of one queue before the other, return false
        if not to_visit_p or not to_visit_q:
            return False
        
        # take current node from front of queue
        current_p = to_visit_p.pop()
        current_q = to_visit_q.pop()
        
        # protection in case there is a NoneType value
        if (current_p.val == None and current_q.val != None) or (current_p.val != None and current_q.val == None):
            return False
        
        # at each node, check to see if their values are equal
        # if they are ever unequal, then return False
        if current_p.val != current_q.val:
            return False
        
        # otherwise, extend the queue with children of current nodes
        if current_p.left:
            to_visit_p.append(current_p.left)
            to_visit_q.append(current_q.left)
        if current_p.right:
            to_visit_p.append(current_p.right)
            to_visit_q.append(current_q.right)

    # if you make it to the end of the search, return True
    return True

# p = TreeNode(1)
# q = TreeNode(1)
# p_2 = TreeNode(None)
# q_2 = TreeNode(2)
# p_3 = TreeNode(3)
# q_3 = TreeNode(3)

# p.left = p_2
# p.right = p_3
# q.left = q_2
# q.right = q_3

p = None
q = None

print(isSameTree(p, q))