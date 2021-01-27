# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Do the lists always combine toward the tail? Is this implied?
# Edge case: one or more list is empty
# Edge case: only one node for either list
# Edge case: LL A and B are the same single node/intersection is at first node

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # If headA or headB has no value (empty list?), return null
        if headA == None or headB == None:
            return None
        
        # Create pointers equal to the head nodes of each LL
        pA = headA
        pB = headB
        
        # Continue looping while the nodes (not just their values) are unequal.
        while pA != pB:
            
            # Pass through both lists, one node at a time.
            # Loop around back to the head of the OTHER list when the tail is reached.
            # By the end of the 2nd loop, the pointers will be at the same node.
            
            if pA.next == pB.next and pA.next == None:
                return None
            
            if pA.next == None:
                pA = headB
            else:
                pA = pA.next
                
            if pB.next == None:
                pB = headA
            else:
                pB = pB.next

        
        return pA