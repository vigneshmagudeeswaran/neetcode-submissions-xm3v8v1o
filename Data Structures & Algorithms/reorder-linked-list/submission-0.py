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
            fast= fast.next.next
        
        
        second =self.reverseList(slow.next)
        slow.next=None

        first= head

        while second:
            tmp1,tmp2 =first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

    
    def reverseList(self,head: Optional[ListNode]):
        prev=None
        curr=head
        
        while curr:
            tmp = curr.next
            curr.next=prev
            prev=curr
            curr= tmp 
        return prev     