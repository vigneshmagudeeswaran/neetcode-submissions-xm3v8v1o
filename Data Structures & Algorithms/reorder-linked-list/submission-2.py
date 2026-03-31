# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast= head,head.next
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        
        second = self.reverseLinkedList(slow.next)
        slow.next=None
        first= head
        while second:
            tmp1,tmp2 =first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

    def reverseLinkedList(self,head: Optional[ListNode]):
        prev= None
        curr = head
        while curr:
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
