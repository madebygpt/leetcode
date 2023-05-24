# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node as the head of the result list
        current = dummy  # Pointer to keep track of the current node
        carry = 0  # Variable to store the carry value
        
        while l1 or l2:
            sum_val = carry
            
            # Add the values from the two lists and the carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10  # Calculate the carry
            current.next = ListNode(sum_val % 10)  # Create a new node with the sum value
            
            current = current.next  # Move the current pointer to the next node
        
        # Check if there is a remaining carry
        if carry:
            current.next = ListNode(carry)
        
        return dummy.next  # Return the head of the result list
