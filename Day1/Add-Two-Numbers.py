# Two Sum
# https://leetcode.com/problems/Add-Two-Numbers/
# Difficulty: Med

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        currentNode = head
        value = 0

        while l1 or l2 or value:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            sum = d1 + d2 + value
            value, digit = divmod(sum, 10)

            currentNode.next = ListNode(digit)
            currentNode = currentNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
