# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast pointer by n + 1 steps to create a gap of n + 1 nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers forward until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Unlink the nth node from the end
        slow.next = slow.next.next

        return dummy.next
