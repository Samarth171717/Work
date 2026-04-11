# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr=head
        prev=None
        while curr:
            next_temp=curr.next
            curr.next=prev
            prev=curr
            curr=next_temp
        return prev


        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        