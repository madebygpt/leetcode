class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node for the result linked list
    curr = dummy  # Pointer to the current node
    
    carry = 0  # Carry-over value
    
    while l1 or l2 or carry:
        # Calculate the sum of the current digits and carry-over
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        # Calculate the value and carry-over for the current digit
        digit = sum_val % 10
        carry = sum_val // 10
        
        # Create a new node with the calculated digit and add it to the result linked list
        curr.next = ListNode(digit)
        curr = curr.next
    
    return dummy.next  # Return the result linked list excluding the dummy node

# Test the function with given examples
# Example 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 7 0 8

print()  # Print a new line for clarity

# Example 2
l1 = ListNode(0)

l2 = ListNode(0)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 0

print()  # Print a new line for clarity

# Example 3
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 8 9 9 9 0 0 0 1
